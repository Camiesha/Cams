# Lead Source — Automatic Detection + Manual Override

**CRM › Leads › Lead Source** · Status: For review · Date: 5 Sep 2026 · Applies to: Crown Prince Event Hall, Alvin Studio
**Companion:** `events-venue-marketing-playbook.md` §5 (CRM), §7 (Ads → GA4 → CRM source field), §14 Gate 1
**Visual version:** published artifact "Lead Source Detection" (same content, information-designed).

**Read by role**

| Audience | Sections |
|---|---|
| Business Owner | 01 · 10 |
| CRM Admin | 03 · 05 · 06 · 08 |
| Product Manager | 01 · 02 · 11 · 14 |
| Developer | 04 → 09 · 11 |
| QA | 12 · 13 |

---

## 01 Executive summary

| Problem | Solution | Outcome |
|---|---|---|
| Leads arrive from two websites, phone, text, email and marketplaces, but the Leads list records no origin. Cost per lead and per booking by channel cannot be produced. | Each intake channel declares itself. A resolver sets **Lead Source** on arrival, falls back to **Unknown / Not Set** when unsure, and never overwrites a value a person has set. | Every lead carries one source. Leads, tours, bookings and revenue can be reported per channel and joined to ad spend for marketing ROI. |

| What changes | What does not change |
|---|---|
| New **Source** column, filter and export field on the Leads list | Lead assignment, the 1h SLA timer, follow-up sequences |
| Editable Source on lead detail, with audit trail | Pipeline, List and Health views, statuses, advisors |
| New Settings page: Lead Sources and detection rules | Existing lead fields and the lead count |
| Intake endpoint accepts a channel and resolves the source | Advisors can still create a lead on a live call; source is optional |

---

## 02 Current → Proposed

**Current** (Leads list screenshot, 5 Sep 2026). Subtitle: "Leads from 2 web apps + phone/text · 1h response target · new leads are shared out automatically." Actions: + New Lead, Export, Pipeline / List / Health. Filters: Search, All statuses, All advisors, SLA overdue. Columns: Name · Venue · Contact · Event Date · Captured (default sort) · Guests · Status · Assigned · Follow-up. **No source column, filter or export field.**

![Existing Leads list](images/leads-list-existing.png)

**Proposed.** Same screen plus: **Source** column after Captured (sortable), **All sources** filter (includes Unknown), Source and Source origin in Export. Indicator: dot = detected automatically; ring = set by a person (tooltip: who, when); "Not set" shown muted.

---

## 03 Source model

| Key | Label | Entry point | Detection | Notes |
|---|---|---|---|---|
| `website` | Website | Inquiry form on either venue web app | Auto | UTM stored as evidence; does not change source |
| `facebook` | Facebook | Meta lead form, Messenger, Facebook notification email | Auto | Webhook or sender domain `facebookmail.com` |
| `yelp` | Yelp | Yelp inquiry notification email | Auto | Sender domain `yelp.com` |
| `phone_call` | Phone Call | Inbound call: phone-system webhook or click-to-log | Auto | Advisor may also pick it on + New Lead |
| `sms` | SMS | Inbound text to a venue number | Auto | New number = new lead |
| `email` | Email | Inquiries mailbox, no other rule matched | Auto | Catch-all for the mailbox channel only |
| `tagvenue` | Tagvenue | Tagvenue inquiry notification email | Auto | Sender domain `tagvenue.com` |
| `zola` | Zola | Zola inquiry notification email | Auto | Sender domain `zola.com` |
| `unknown` | Unknown / Not Set | Manual entry, import without source, unrecognised payload | Fallback | System row; cannot be deleted or deactivated |

Adding a source (Instagram, Google Business Profile, Referral, Walk-in) is one new row in Settings › Lead Sources. No schema change, no deploy.

---

## 04 Detection flow

```
INQUIRY  (form · text · call · email · webhook)
   ↓
CHANNEL  web_form · sms_inbound · voice_inbound · email_inbox · meta_leads · manual · import
   ↓  POST /api/leads/intake
SOURCE RESOLVER
   1. source_key given by a certain integration → use it
   2. else first matching lead_source_rules row by priority
   ↓ match                         ↓ no match / bad payload
LEAD SOURCE                     UNKNOWN / NOT SET (origin = auto, editable later)
   ↓  writes lead_source_id, lead_source_detected_id, lead_source_evidence, lead_source_origin = auto
ASSIGNMENT (existing, unchanged; SLA timer starts here as today)
   ↓
LEADS LIST · Source column
```

---

## 05 Detection rules

| Pri | Channel | Signal | Rule | Result |
|---|---|---|---|---|
| — | `web_form` | Form on venue web app | Channel is sufficient; UTM/referrer to evidence only | Website |
| — | `meta_leads` | Meta webhook | Integration sends `source_key: facebook` | Facebook |
| — | `sms_inbound` | SMS provider webhook | Channel is sufficient | SMS |
| — | `voice_inbound` | Phone-system webhook | Channel is sufficient | Phone Call |
| 10 | `email_inbox` | sender_domain | `*.yelp.com` | Yelp |
| 20 | `email_inbox` | sender_domain | `tagvenue.com` | Tagvenue |
| 30 | `email_inbox` | sender_domain | `zola.com` | Zola |
| 40 | `email_inbox` | sender_domain | `facebookmail.com` | Facebook |
| 99 | `email_inbox` | — | No rule matched | Email |
| — | `manual` | + New Lead | Pre-selected; advisor may change before saving | Unknown |
| — | `import` | CSV Source column | Map by key or label; unrecognised value falls back | Mapped or Unknown |
| — | any | Missing or malformed | Evidence records the failure reason | Unknown |

**Why the email rules matter.** Yelp, Tagvenue and Zola all notify by email. Without sender-domain rules, three paid channels would report zero leads and "Email" would be overstated.

**Intake contract**

```json
POST /api/leads/intake
{
  "channel": "web_form",
  "venue": "crown_prince",
  "source_key": null,
  "evidence": {
    "form_id": "brochure-request",
    "utm_source": "google", "utm_medium": "cpc",
    "referrer": "https://www.google.com/"
  },
  "lead": { "...existing fields unchanged..." }
}
```

---

## 06 Override logic

```
AUTO  (resolver sets source or Unknown)
  → EDIT  (authorized user picks a source)
  → MANUAL  (origin flips; set_by / set_at recorded; audit row written)
  → 🔒 PROTECTED  (automation can never replace it; only "Reset to detected" by Admin/Manager can)
```

**Guard, on every automatic result D for lead L**

```
origin == manual        → skip; log "manual kept"
origin == import        → skip
source ∉ {unknown, D}   → skip; log conflict for review
else                    → source = D, detected = D, origin = auto
```

**Edge rules**

- Later contact never changes source. A Website lead who then texts stays Website; the text goes to the timeline.
- Merge: keep the surviving lead's source unless it is Unknown, then take the other lead's source and origin.
- A deactivated source stays on historic leads and in their picker; hidden from new selections.
- Every change is logged: "Source changed Unknown → Yelp by A. Advisor, 05 Sep 11:02".

---

## 07 Data model

```
leads ──lead_source_id──────────▶ lead_sources ◀──lead_source_id── lead_source_rules
      ──lead_source_detected_id──▶
      ──lead_source_set_by──────▶ users
```

| Table | Column | Type | Purpose |
|---|---|---|---|
| `lead_sources` | `id` | PK | |
| `lead_sources` | `key` | text, unique | Stable machine name; never renamed once in use |
| `lead_sources` | `label` | text | Display label; renameable |
| `lead_sources` | `is_active` | boolean | Inactive hidden from pickers, kept on historic leads |
| `lead_sources` | `is_system` | boolean | `true` only for `unknown`; blocks delete and deactivate |
| `lead_sources` | `sort_order` | integer | Picker order |
| `leads` | `lead_source_id` | FK, not null, default `unknown` | The shown value |
| `leads` | `lead_source_origin` | enum auto · manual · import | The lock; manual and import block automation |
| `leads` | `lead_source_detected_id` | FK, nullable | Kept after correction for accuracy audits |
| `leads` | `lead_source_evidence` | JSON, nullable | channel, form_id, sender, inbound number, UTM, referrer, failure reason |
| `leads` | `lead_source_set_by` | FK users, nullable | Null when set by automation |
| `leads` | `lead_source_set_at` | timestamp, nullable | |
| `lead_source_rules` | `channel`, `match_field`, `pattern`, `lead_source_id`, `priority`, `is_active` | | Lower priority wins; first match stops |
| `activity_log` (existing) | | | One row per source change: from, to, who, when, reason |

---

## 08 CRM UI

| List | Detail | Settings › Lead Sources |
|---|---|---|
| Source column after Captured, sortable | Source select ordered by `sort_order`; active sources plus current value | Add, rename, reorder, deactivate sources |
| All sources filter, includes Unknown | If changed: "Detected as Yelp on 05 Sep · changed to Email by A. Advisor" | Cannot deactivate `unknown` or a source used by an active rule |
| Dot = detected; ring = set by a person | Reset to detected (Admin/Manager) | Rules: channel, field, pattern, source, priority |
| "Not set" shown muted | + New Lead: Unknown pre-selected, not mandatory | "Test against last 50 inbound emails" preview |
| Export adds Source and Source origin | Import wizard maps a Source column | |

---

## 09 Permissions

| Role | View | Edit source | Reset to detected | Manage sources & rules | Export |
|---|---|---|---|---|---|
| Admin | ✓ | ✓ any lead | ✓ | ✓ | ✓ |
| Manager | ✓ | ✓ any lead | ✓ | — | ✓ |
| Advisor | ✓ | ✓ own assigned leads | — | — | ✓ |
| Read-only / Finance | ✓ | — | — | — | ✓ |
| Integration (API key) | — | Set on create only, origin `auto` | — | — | — |

---

## 10 Reporting

```
SOURCE → LEAD → TOUR → BOOKING → REVENUE
   └──── Google Ads spend per source ────┘ → MARKETING ROI
```

| Report | Grouped by | Measures | Needs |
|---|---|---|---|
| Leads by source | Source × Venue × Week | Leads, Unknown share, % detected vs manual | Source, Source origin |
| Funnel by source | Source × Venue | Leads → Qualified → Tours → Bookings | Source, status history |
| Cost per booking | Source | Ad spend ÷ bookings; revenue ÷ spend | Source + Ads spend export |

---

## 11 Migration

| # | Phase | Work | Owner | Exit check |
|---|---|---|---|---|
| 1 | Prepare | Answer decisions (14). Collect access to CRM, both web apps, SMS/phone provider, inquiries mailbox. Export baseline lead counts. | Owner · Admin · Finance | Baseline totals saved |
| 2 | Database | Create `lead_sources` (9 rows), `lead_source_rules` (4 rules). Add 6 columns to `leads`, default unknown/auto. | Developer | All views load unchanged; count = baseline |
| 3 | Intake | Resolver in intake endpoint; overwrite guard; audit rows; Reset to detected. | Developer | Unit tests per channel + Unknown fallback pass |
| 4 | Connect | Web forms send channel + UTM. SMS and phone webhooks. Mailbox → parser with domain rules. Meta webhook if used. | Developer · Admin | One test lead per channel lands with correct source |
| 5 | Screens | List column, filter, export. Detail editor. New Lead and import defaults. Settings › Lead Sources. | Developer | Values match records; adding a source needs no deploy |
| 6 | Backfill | Set source only where intake logs record the channel. All else stays Unknown. No inference from names or notes. | Developer, checked by Finance | Control total holds; per-source counts sum to total |
| 7 | Verify & go live | Run test matrix (13). First weekly leads-by-source report. Advisors work the Unknown filter to zero. | QA · Finance · Owner | All acceptance criteria pass; report comes from Export |

> 🔒 **Control total:** lead count before = lead count after. Baseline (phase 1), post-schema (phase 2) and post-backfill (phase 6) counts must be identical. **Completeness:** every lead has exactly one source; Unknown is counted, never blank; per-source counts sum to the total.

---

## 12 Acceptance criteria

| | # | Criterion | Verified by |
|---|---|---|---|
| ☐ | AC1 | Source identified automatically when reliable information exists | T01–T07 |
| ☐ | AC2 | Correct Lead Source saved to the record, with detected value and evidence | T01–T07, T09 |
| ☐ | AC3 | Lead Source appears in the Leads list, filter and export | T15, T16 |
| ☐ | AC4 | Authorized users can edit the Lead Source | T10, T11 |
| ☐ | AC5 | Manual corrections are preserved against automation | T12, T13 |
| ☐ | AC6 | Undetectable sources become Unknown / Not Set, never a wrong source | T08, T09, T14 |
| ☐ | AC7 | New sources added without restructuring the Leads table | T17, T18 |
| ☐ | AC8 | No interference with assignment, SLA, follow-up, views | T19, T20 |

---

## 13 Test matrix

| ID | Scenario | Steps | Expected | AC |
|---|---|---|---|---|
| T01 | Website form, each venue | Submit brochure form on both sites with UTM params | Source = Website, venue correct, UTM in evidence, origin auto | 1, 2 |
| T02 | Inbound SMS | Text the venue number from a new phone | New lead, Source = SMS | 1, 2 |
| T03 | Inbound call | Call the venue number; phone system logs it | New lead, Source = Phone Call | 1, 2 |
| T04 | Yelp notification | Forward a real Yelp inquiry email to the mailbox | Source = Yelp, sender domain in evidence | 1, 2 |
| T05 | Tagvenue notification | Same with a Tagvenue email | Source = Tagvenue | 1, 2 |
| T06 | Zola notification | Same with a Zola email | Source = Zola | 1, 2 |
| T07 | Facebook notification email | Same with a facebookmail.com email | Source = Facebook | 1, 2 |
| T08 | Direct personal email | Send from a Gmail address to the mailbox | Source = Email, not Unknown | 6 |
| T09 | Malformed intake | POST to intake with no `channel` | Lead created, Source = Unknown, evidence records reason, assignment runs | 2, 6 |
| T10 | Advisor edits own lead | As Advisor, change Unknown → Phone Call on assigned lead | Saved; origin manual; set_by/set_at filled; audit row | 4 |
| T11 | Role limits | Advisor opens another's lead; Read-only opens any lead | Advisor: no editor. Read-only: text only. Manager: edits any | 4 |
| T12 | Manual value vs duplicate webhook | Correct Email → Yelp, then replay original inbound webhook | Stays Yelp; log "manual kept" | 5 |
| T13 | Later contact on other channel | Website lead texts the venue number | Stays Website; SMS in timeline; no new lead | 5 |
| T14 | Manual create without source | + New Lead, leave Source, save | Source = Unknown, origin auto, in Unknown filter | 6 |
| T15 | List, sort, filter | Sort by Source; filter = Yelp; filter = Unknown | Rows match record values; indicators correct | 3 |
| T16 | Export | Export the filtered list | Columns Source and Source origin present and correct | 3 |
| T17 | Add a source | Settings › add "Instagram" | In pickers and filter immediately; no deploy | 7 |
| T18 | Deactivate a source | Deactivate Zola while in use; try to deactivate Unknown | Zola hidden from new picks, kept on lead; Unknown refused | 7 |
| T19 | Assignment and SLA unchanged | Create leads via each channel | Same rotation and 1h timer, including Unknown leads | 8 |
| T20 | Control total | Compare counts at baseline, post-schema, post-backfill; sum per source | All equal; sum = total; Unknown share reported | 8 |
| T21 | Merge | Merge Unknown into Yelp; then Yelp into Website | First: Yelp kept. Second: surviving Website kept | 5 |
| T22 | Reset to detected | Manager resets T12's lead; Advisor attempts same | Manager: back to detected, origin auto, logged. Advisor: action absent | 4, 5 |

---

## 14 Decisions required

| # | Decision | Recommendation | Owner | Blocks |
|---|---|---|---|---|
| D1 | Seed extra sources now: Google Business Profile, Instagram, Referral, Walk-in? | Yes for Referral and Walk-in (playbook already reports them); others when the channel goes live | Owner | Phase 2 |
| D2 | Do ad-driven website leads stay **Website**, with campaign attribution in GA4/Ads? | Yes. Lead Source = channel of arrival; campaign lives in evidence and GA4 | Owner · Finance | Phase 3 |
| D3 | May Advisors edit sources on leads not assigned to them? | No. Own leads only; Managers correct the rest | Owner | Phase 5 |
| D4 | Who owns the inquiries mailbox and phone/SMS provider accounts? | Name one person; the business holds the login, not the vendor | Owner · Admin | Phase 4 |

---

**Implementation summary:** INQUIRY → DETECTION → SOURCE → CRM → REPORTING. Each channel declares itself · rules resolve the source · Unknown when unsure · people can correct, automation cannot undo · the list, export and reports carry it.
