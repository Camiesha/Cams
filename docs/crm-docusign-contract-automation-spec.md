# CRM › Bookings › Contract Automation with DocuSign

**Status:** For review · **Date:** 12 Oct 2026 · **Applies to:** Crown Prince Event Hall, Alvin Studio
**Companion:** published artifact "Contract Automation" — a business-to-IT proposal (problem, workflow, status model, where AI fits, architecture, cost, decisions). This file is the full technical source of truth; the artifact carries the same requirements for stakeholders.
**Related:** `crm-lead-source-spec.md` (same CRM, same booking records), `events-venue-marketing-playbook.md` §6 Close (the booking is the end of the funnel this automates).

**Read by role**

| Audience | Sections |
|---|---|
| Business Owner | 01 · 05 · 13 · 15 |
| CRM Admin | 03 · 04 · 09 · 11 · 12 |
| Product Manager | 01 · 02 · 03 · 14 · 15 |
| Developer | 06 · 07 · 08 · 10 · 11 |
| Finance / Audit | 01 · 04 · 13 · 16 |
| QA | 16 · 17 |

---

## 01 Executive summary

| Problem | Solution | Outcome |
|---|---|---|
| Contracts are made by hand. A booking is confirmed in the CRM, then someone opens a Word template, retypes the client name, dates, venue, guest count and price, exports a PDF, emails it, waits, chases the client by hand, downloads the signed copy, and uploads it back to the booking. Every step is manual, slow, and easy to get wrong — a wrong figure on a signed contract is a real liability. | Integrate **DocuSign** directly into the Booking record. The CRM **generates** the contract from the booking's own data and the approved template, **sends** it for e-signature, **tracks** its status, **files** both the sent and the signed copy under the booking automatically, and **reminds** clients who have not signed — with no manual generate, send, download or upload. | Every booking produces a correct contract in seconds, sent the same minute it is approved. The team sees status at a glance. The signed PDF and its Certificate of Completion are filed under the booking for retrieval and audit. Nobody retypes a client's details onto a legal document again. |

| What changes | What does not change |
|---|---|
| A **Contract** panel on every Booking record: Generate, Send, track status, view/download | The Booking record itself, its fields, and where bookings live |
| Contracts are **generated from booking data** into the approved template, not retyped | Your **approved contract templates** and their legal wording — attorney-approved, unchanged |
| Documents are **filed automatically** under the booking, in the same storage structure used today | The Booking Documents area's folder/structure conventions |
| A **contract status** (Draft → Sent → Partially Signed → Signed; or Expired/Declined/Voided) on the booking | Pricing stays custom-quote; the quote still comes before the contract |
| Automatic **reminders and expiry** per contract; team notifications on signature | Who may approve a booking and who may send a contract (your existing roles) |

**One rule above all:** the system assembles contracts from **approved templates and approved clauses only**. AI and automation fill in and select; they do not invent legal language. Every template and every optional clause is attorney-reviewed before it is available to automation (see §05, §15 D1).

---

## 02 Current → Proposed

**Current.** Booking confirmed → staff opens the Word/PDF template → retypes client name, event date(s), venue, hours, guest count, deposit and balance, add-ons → exports PDF → attaches to an email → sends → watches inbox → manually emails/texts reminders → client signs and emails back → staff downloads → renames → uploads to the booking folder. Typically 15–30 minutes of work per contract, spread over days, with retyping as the main error source.

| To issue and file a contract today | After |
|---|---|
| Open template · retype ~10 fields · export · attach · email · chase by hand · download reply · rename · upload. Many steps, several days, manual follow-up. | On the booking: **Generate** (data merged automatically) → review → **Send**. Reminders are automatic. Signed PDF + certificate file themselves under the booking. Status updates itself. |

**Proposed.** The Booking record gains a **Contract** panel. One click generates the contract from the booking's data into the approved template; the generated PDF is filed under the booking immediately (status **Draft**). Send routes it to the client (and co-signer, if any) for e-signature (status **Sent for Signature**). DocuSign handles delivery, reminders and expiry. As recipients sign, status moves to **Partially Signed** then **Signed**; the completed PDF and its Certificate of Completion are filed under the booking automatically. The team is notified. Nothing is downloaded or uploaded by hand.

---

## 03 The automated workflow

Six stages, each mapped to who/what does it and to the DocuSign capability behind it (detailed in §06).

```
BOOKING (confirmed, quote accepted)
   │  booking data: client, venue, dates, hours, guests, deposit, balance, add-ons
   ▼
1. GENERATE  ── CRM merges booking data into the approved template ──▶ draft PDF
   │            (DocuSign Doc Gen for eSignature, or server-side merge)
   ▼
   FILE DRAFT  ── draft PDF saved under the booking (status: Draft) ──┐
   ▼                                                                   │
2. SEND  ── envelope created + sent to client (+ co-signer) ──────────┤  CRM Booking
   │         reminders + expiry attached (status: Sent for Signature) │  Documents
   ▼                                                                   │  (same
3. SIGN  ── client signs; co-signer signs                             │  structure
   │         (status: Partially Signed → Signed)                      │  as today)
   ▼                                                                   │
4. FILE SIGNED ── completed PDF + Certificate of Completion saved ────┘
   │              under the booking automatically (status: Signed)
   ▼
5. TRACK  ── status visible on the booking and in a Contracts list
   │         DocuSign Connect webhook updates the CRM in real time
   ▼
6. REMIND / FOLLOW-UP ── automatic reminders while unsigned;
                          team notified on sign / decline / expiry
```

**Requirement → stage map (the six asks in the request):**

| # | Requirement | Stage | Section |
|---|---|---|---|
| R1 | Automated contract generation from booking data + approved templates | 1 Generate | §05, §06, §08 |
| R2 | E-signature integration (auto-send, minimal manual work) | 2 Send / 3 Sign | §06, §07 |
| R3 | CRM document storage — draft filed under the booking, same structure | File draft | §09 |
| R4 | Signed-contract storage — completed version filed under the booking | 4 File signed | §09 |
| R5 | Status and tracking (Draft, Sent, Partially Signed, Signed, Expired) | 5 Track | §04 |
| R6 | Notifications and follow-up reminders for unsigned contracts | 6 Remind | §10 |

---

## 04 Contract status model

The booking carries one **Contract status**. It is driven by DocuSign envelope and recipient events, not set by hand.

| CRM status | Meaning | Driven by (DocuSign) | Booking shows |
|---|---|---|---|
| **No contract** | Nothing generated yet | — | "Generate contract" |
| **Draft** | Generated and filed, not yet sent | Envelope `created` (not sent) | Review · Send · Regenerate |
| **Sent for Signature** | With the client; awaiting signatures | Envelope `sent` / `delivered` | Sent date · recipients · Resend · Void |
| **Partially Signed** | At least one, not all, required parties signed | Recipient `completed` events while envelope not yet `completed` | Who signed, who is pending |
| **Signed** | All required parties signed | Envelope `completed` | Signed date · download signed PDF + certificate |
| **Declined** | A signer declined | Envelope `declined` | Reason · regenerate / contact client |
| **Expired** | Not signed before expiry; auto-voided | Envelope `voided` (expiration) | Expired date · regenerate & resend |
| **Voided** | Cancelled by the team | Envelope `voided` (by sender) | Who/when/why · regenerate |

> **Note on "Partially Signed".** DocuSign's *envelope* status moves from `sent` straight to `completed`; it has no single "partially signed" value. The CRM derives **Partially Signed** from **recipient-level** events (`recipient completed` for some but not all required signers). This matters only when a contract has two or more required signers (e.g. client + co-host, or two venue DBAs). For a single-signer contract the status goes Sent → Signed.

**Status is read-only in the CRM** — it reflects DocuSign, the system of record for who signed and when. The only human status action is **Void** (cancel a sent contract), which calls DocuSign to void the envelope and files the reason.

---

## 05 Where AI and automation fit

The request asks specifically for **AI and automation**. These are two different things and the distinction protects you legally. Each stage below says which it is.

| Stage | Automation (deterministic, no AI) | AI (model-assisted) | Guardrail |
|---|---|---|---|
| Choose the template | Rule: event type + venue → approved template (e.g. wedding vs corporate vs quinceañera; Crown Prince vs Alvin) | Optional: AI *suggests* the template when the event type is ambiguous; a person confirms | Only approved templates are selectable. AI never writes a template. |
| Fill the contract | Merge booking fields into the template's named placeholders | — | A missing required field blocks generation; it is never guessed or AI-filled |
| Optional clauses | Rule: include/exclude an approved clause by booking data (e.g. "alcohol service" add-on → insurance clause) | Optional: AI flags when a booking's notes suggest a clause may be needed, for a person to add | Clauses are a fixed approved library; AI proposes from that library only, never free text |
| Review before send | Required human review gate on first use / high-value / non-standard | Optional: AI "diff" summary of what this contract changed vs the standard template, to speed review | A person clicks Send. AI output is advisory, shown to the reviewer |
| After signing | Auto-file; auto-update status; auto-notify | Optional (IAM Navigator / Lexion): extract key terms (dates, amounts, cancellation terms) for search and reporting | Extraction is read-only metadata; it never alters the signed PDF |

**The honest position for a venue business:** the heavy lifting here is **automation**, not AI — merging known booking data into an attorney-approved template and sending it. That is reliable, auditable, and cheap. **AI is an accelerator on top**: template suggestion when ambiguous, a review summary, and (if you license DocuSign IAM) term extraction and search across all signed contracts. Do **not** let a model draft binding legal language from scratch. This keeps the system defensible if a contract is ever disputed — every word came from a template your attorney approved.

---

## 06 DocuSign capability map

Each job maps to a specific DocuSign product or API. This tells IT exactly what to license and build.

| Job (this spec) | DocuSign capability | Notes |
|---|---|---|
| Generate contract from booking data | **Document Generation for eSignature (Doc Gen)** | Merges a data payload into a `.docx` template with named fields and conditional clauses; sent via the eSignature REST API. Production use needs a paid add-on. Alternative: merge server-side in the CRM and upload the finished PDF to a plain envelope. |
| Send for e-signature | **eSignature REST API** — Envelopes: create + send | One envelope per contract; recipients = client (+ co-signer). Supports routing order for multi-party signing. |
| Sign inside the CRM (optional) | **Embedded signing (recipient view)** | For a client signing on a tablet at the venue during a tour; otherwise email signing is default. |
| Many contracts at once (optional) | **Bulk Send** | Rarely needed for a venue; one-off per booking is the norm. |
| Status back to the CRM in real time | **DocuSign Connect** (webhook) | HTTP POST (JSON) on envelope + recipient events: `sent`, `delivered`, `recipient-completed`, `completed`, `declined`, `voided`. Verify the `X-DocuSign-Signature` HMAC header. Attach per-envelope (`eventNotification`) or configure account-wide. |
| Reminders + expiry | **Envelope `notification` object** | Per-envelope `reminderEnabled/reminderDelay/reminderFrequency` and `expireEnabled/expireAfter/expireWarn`. Default is 120-day expiry, no reminders, unless set. |
| Download the final document | **Envelopes: get document = `combined`** | Returns one PDF of all signed documents **plus the Certificate of Completion**. `archive` returns a ZIP. This is what the CRM files under the booking. |
| AI term extraction + search across contracts (optional) | **DocuSign IAM — Navigator** (repository + AI; Lexion) | Higher tier. Stores and analyses all agreements, extracts terms, enables search/reporting. Consider only if you want analytics across the whole contract book, not for the core workflow. |
| No-code workflow / SMS·WhatsApp reminders (optional) | **DocuSign IAM — Maestro** | No-code workflow builder with multi-channel (SMS/WhatsApp) delivery. An alternative to building the webhook glue yourself, at a higher licence tier. |

**Recommended starting build:** eSignature REST API + Doc Gen + Connect + envelope notifications. That delivers all six requirements. IAM (Navigator/Maestro) is an optional upgrade for AI analytics and no-code workflows — decide at §15 D5.

---

## 07 Integration architecture

```
            CRM (Bookings)                         DocuSign
  ┌───────────────────────────────┐      ┌──────────────────────────┐
  │ Booking record                │      │                          │
  │  └ Contract panel             │      │                          │
  │       │ Generate              │      │                          │
  │       ▼                       │      │                          │
  │  build data payload ──────────┼─────▶│ Doc Gen: merge into       │
  │       │                       │      │ approved .docx template   │
  │  file draft PDF under booking │◀─────┼── generated document      │
  │       │ Send                  │      │                          │
  │       ▼                       │      │ Envelopes: create+send    │
  │  create envelope ─────────────┼─────▶│  recipients, routing,     │
  │   + notification (reminders,  │      │  reminders, expiry        │
  │     expiry) + eventNotification│      │       │                  │
  │                               │      │       ▼ email to client   │
  │  webhook listener  ◀──────────┼──────┼── Connect POST (JSON,     │
  │   /api/contracts/docusign     │      │   HMAC-signed) on each    │
  │       │ verify HMAC           │      │   envelope/recipient event│
  │       │ update status         │      │                          │
  │       │ on completed:         │      │                          │
  │       ▼  GET document=combined┼─────▶│ Envelopes: get combined   │
  │  file signed PDF + cert ◀─────┼──────┼── signed PDF + certificate│
  │  notify team                  │      │                          │
  └───────────────────────────────┘      └──────────────────────────┘
```

**Auth:** OAuth (JWT grant) for server-to-server calls from the CRM to DocuSign; the integration uses a dedicated DocuSign system user, not a person's login (so it keeps working when staff change).

**Idempotency:** every Connect event carries the envelope id and event; the listener upserts by envelope id so a replayed or out-of-order webhook never double-files a document or double-counts a status. On `completed`, fetch the combined document once and file it if not already present.

**Resilience:** if a webhook is missed, a scheduled reconcile job polls envelope status for any contract still "Sent"/"Partially Signed" past a threshold and self-heals. Connect also supports its own retry; the reconcile job is the backstop.

---

## 08 Booking → contract data payload

Generation reads the booking's existing fields. No new client-facing data entry.

| Template field | Booking source | Required | If missing |
|---|---|---|---|
| Client name(s) | Booking client | ✓ | Block generate |
| Co-signer (optional) | Booking secondary contact | — | Single-signer contract |
| Venue | Booking venue (Crown Prince / Alvin) | ✓ | Block generate |
| Event type | Booking event type | ✓ | Block generate (drives template) |
| Event date(s) | Booking date(s) | ✓ | Block generate |
| Start / end time | Booking hours | ✓ | Block generate |
| Guest count | Booking guests | ✓ | Block generate |
| Total / deposit / balance | Booking quote (accepted) | ✓ | Block generate |
| Add-ons (e.g. alcohol service) | Booking add-ons | — | Omit related optional clause |
| Payment schedule / due dates | Booking terms | ✓ | Block generate |
| Contract date | System date at generate | ✓ | — |

**Rule:** generation is only possible once the booking has an **accepted quote** and the required fields above are present. The Generate button is disabled, with a checklist of what is missing, until then. This prevents a contract ever carrying a blank or placeholder figure — the accountant's first concern.

```json
POST  (CRM → DocuSign Doc Gen → Envelope)
{
  "templateKey": "crown_prince__wedding__v4",
  "mergeData": {
    "client_name": "…", "cosigner_name": null,
    "venue": "Crown Prince Event Hall",
    "event_type": "Wedding",
    "event_date": "2026-11-21",
    "start_time": "16:00", "end_time": "23:00",
    "guest_count": 180,
    "total": 9500.00, "deposit": 2000.00, "balance": 7500.00,
    "payment_schedule": [ { "due": "2026-10-20", "amount": 2000.00 }, … ],
    "addons": ["alcohol_service"],
    "contract_date": "2026-10-12"
  },
  "clauses": { "alcohol_insurance": true },
  "booking_id": "BK-10482"
}
```

---

## 09 Document storage under the booking

Documents file themselves into the **same Booking Documents structure used today** — this is requirement R3/R4 and must not introduce a parallel store.

| Moment | File | Named | Folder |
|---|---|---|---|
| On Generate | Draft contract PDF | `Contract – BK-10482 – Draft – 2026-10-12.pdf` | Booking › Documents › Contracts |
| On Send | (envelope reference, no new file) | status only | — |
| On Signed | Completed signed PDF (combined) | `Contract – BK-10482 – Signed – 2026-11-02.pdf` | Booking › Documents › Contracts |
| On Signed | Certificate of Completion | `Contract – BK-10482 – Certificate – 2026-11-02.pdf` | Booking › Documents › Contracts |

Rules:
- **Mirror current conventions.** Whatever folder/label/permission the Booking Documents area uses today for manually uploaded contracts is reused exactly; contracts are not special-cased into a new location. (Confirm the current structure at §15 D3.)
- **Supersede, don't duplicate.** Regenerating a draft replaces the prior *draft*; signed documents are immutable and never overwritten.
- **One source of truth.** The DocuSign envelope id is stored on the booking so the team can open the live envelope from the CRM, but the *filed PDFs are the retained record* — retrieval never depends on DocuSign being reachable.
- **Retention.** Signed PDF + certificate are retained per the business's document-retention policy, independent of the DocuSign account (so cancelling DocuSign later never loses signed contracts).

---

## 10 Notifications, reminders and follow-ups

**To the client (automatic, via DocuSign):**

| Trigger | Action | Setting |
|---|---|---|
| Contract sent | DocuSign signing email | Envelope send |
| Unsigned after N days | Reminder email | `reminderDelay` = first reminder after N days; `reminderFrequency` = every M days thereafter |
| Approaching expiry | Expiry warning | `expireWarn` days before `expireAfter` |
| Expired | Envelope voids; CRM flags for regenerate/resend | `expireEnabled`, `expireAfter` |

Recommended defaults (confirm at §15 D4): first reminder after **3 days**, repeat every **3 days**, expire after **21 days**, warn **3 days** before. Optional SMS/WhatsApp reminders require DocuSign IAM Maestro (§06) or a CRM-side SMS step.

**To the team (automatic, in the CRM / existing follow-up channel):**

| Event | Notify | Why |
|---|---|---|
| Client opened but did not sign (N days) | Assigned owner | Prompt a personal nudge call |
| Partially Signed | Assigned owner | One party done; chase the other |
| Signed | Assigned owner + Finance | Collect deposit; update booking |
| Declined | Assigned owner | Contact client, resolve, regenerate |
| Expired / Voided | Assigned owner | Decide to resend or let go |

These reuse the CRM's existing follow-up/notification mechanism (see `crm-lead-source-spec` context and the Follow-Up Status work) rather than inventing a new one.

---

## 11 CRM UI — the Contract panel

On every Booking record, a **Contract** panel:

| State | Shows | Actions |
|---|---|---|
| No contract | Readiness checklist (required fields present?) | **Generate** (enabled only when ready) |
| Draft | Draft PDF preview · template used · generated date · AI change-summary (if enabled) | Review · **Send** · Regenerate · Delete draft |
| Sent for Signature | Recipients + their status · sent date · last reminder · expiry date | Resend reminder now · Void · Open in DocuSign |
| Partially Signed | Who signed (with time) · who is pending | Resend to pending · Void |
| Signed | Signed PDF + Certificate (download) · signed date | Download · Open filed documents |
| Declined / Expired / Voided | Reason · date | Regenerate & resend |

A **Contracts** list view (across bookings) with columns: Booking · Client · Venue · Event date · Contract status · Sent · Signed · Owner — filterable by status (e.g. everything "Sent for Signature" older than 7 days), so the team works outstanding contracts without opening each booking. This mirrors the "surface it in the list" principle from the Lead Source spec.

---

## 12 Permissions

| Role | Generate | Send | Void | Download signed | Manage templates/rules |
|---|---|---|---|---|---|
| Admin | ✓ | ✓ | ✓ | ✓ | ✓ |
| Manager | ✓ | ✓ | ✓ | ✓ | — |
| Advisor (owns booking) | ✓ | ✓ own bookings | ✓ own bookings | ✓ | — |
| Finance / Read-only | — | — | — | ✓ | — |
| Integration (system user) | generate + send on action only | — | — | file only | — |

Template and clause library management (adding/retiring approved templates) is Admin-only and gated behind legal sign-off (§15 D1).

---

## 13 Security, compliance and audit

Written for the Finance/audit reader, since a signed contract is a financial and legal record.

- **Legal validity.** DocuSign e-signatures are valid under the US ESIGN Act and state UETA. The **Certificate of Completion** records each signer's identity, email, IP, and timestamps — it is the evidence of a valid signature and is filed with every signed contract (§09).
- **Tamper-evidence.** The completed PDF is sealed by DocuSign; the certificate detects post-signature alteration. The CRM files the sealed copy, never a re-saved version.
- **Audit trail.** Every contract action (generated by whom, sent by whom, status changes, voids with reason) is logged on the booking, matching the activity-log pattern already used for lead-source changes.
- **Data retention independence.** Signed PDFs + certificates live in the CRM's own storage, so the record survives even if the DocuSign subscription lapses (§09).
- **Webhook integrity.** The Connect listener verifies the `X-DocuSign-Signature` HMAC on every call and rejects unsigned/forged posts.
- **Access.** OAuth JWT with a dedicated system user; secrets in the CRM's secret store, not in code; least-privilege DocuSign permissions.
- **PII.** Client details flow CRM → DocuSign only as needed to produce and route the contract; no payment-card data is ever placed in a contract document.

---

## 14 Build plan

| # | Phase | Work | Owner | Exit check |
|---|---|---|---|---|
| 1 | Prepare | Answer §15 decisions. Confirm current Booking Documents structure (D3). Get attorney sign-off on templates + clause library (D1). Choose DocuSign plan incl. Doc Gen add-on (D5). Provision DocuSign account, system user, JWT app. | Owner · Admin · Finance · Legal | Templates approved; plan purchased; sandbox access |
| 2 | Templates | Convert approved contracts to Doc Gen `.docx` templates with named merge fields + conditional clauses. Map each (event type × venue) to a template key. | Admin · Developer | Each template renders correctly from sample booking data in sandbox |
| 3 | Generate | Booking → data payload; readiness checklist; Doc Gen call; file draft under booking; status Draft. | Developer | Draft PDF for each template matches booking data exactly; missing-field block works |
| 4 | Send | Envelope create+send; recipients + routing; `notification` (reminders/expiry); `eventNotification` (Connect). | Developer | Test contract arrives; reminders + expiry visible on the envelope |
| 5 | Track + file | Connect listener: HMAC verify, idempotent status updates, derive Partially Signed, fetch combined doc on completed, file signed PDF + certificate. Reconcile job. | Developer | Status and filed docs match DocuSign for every event; replayed webhook is a no-op |
| 6 | UI | Contract panel per booking; Contracts list view; team notifications wired to existing follow-up channel. | Developer | Team can run the full flow without leaving the CRM |
| 7 | Pilot | Run live on a small set of real bookings with a human review gate on every send; compare filed docs to DocuSign; verify audit trail + certificate filing. | QA · Finance · Owner | Acceptance criteria (§16) pass; one full cycle incl. a two-signer and an expiry |

> 🔒 **Control check (for Finance):** for each piloted booking, the figures on the generated contract must equal the booking's accepted quote exactly, and the filed signed PDF must be byte-identical to DocuSign's combined download. No contract is ever sent with a field the booking did not supply.

---

## 15 Decisions required

| # | Decision | Recommendation | Owner | Blocks |
|---|---|---|---|---|
| D1 | Which contracts/templates, and who signs off their wording for automation? | Attorney approves each template + the optional-clause library before it is available to automation; no AI-authored legal text | Owner · Legal | Phase 2 |
| D2 | Single-signer or multi-signer contracts (client + co-host; two venue DBAs)? | Support both; routing order per template. Note Alvin Studio is a DBA of Crown Prince Hall — confirm the correct signing entity per venue | Owner · Legal | Phase 2 · 4 |
| D3 | Exact current Booking Documents structure (folder, naming, permissions) to mirror? | Admin documents it in phase 1; contracts file into it unchanged | Admin | Phase 3 · 5 |
| D4 | Reminder cadence and expiry window? | First reminder 3 days, repeat every 3, expire 21 days, warn 3 before — confirm | Owner | Phase 4 |
| D5 | DocuSign plan: core (eSignature + Doc Gen + Connect) now, or full IAM (Navigator/Maestro AI) later? | Start core — it meets all six requirements. Revisit IAM once there is a contract book worth analysing | Owner · Finance | Phase 1 |
| D6 | Human review gate: every contract, or only first-use / high-value / non-standard? | Every contract during pilot; then relax to non-standard + above a value threshold | Owner | Phase 7 |
| D7 | When exactly is a contract generated — on booking confirmed, on quote accepted, or on demand? | On demand from the Contract panel once the quote is accepted (keeps a person in the loop) | Owner · PM | Phase 3 |

---

## 16 Acceptance criteria

| | # | Criterion | Verified by |
|---|---|---|---|
| ☐ | AC1 | Contract generated from booking data into the approved template, no retyping | T01–T03 |
| ☐ | AC2 | Required fields enforced; generation blocked (never guessed) when data is missing | T04 |
| ☐ | AC3 | Contract sent for e-signature from the CRM in one action | T05 |
| ☐ | AC4 | Draft filed under the booking on generate, in the existing structure | T06 |
| ☐ | AC5 | Signed PDF + Certificate of Completion filed under the booking on completion | T07 |
| ☐ | AC6 | Status reflects DocuSign: Draft · Sent · Partially Signed · Signed · Declined · Expired · Voided | T08–T11 |
| ☐ | AC7 | Reminders sent automatically; expiry voids and flags the booking | T12, T13 |
| ☐ | AC8 | Team notified on sign / partial / decline / expiry via the existing follow-up channel | T14 |
| ☐ | AC9 | Figures on the contract equal the accepted quote exactly | T01, pilot control check |
| ☐ | AC10 | Replayed/out-of-order webhook never double-files or mis-counts; missed event self-heals | T15 |
| ☐ | AC11 | Webhook HMAC verified; forged post rejected | T16 |

---

## 17 Test matrix

| ID | Scenario | Steps | Expected | AC |
|---|---|---|---|---|
| T01 | Generate, single signer | Confirmed booking with accepted quote → Generate | Draft PDF; all fields = booking; figures = quote; status Draft | 1, 9 |
| T02 | Template selection | Generate for a wedding and a corporate booking at each venue | Correct template per event type × venue | 1 |
| T03 | Optional clause | Booking with alcohol-service add-on → Generate | Insurance clause included; without add-on, excluded | 1 |
| T04 | Missing data | Remove guest count → Generate | Blocked with checklist; nothing sent | 2 |
| T05 | Send | Draft → Send | Client receives signing email; status Sent for Signature | 3 |
| T06 | Draft filed | After Generate | Draft PDF under Booking › Documents › Contracts, named per convention | 4 |
| T07 | Signed filed | Complete signing | Combined signed PDF + certificate filed; status Signed | 5 |
| T08 | Partial signing | Two required signers; first signs only | Status Partially Signed; shows who is pending | 6 |
| T09 | Decline | Signer declines | Status Declined with reason; team notified | 6, 8 |
| T10 | Void | Team voids a sent contract | Envelope voided; status Voided with reason | 6 |
| T11 | Status realtime | Sign in DocuSign; watch the booking | CRM status updates without refresh/manual action | 6 |
| T12 | Reminder | Leave a sent contract unsigned past the reminder delay | Reminder email sent automatically | 7 |
| T13 | Expiry | Leave unsigned past expiry | Envelope voids; status Expired; regenerate offered | 7 |
| T14 | Team notify | Each of sign / partial / decline / expiry | Owner (and Finance on sign) notified via existing channel | 8 |
| T15 | Idempotency | Replay a completed webhook; deliver events out of order | No duplicate file; status correct; reconcile job heals a dropped event | 10 |
| T16 | Webhook security | POST to the listener with a bad/absent HMAC | Rejected; no state change | 11 |

---

**Implementation summary:** BOOKING → GENERATE (approved template + booking data) → FILE DRAFT → SEND (e-signature) → SIGN → FILE SIGNED (PDF + certificate) → TRACK (status) → REMIND. Automation does the generating, sending, filing and chasing; AI assists with template choice, review and analytics; attorney-approved templates guarantee every word is defensible. All six requirements met on the core DocuSign plan; IAM is an optional AI-analytics upgrade.
