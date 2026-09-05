# CRM Lead Source — Automatic Detection with Manual Override

**Applies to:** CRM › Leads (Crown Prince Event Hall, Alvin Studio)
**Status:** Specification for review · 2026-09-05
**Companion:** `events-venue-marketing-playbook.md` §5 (CRM), §7 (Ads → GA4 → CRM source field), §14 Gate 1

> **Why this matters to the numbers.** The Lead Source field is the join key between spend and revenue. Every cost-per-lead, cost-per-booking and channel ROI figure in the playbook depends on each lead carrying the channel it came from. Today the Leads list has no such column, so none of those figures can be produced.

---

## 1. Existing state

Recorded from the Leads list screenshot supplied 2026-09-05. If the PNG is added to the repo at `docs/images/leads-list-existing.png` it will render here.

![Existing Leads list](images/leads-list-existing.png)

**What the screen shows today**

| Element | Current state |
|---|---|
| Location | CRM › Leads |
| Subtitle | "Leads from 2 web apps + phone/text · 1h response target · new leads are shared out automatically" |
| Actions | **+ New Lead**, **Export ▾**, view toggle **Pipeline / List / Health** |
| Filters | Search (code, name, contact, event type) · All statuses · All advisors · SLA overdue |
| Columns | Name · Venue · Contact · Event Date · **Captured** (default sort, descending) · Guests · Status · Assigned · Follow-up |
| Lead Source | **Not present** — no column, no filter, no export field |

**What this tells us about intake**

- Leads already arrive through at least four entry points: two website apps (one per venue), phone, and text. Manual creation exists via **+ New Lead**.
- "Shared out automatically" means an assignment routine already runs on new leads. Source detection should run in that same intake step, before assignment, so the source is present from the first second.
- "Captured" is already a system-set timestamp. Lead Source should behave the same way: set by the system on arrival, visible in the list, and editable when the system could not tell.

---

## 2. Required behaviour

**Preferred flow**

```
Inquiry received → CRM identifies entry point → Lead Source set automatically → shown in Leads list
```

**Fallback flow**

```
Inquiry received → entry point cannot be identified → Lead Source = Unknown / Not Set → user selects the correct source
```

**Rules**

1. Set the Lead Source automatically whenever the entry point is known with certainty.
2. When it is not known with certainty, store **Unknown / Not Set**. Never guess.
3. Authorized users can edit the Lead Source at any time.
4. A manually set or corrected Lead Source is never overwritten by automation.
5. New Lead Source options are added as data, not as schema changes.
6. Detection runs inside the existing intake path and does not alter assignment, SLA timers, or follow-up automation.

**Initial source list**

| Key | Display label | Typical entry point |
|---|---|---|
| `website` | Website | Inquiry form on either venue web app |
| `facebook` | Facebook | Meta lead form, Messenger, or Facebook notification email |
| `yelp` | Yelp | Yelp inquiry (delivered by Yelp notification email) |
| `phone_call` | Phone Call | Inbound call logged by the phone system or by an advisor |
| `sms` | SMS | Inbound text to the venue number |
| `email` | Email | Direct email to the inquiries mailbox that matches no other rule |
| `tagvenue` | Tagvenue | Tagvenue inquiry (delivered by Tagvenue notification email) |
| `zola` | Zola | Zola inquiry (delivered by Zola notification email) |
| `unknown` | Unknown / Not Set | System default. Cannot be deleted or deactivated. |

---

## 3. Recommended technical approach

### 3.1 Data model

Store sources as a reference table and point each lead at a row. Adding "Instagram" or "Google Business Profile" later is one inserted row, not a migration of the Leads table (acceptance criterion 7).

**Table `lead_sources`**

| Column | Type | Notes |
|---|---|---|
| `id` | integer, PK | |
| `key` | text, unique | Stable machine name, e.g. `yelp`. Used by integrations and rules. Never renamed once in use. |
| `label` | text | Display label. Safe to rename. |
| `is_active` | boolean | Inactive sources are hidden from pickers but kept on historic leads. |
| `is_system` | boolean | `true` only for `unknown`. Blocks delete/deactivate. |
| `sort_order` | integer | Picker order. |
| `created_at`, `updated_at` | timestamp | |

**New columns on `leads`**

| Column | Type | Notes |
|---|---|---|
| `lead_source_id` | FK → `lead_sources.id`, not null, default = `unknown` | The value shown everywhere. |
| `lead_source_origin` | enum `auto` · `manual` · `import` | How the current value was set. This is the lock: `manual` blocks automation. |
| `lead_source_detected_id` | FK → `lead_sources.id`, nullable | What detection concluded on arrival. Kept even after a manual correction so detection accuracy can be audited. |
| `lead_source_evidence` | JSON, nullable | Raw signals used: intake channel, form id, sender address, inbound number, UTM parameters, referrer. Diagnostics only, not shown in the list. |
| `lead_source_set_by` | FK → `users.id`, nullable | Null when set by automation. |
| `lead_source_set_at` | timestamp, nullable | |

Every change to `lead_source_id` also writes a row to the existing lead activity/audit log ("Source changed from Unknown to Yelp by A. Advisor").

### 3.2 Detection: channel declaration first, then rules

Detection is **not** text-mining the inquiry. Each entry point knows what it is and declares it. A single intake service then applies an ordered rule set to resolve the final source. The rules live in a table so a new marketplace can be recognised without a code release.

**Table `lead_source_rules`**

| Column | Notes |
|---|---|
| `channel` | Which intake path the rule applies to: `web_form`, `email_inbox`, `sms_inbound`, `voice_inbound`, `meta_leads`, `manual`, `import` |
| `match_field` | e.g. `sender_domain`, `form_id`, `utm_source`, `subject_contains` |
| `pattern` | Exact value or glob, e.g. `*.yelp.com`, `tagvenue.com`, `zola.com`, `facebookmail.com` |
| `lead_source_id` | Source to assign when the rule matches |
| `priority` | Lower number wins; first match stops evaluation |
| `is_active` | |

**Resolution order per channel**

| Channel | How it reaches the CRM | Resolution |
|---|---|---|
| Web form (2 venue apps) | App POSTs to `POST /api/leads/intake` with `channel: web_form`, venue, form id, UTM and referrer | → **Website**. UTM values are stored in evidence for campaign reporting; they do not change the Lead Source (a Facebook ad that lands on our site and converts on our form is still a Website lead; the ad is credited in GA4/Ads reporting). |
| Meta Lead Ads / Messenger | Meta webhook | → **Facebook** |
| Inbound SMS | SMS provider webhook; new number = new lead | → **SMS** |
| Inbound call | Phone system webhook or click-to-log from the call screen | → **Phone Call** |
| Inquiries mailbox | Inbound email parse | Match `sender_domain` against rules: `yelp.com` → **Yelp**, `tagvenue.com` → **Tagvenue**, `zola.com` → **Zola**, `facebookmail.com` → **Facebook**. No match → **Email**. |
| + New Lead (manual) | Advisor types it in | → **Unknown / Not Set** pre-selected; advisor may change it before saving. Origin = `manual` if they change it, otherwise stays `auto`/`unknown` so a later detection could still fill it. |
| CSV import | Import wizard | Map a "Source" column to `lead_sources.key` or `label`. Unmapped or unrecognised value → **Unknown / Not Set**. Origin = `import`. |
| Anything else / integration error | Payload missing or malformed | → **Unknown / Not Set**, evidence records the failure reason. |

The email rule is the one that matters most: Yelp, Tagvenue and Zola all notify by email, so without sender-domain rules every marketplace lead would be misfiled as "Email".

**Intake contract**

```json
POST /api/leads/intake
{
  "channel": "web_form",
  "venue": "crown_prince",
  "source_key": null,
  "evidence": {
    "form_id": "brochure-request",
    "utm_source": "google", "utm_medium": "cpc", "utm_campaign": "sj-corporate",
    "referrer": "https://www.google.com/"
  },
  "lead": { "...existing fields unchanged..." }
}
```

`source_key` is optional. When an integration is certain (Meta webhook), it sends the key. When omitted, the rules decide. Either way the service writes `lead_source_id`, `lead_source_detected_id`, `lead_source_evidence`, and `lead_source_origin = auto`, then hands off to the existing assignment step.

### 3.3 Overwrite protection

```
on automatic detection result D for lead L:
  if L.lead_source_origin == 'manual'            → do nothing (log "skipped: manual value")
  if L.lead_source_origin == 'import'            → do nothing
  if L.lead_source_id != unknown and != D        → do nothing (log conflict for review)
  else                                           → set lead_source_id = D, detected_id = D, origin = auto
```

- Later activity on the same lead through a different channel (a website lead who then texts) never changes the Lead Source. Source records the **first** inquiry; later channels appear in the activity timeline.
- The only way an automatic value replaces a manual one is the explicit **Reset to detected** action on the lead, available to Admin/Manager, which is itself logged.
- On lead merge, keep the surviving lead's source unless it is Unknown, in which case take the other lead's source and origin.

### 3.4 Permissions

| Role | View | Edit Lead Source | Reset to detected | Manage source list & rules |
|---|---|---|---|---|
| Admin | ✓ | ✓ any lead | ✓ | ✓ |
| Manager | ✓ | ✓ any lead | ✓ | — |
| Advisor | ✓ | ✓ own assigned leads | — | — |
| Read-only / Finance | ✓ | — | — | — |

### 3.5 User interface

**Leads list**

- Add a **Source** column immediately after **Captured** (both are "how and when this lead arrived"). Sortable.
- Add an **All sources** filter beside **All advisors**. Include "Unknown / Not Set" so unassigned sources can be worked as a queue.
- Unknown renders muted ("Not set") so it reads as a gap, not a value.
- A small indicator on the value: detected automatically vs. set by a person (tooltip shows who and when).
- **Export** gains two fields: `Source` and `Source origin`.

Proposed header row:

`Name · Venue · Contact · Event Date · Captured ↓ · Source · Guests · Status · Assigned · Follow-up`

**Lead detail**

- Lead Source is a select, ordered by `sort_order`, showing active sources plus the lead's current value if it has since been deactivated.
- When the current value differs from the detected value, show "Detected as Yelp on 05 Sep, changed to Email by A. Advisor" with **Reset to detected** for Admin/Manager.

**+ New Lead**

- Source select defaults to **Unknown / Not Set**. Not mandatory; an advisor on a live call should not be blocked. The Unknown queue in the list filter catches these later.

**Settings › Lead Sources** (Admin)

- Add, rename, reorder, deactivate sources. Deactivate is blocked for `unknown`, and blocked for any source still referenced by an active detection rule until the rule is retired.
- Manage detection rules (channel, field, pattern, source, priority) with a "Test against last 50 inbound emails" preview before saving.

### 3.6 Reporting

With the field in place the CRM can produce, per source and per venue: leads · qualified · tours · bookings · booking revenue. Joined with Google Ads spend this yields cost per lead and cost per booking, the two numbers Gate 1 in the playbook depends on. Export `Source origin` too, so a finance reviewer can see what share of the attribution was system-set versus hand-entered.

### 3.7 Migration and rollout

1. Create `lead_sources`, seed the nine rows above, create `lead_source_rules` and seed the four email-domain rules.
2. Add the `leads` columns with default `unknown` / `auto`. No existing behaviour changes.
3. **Backfill only from evidence.** Where the intake log records the channel (web app endpoint, SMS webhook, phone webhook), set the source from it with origin `auto`. Everything else stays Unknown. Do not infer from names or notes.
4. Update the two web apps and the SMS/phone/email integrations to call the intake contract with `channel`.
5. Ship the list column, filter and export field; ship the detail editor; ship Settings › Lead Sources.
6. Run the Gate 1 test from the playbook: submit one test lead through each entry point and confirm it appears in the list with the right source.

---

## 4. Acceptance criteria and test cases

| # | Criterion | Test |
|---|---|---|
| 1 | Source identified automatically when reliable information exists | Submit a form on each web app → Website. Send an SMS to the venue number → SMS. Forward a Yelp notification into the inbox → Yelp. Same for Tagvenue, Zola, Facebook. |
| 2 | Correct Lead Source saved to the record | Open each test lead; `lead_source_id`, `detected_id` and evidence are populated; origin = `auto`. |
| 3 | Lead Source appears in the Leads list | Column visible, sortable, filter works, value matches record. Export contains Source and Source origin. |
| 4 | Users can manually edit | Advisor edits own lead; Manager edits any lead; read-only role sees no editor. |
| 5 | Manual corrections preserved | Correct a lead from Email to Yelp, then re-run detection (or receive a duplicate webhook). Value stays Yelp; audit log shows the skip. |
| 6 | Undetectable sources → Unknown / Not Set | Send an email from a personal Gmail with no rule match → Email. POST to intake with no `channel` → Unknown, evidence records the reason. Create via + New Lead without choosing → Unknown. |
| 7 | New options without restructuring | Add "Instagram" in Settings; it appears in pickers and filter immediately; no schema change, no deploy. |
| 8 | No interference with existing CRM functions | Assignment routing, 1h SLA timer, follow-up sequence, Pipeline and Health views behave identically for leads with any source, including Unknown. Intake latency unchanged within tolerance. |

---

## 5. Decisions needed

1. Confirm the source list above is the full starting set, and whether **Google Business Profile**, **Instagram**, **Referral** and **Walk-in** should be seeded now (the playbook already reports on referral and walk-in).
2. Confirm that ad-driven website leads stay **Website** in this field, with campaign attribution kept in GA4/Ads rather than in Lead Source.
3. Confirm the role matrix in §3.4, in particular whether Advisors may edit sources on leads not assigned to them.
4. Confirm who owns the inquiries mailbox and the phone/SMS provider so the inbound integrations can be wired.
