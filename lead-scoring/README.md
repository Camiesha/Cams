# CPH / ACD — Lead-Scoring Research & Redesign

**For:** Crown Prince Event Hall (CPH) · Alvin Studio & Courtyard (ACD) · event-inquiry CRM
**Prepared:** October 2026
**Scope:** Lead-scoring methodology (research-backed), automated calculation + backend logic, UI redesign specification, and a clickable prototype.

## What's here

| File | What it is |
|---|---|
| `report.html` | The full deliverable — all 12 sections: executive summary, current-model audit, research & best practice (with cited sources), scoring architecture, the final scoring matrix, Hot/Warm/Cold rules, the calculation formula with five worked examples, backend/automation requirements, UI recommendations, a testing & validation plan, a phased roadmap, and the complete visual redesign spec. Open it in any browser. |
| `prototype.html` | A self-contained, clickable prototype. Pipeline board with live score rings, a click-to-open score breakdown drawer, an activity/score timeline, a prioritisation dashboard, and a mobile view. The **“Simulate Calendly tour”** button on the new lead recomputes the score with the real model and shows the override pushing it to Warm. |

## The one-paragraph summary

The current score mostly measures **profile completeness and staff admin actions**, so a tidy-but-cold form outscores a serious buyer who booked a tour on arrival. The redesign replaces it with a **two-axis, lifecycle-aware buying-intent score**: intent/behaviour is the dominant axis (55 of 100, driven by the furthest booking milestone reached), fit/qualification is secondary (35), engagement decays (10), negatives are capped and reversible, and **classification overrides** guarantee the behaviour the business cares about — a self-booked Calendly tour makes a lead *at least Warm*, a deposit discussion makes it *Hot*. New/uncontacted leads are **“Not scored yet”** (shown with missing fields + a next action), never a misleading low “Cold”. A confirmed booking is treated as a **conversion** (Won lifecycle state), not a 100-point prospect.

## Honesty of the number (read this)

The score is a **weighted buying-intent priority score out of 100 — not a statistical probability of booking.** Every score, conversion rate and threshold in these files is **illustrative** until it is backtested and calibrated against CPH/ACD's own historical bookings. The report defines exactly how to get from the interim priority score to a calibrated predictive probability once enough closed outcomes exist (`report.html` §4, §10).

## Implementation note

No live CRM source code was present in this repository, so the deliverable is a high-fidelity specification plus a working prototype, written so the CRM developer can translate it directly into scoring rules, backend triggers, data fields and test cases (`report.html` §8, §12.J). It is **grounded in the live CRM**: the video-tour transcript in this repo (`web-crm-video-tour-transcript.md`) confirms the CRM's **Journey** (Lead → Contacted → Tour → Proposal → Deposit → Won) and the records the engine reads — Communications thread, Interaction Recap, Quotation with 72-hour deposit link, Payments, and the e-signed rental agreement — all of which map directly to scoring factors (`report.html` §8). The model therefore reuses existing lead fields and event records, computes server-side in California (America/Los_Angeles) time, keeps weights in configuration for retuning, and logs every change idempotently for audit and the trend timeline. The only inputs flagged for the dev team to confirm are the **tour source** (Calendly self-booked vs. staff-arranged) and **no-show** capture, which drive the Warm override and the reversible no-show penalty.
