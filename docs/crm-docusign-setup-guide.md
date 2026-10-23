# DocuSign → CRM Setup Guide

**Status:** Implementation runbook · **Date:** 12 Oct 2026 · **For:** CRM developer + DocuSign account admin
**Companion:** `crm-docusign-contract-automation-spec.md` (what we're building and why) · published artifact "Contract Automation" (stakeholder proposal).
**Scope:** Connect DocuSign to the CRM so Bookings can generate, send, track and file contracts automatically. This is the wiring; the spec is the design.

> **Build in the sandbox first.** Everything below works in a free DocuSign **developer (demo)** account, including Doc Gen and Connect. Nothing is paid until you promote to production (Part I). Do not build against a live account.

**Who does what**

| Step area | Owner |
|---|---|
| DocuSign account, app, keys, consent, Connect config | DocuSign **admin** |
| Store secrets, write the integration code, listener | CRM **developer** |
| Approve templates before they go live | **Legal** (spec §15 D1) |

**The integration pattern** (spec §07): the CRM talks to DocuSign server-to-server using **OAuth JWT grant** as a dedicated **system user** — never a staff member's personal login. When this guide says "the CRM calls…", it means a backend service authenticated that way.

---

## Part A — Create the account, app and keys (sandbox)

### A1. Create a developer account
1. Go to **developers.docusign.com** → **Create account** (free). This is the demo environment (`demo.docusign.net`), separate from any live account.
2. In the setup wizard, when asked **"What do you want to build?"**, choose **API Integration** (not Workflow, not Extension App). Workflow = DocuSign's own no-code Maestro; Extension App = a marketplace app — neither is us.

### A2. Create the integration key (the "app")
1. In the developer console: **Settings → Integrations → Apps and Keys**.
2. **Add App and Integration Key**. Name it e.g. `Cams-CRM-Contracts`.
3. The **Integration Key** (a GUID) is shown. This is your OAuth **client ID**. Record it.
4. Under **Authentication**, select **JWT (service integration)** — the unattended CRM-to-DocuSign pattern. (Authorization Code grant is for apps where a human logs in; not us.)

### A3. Generate the RSA keypair
1. In the same app, under **Service Integration**, click **Generate RSA** (or **Add RSA Keypair**).
2. DocuSign shows the **public** and **private** key once. **Copy the private key now** — it is not shown again. The CRM signs its JWT with this private key.
3. Store the private key as a secret (Part C). DocuSign keeps the public key.

### A4. Add a redirect URI
1. Still in the app, add a **Redirect URI**, e.g. `http://localhost:8080/callback` (or a real CRM URL).
2. This is used **only** to grant consent the first time (B1). It is not used for ongoing API calls.

### A5. Collect the five values the CRM needs
Record these — they are the integration's identity:

| Value | Where to find it | Example |
|---|---|---|
| **Integration Key** (client ID) | Apps and Keys → your app | `a1b2c3d4-…` |
| **RSA private key** | Generated in A3 (copy once) | `-----BEGIN RSA PRIVATE KEY-----…` |
| **Impersonated User ID** (API Username GUID) | **Settings → Users →** the system user → **API Username** | `f9e8d7c6-…` |
| **Account ID** (API Account ID) | Apps and Keys (top) or Admin → Account | `11112222-…` |
| **Account Base URI** | Returned by the `/oauth/userinfo` call after first auth (B2); e.g. `https://demo.docusign.net` | `https://demo.docusign.net` |

> **Create a dedicated system user** (e.g. `crm-integration@yourdomain`) and impersonate **that** user, not a real person. If a staff member leaves, the integration keeps working. Give that user permission to send and manage envelopes.

---

## Part B — Authorize the integration (JWT consent)

JWT impersonation requires a **one-time consent** that the account allows the app to act as the user. Without it, the first token call fails with `consent_required`.

### B1. Grant consent
Two ways — do one:

**Admin consent (recommended for production).** An org admin grants consent for the whole organization to the Integration Key once, in **Admin → Connected Apps** (requires a claimed email domain). Preferred because it needs no per-user browser step.

**Per-user consent (fine for sandbox).** Open this URL in a browser, signed in as the **impersonated user**, and click **Allow**:
```
https://account-d.docusign.com/oauth/auth
  ?response_type=code
  &scope=signature%20impersonation
  &client_id=YOUR_INTEGRATION_KEY
  &redirect_uri=YOUR_REDIRECT_URI
```
(Demo uses `account-d.docusign.com`; production uses `account.docusign.com`.) You'll be redirected to the redirect URI — the redirect itself doesn't matter; the consent is now recorded. Needed scopes: **`signature impersonation`**.

### B2. Get a token and the base URI
The CRM now authenticates on its own:
1. Build and sign a JWT assertion (iss = Integration Key, sub = impersonated User ID, aud = `account-d.docusign.com`, scope `signature impersonation`), signed with the RSA private key. Use DocuSign's SDK (`requestJWTUserToken`) — don't hand-roll the JWT.
2. POST it to the token endpoint:
   ```
   POST https://account-d.docusign.com/oauth/token
   grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=<signed JWT>
   ```
   Response: a short-lived **access token** (~1 hour). Cache it; refresh before expiry.
3. Call **`GET /oauth/userinfo`** (same host) with the token → returns the **Account ID** and **Base URI** (`base_uri`). All eSignature calls use `BASE_URI/restapi/v2.1/accounts/ACCOUNT_ID/…`.

**Checkpoint:** a successful token + `userinfo` call means auth is wired. You now have everything in A5.

---

## Part C — Store the credentials in the CRM

Put these in the CRM's **secret store / environment**, never in code or the repo:

| CRM config key | Value |
|---|---|
| `DOCUSIGN_INTEGRATION_KEY` | Integration Key (A5) |
| `DOCUSIGN_USER_ID` | Impersonated User ID GUID (A5) |
| `DOCUSIGN_ACCOUNT_ID` | Account ID (A5) |
| `DOCUSIGN_PRIVATE_KEY` | RSA private key (A3) — secret |
| `DOCUSIGN_AUTH_SERVER` | `account-d.docusign.com` (demo) → `account.docusign.com` (prod) |
| `DOCUSIGN_BASE_PATH` | from `userinfo`, e.g. `https://demo.docusign.net/restapi` |
| `DOCUSIGN_HMAC_KEY` | Connect HMAC secret (Part F) |

Promoting to production later means swapping only the auth server, base path, keys and account ID — not the code.

---

## Part D — Build the Doc Gen templates

This is how a contract gets generated from booking data (spec §05, §08). Do this once per approved template (event type × venue).

1. **Write the .docx template.** Take the attorney-approved contract and replace each variable with a merge placeholder in double braces: `{{client_name}}`, `{{venue}}`, `{{event_date}}`, `{{total}}`, etc. For optional clauses, use DocuSign's conditional syntax so a clause appears only when its data is present (e.g. the alcohol-insurance clause when `addons` includes `alcohol_service`).
2. **Create a DocuSign template** and attach the .docx **as a Doc Gen document**. Important: the template's document must be flagged `"isDocGenDocument": "true"`. The web UI's "Create Template" button does **not** attach Doc Gen form fields, so create the template via the **API (JSON upload)** if you want the fields stored with it.
3. **Add signature/date tabs** for the signer(s) in the template, with the correct **routing order** for multi-signer contracts (spec §15 D2).
4. **Record the template ID** and map each `(event type × venue)` to it (e.g. `crown_prince__wedding__v4`). The CRM uses this map to pick the template.
5. **Verify** the field list: `GET …/templates/{templateId}/documents/{documentId}/docGenFormFields` should list every placeholder. If it returns none, the placeholders aren't set up as Doc Gen fields — fix the .docx/flag before going further.

> **Gotchas (verify against the current API reference):** hyperlinks inside the .docx can break document creation; and placeholder names must match the merge-data keys exactly or they render unresolved (`{{client_name}}` left literal in the PDF). Test each template with sample booking data before it's approved for live use.

---

## Part E — Generate and send a contract (the API sequence)

Triggered by **Generate** then **Send** on the Booking Contract panel (spec §11). The CRM backend does:

1. **Build the data payload** from the booking (spec §08). Block generation if any required field is missing.
2. **Create the envelope as a draft** from the template, with `status: "created"` (not `"sent"`), recipients = client (+ co-signer), and the `notification` object for reminders/expiry (Part H).
3. **Get the Doc Gen fields:** `GET …/envelopes/{envelopeId}/docGenFormFields` → returns the field list and the `documentId`.
4. **Populate the fields:** `PUT …/envelopes/{envelopeId}/docGenFormFields` with a `docGenFormFields` array — each entry has the `documentId` and a `docGenFormFieldList` of `{name, value}` from the booking data.
5. **File the draft:** download the generated PDF and save it under the booking (spec §09), status → **Draft**.
6. **Send:** when the user clicks Send, `PUT …/envelopes/{envelopeId}` with `status: "sent"`. DocuSign emails the signer. Status → **Sent for Signature**.

```
Booking → payload → create envelope (created) → get docGenFormFields
       → put field values → [file draft PDF]  → put status=sent → DocuSign emails client
```

For **embedded signing** (tablet at the venue), after sending, call `createRecipientView` to get a signing URL and open it in the CRM.

---

## Part F — Connect webhook (status back to the CRM)

This is what updates the booking status and files the signed copy automatically (spec §04, §07).

### F1. Expose a listener
Build a public HTTPS endpoint in the CRM, e.g. `POST /api/contracts/docusign`. It must be reachable from DocuSign (not localhost in production).

### F2. Configure Connect
**Either** account-wide **or** per-envelope:

- **Account-wide:** **Settings → Connect → Add Configuration → Custom**. Set the **URL to publish to** (your listener), format **JSON (REST)**, and select trigger events:
  - Envelope: **Sent, Delivered, Completed, Declined, Voided**
  - Recipient: **Completed** (needed to derive **Partially Signed**)
- **Per-envelope:** add an `eventNotification` object when creating the envelope (Part E step 2). This avoids the 100-configuration account limit and scopes events to contracts only.

### F3. Enable and verify HMAC
1. In Connect settings, add a **Connect Key** (HMAC secret). Store it as `DOCUSIGN_HMAC_KEY` (Part C).
2. On every incoming POST, the listener **verifies the `X-DocuSign-Signature-1` header** (HMAC-SHA256 of the raw body with your key). Reject anything that doesn't match — this stops forged status updates.

### F4. Handle events (idempotent)
Key every event by **envelope id** and upsert, so a replayed or out-of-order webhook never double-files or double-counts (spec §07):

| Event received | CRM action |
|---|---|
| Envelope `sent` / `delivered` | Status → Sent for Signature |
| Recipient `completed` (not all) | Status → Partially Signed; record who signed |
| Envelope `completed` | Status → Signed; **trigger Part G** |
| Envelope `declined` | Status → Declined (reason); notify owner |
| Envelope `voided` | Status → Expired (if expiry) or Voided; notify owner |

### F5. Reconcile job (backstop)
A scheduled job polls `GET …/envelopes?from_date=…` (or per-envelope status) for any contract stuck "Sent"/"Partially Signed" past a threshold, and self-heals a missed webhook.

---

## Part G — File the signed contract

On the envelope `completed` event:
1. **Download the combined document:** `GET …/envelopes/{envelopeId}/documents/combined` → one PDF containing **all signed documents plus the Certificate of Completion** (the audit record).
2. **File it** under the booking in the same structure as the draft (spec §09), named to convention, status → **Signed**. Signed PDFs are immutable — never overwrite.
3. **Notify** the owner and Finance via the CRM's existing follow-up channel (spec §10).

The filed PDF — not DocuSign — is the retained record. Retrieval never depends on DocuSign being reachable.

---

## Part H — Reminders, expiry and follow-ups

Set the envelope `notification` object at create time (spec §10). Recommended defaults (confirm spec §15 D4):

```json
"notification": {
  "useAccountDefaults": "false",
  "reminders":  { "reminderEnabled": "true",  "reminderDelay": "3", "reminderFrequency": "3" },
  "expirations":{ "expireEnabled": "true", "expireAfter": "21", "expireWarn": "3" }
}
```
= first reminder after 3 days, repeat every 3; expire after 21 days, warn 3 days before. (Default without this: 120-day expiry, no reminders.) Team-side notifications are driven by the Connect events in Part F, not by DocuSign. SMS/WhatsApp reminders need DocuSign IAM Maestro or a CRM-side SMS step.

---

## Part I — Go live (promote to production)

Only after the full flow works in the sandbox:

1. **Pass Go-Live / API review.** DocuSign requires a number of successful API calls in demo (historically ~20) before an integration key can be promoted. In the developer console: **Apps and Keys → Go Live**, and follow the checklist.
2. **Promote the Integration Key** to production (same key GUID moves to prod) and/or create it in the **production** account.
3. **Create/obtain the production DocuSign account** and the **Doc Gen add-on** (paid — spec §15 D5). Confirm Doc Gen is enabled on the prod plan.
4. **Re-grant consent** on production (`account.docusign.com`) — sandbox consent doesn't carry over.
5. **Swap the config** (Part C): `DOCUSIGN_AUTH_SERVER` → `account.docusign.com`, `DOCUSIGN_BASE_PATH` → the production base URI from `userinfo`, production Account ID, and (if different) the production RSA key.
6. **Re-point Connect** to the production listener URL and set a production HMAC key.
7. **Pilot** on a few real bookings with a human review gate (spec §14 phase 7, §15 D6).

---

## Reference — endpoints

| Purpose | Demo | Production |
|---|---|---|
| OAuth auth / consent | `account-d.docusign.com/oauth/auth` | `account.docusign.com/oauth/auth` |
| OAuth token | `account-d.docusign.com/oauth/token` | `account.docusign.com/oauth/token` |
| User info (→ base URI, account id) | `account-d.docusign.com/oauth/userinfo` | `account.docusign.com/oauth/userinfo` |
| eSignature REST base | `https://demo.docusign.net/restapi` | `{base_uri}/restapi` (from userinfo) |
| eSignature calls | `…/restapi/v2.1/accounts/{accountId}/…` | same |

Scopes for JWT: **`signature impersonation`**. Access tokens last ~1 hour.

---

## Setup checklist — done when

- [ ] Developer account created; app type **API Integration**
- [ ] Integration Key created; auth type **JWT**
- [ ] RSA keypair generated; private key stored as a secret
- [ ] Dedicated **system user** created and impersonated (not a person)
- [ ] Consent granted (admin or per-user); token + `userinfo` call succeed
- [ ] Five values stored in the CRM secret store (Part C)
- [ ] At least one Doc Gen template built, flagged, field-verified, legal-approved
- [ ] CRM can generate → file draft → send a test contract
- [ ] Connect configured; **HMAC verified**; events update status correctly
- [ ] Signed `completed` → combined PDF + certificate filed under the booking
- [ ] Reminders + expiry fire; team notifications fire
- [ ] Replayed/out-of-order webhook is a no-op; reconcile job heals a dropped event
- [ ] Go-Live passed; production config swapped in; pilot on real bookings

---

## Troubleshooting — common gotchas

| Symptom | Cause / fix |
|---|---|
| `consent_required` on first token call | Consent not granted. Open the consent URL as the impersonated user (B1), or grant admin consent. |
| `invalid_grant` | Wrong `aud` (demo vs prod host), expired/clock-skewed JWT, or wrong User ID/key. Use the SDK's JWT helper. |
| Doc Gen fields come back empty | Template document not flagged `isDocGenDocument`, or template created via the UI button. Create via API JSON upload. |
| `{{placeholder}}` appears literally in the PDF | Merge-data key doesn't match the placeholder name exactly, or the field value wasn't PUT before send. |
| Document creation errors on a template | Hyperlinks in the .docx can break Doc Gen — remove or verify them. |
| Webhook never arrives | Listener not publicly reachable (localhost), HTTPS/cert issue, or events not selected in Connect. |
| Forged/duplicate status updates | HMAC not verified, or events not keyed by envelope id. Enforce both (F3, F4). |

> Request bodies and field names shift between API versions — verify each call against the **current DocuSign eSignature REST API reference** before relying on it. This guide gives the sequence and the pieces; the reference gives the exact JSON.
