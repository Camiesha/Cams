---
name: rac-services-report
description: Builds a RAC report — Research · Assessment · Comparison — a self-contained HTML report for hiring a service, contractor, vendor, or professional, ending in one committed verdict where every candidate carries a verified license, insurance status, availability, review-trust ranking, and copy-paste quote-request emails with identical scope. Use this whenever the user is deciding who to hire — contractors, cleaners, roofers, landscapers, plumbers, movers, repair shops, agencies, lawyers, accountants, software vendors, SaaS subscriptions — or asks "who should I hire", "which company should I use", "is this contractor legit", or wants vendors compared or a quote vetted. For buying a physical product, use rac-product-report instead.
---

# RAC report — services & vendors edition

A RAC report for a hire. Its job: carry the reader from "I don't know who to trust" to a signed, protected engagement in a single read. Every candidate that survives to the comparison arrives with a verified license, insurance status, availability, a trust-ranked review picture and a verdict — and the report closes by naming **one** vendor, not a shortlist.

Deliver it as one self-contained HTML artifact. Sibling skill: `rac-product-report` is for physical products; this one is for people and companies you hire. The deciding question: does the purchase fail because a *thing* breaks, or because a *person* doesn't show up?

## Phase 1 — Intake, after reconnaissance

Every question spends the user's patience, so each one has to buy accuracy the report cannot get another way.

**If the hire is not yet clear**, ask one question and wait:

> **What are you hiring for?** Name the job — and any vendor you're already leaning toward or have a quote from.

**Step 1 — reconnoitre before asking anything else.** A short sweep first: what credential kills candidates in this category, what cost line moves the real total, what risk changes the contract. Questions composed in ignorance of the category are stock questions, and stock questions make users quit.

**Step 2 — build the question list against the impact test.** Hard cap: **seven questions**. Each must pass: *if the answer changed, would the pick change, would a candidate die at the gate, or would the total move materially?* No on all three → don't ask; assume the default and print the assumption. Location + service address area, budget, the one priority, scope, and timing window almost always pass. Derive the rest from four angles: **eligibility** (the credential or coverage that makes a vendor impossible), **ranking** (the job detail that reorders winners), **cost** (the permit, disposal, materials tier or change-order exposure that moves the total), **risk** (the lien, damage, or no-show exposure that changes the contract).

**Step 3 — ask once, ranked by impact.** One message, numbered, most decision-changing first. Each question carries one clause on why it changes the report, and the best-guess default in brackets.

**Step 4 — say plainly that answering is optional.** Close with: *"Answer any, all, or none — 'go' runs the report on the defaults shown."* Unanswered questions become printed assumptions in the banner, each marked with what a wrong guess would do: flip the verdict, kill a candidate, or move the total.

Play the brief back in three lines, then start. **Never block on the intake** — "go", "defaults" or silence-then-repeat means proceed on the stated defaults.

## Phase 2 — Research

Read `references/research-standards.md` before searching. It carries the candidate discovery sweeps, the source hierarchy, the license-number rule, the availability check, the quote-versus-price rule, the review-platform trust tiers and the citation format. Those rules are the difference between this and a lead-generation listicle.

**Find the field with the five discovery sweeps** in the standards — regulator directory, map-pack listings, per-platform top-rated, community word-of-mouth, trade-body member list. Long-list 10–20, cut to 5–7 against the cut rules, keep one line per cut. Any vendor the user named is always a candidate, audited as honestly as its rivals.

**Open every source you cite.** A URL you haven't loaded is not a citation. Verify the license in the board's own database, not on the vendor's site.

## Phase 3 — Write the report

Read `references/report-template.md` for the section order, the cost stamp, the Hire Box, the review-platform matrix, the quote-request emails, the Final Verdict, the design spec and the pre-publish self-assessment.

Build it as HTML and publish with the Artifact tool, loading the `artifact-design` skill first. If the Artifact tool is unavailable, write the HTML to a file and send it.

Four things are required on every report and easy to forget. **The cost stamp** — `Token:` and `Cost:` top right, once, for the whole job. **The trust-ranked review-platform matrix** — most-trusted first, tier chips, `MOST TRUSTED` badge on row one. **The identical-scope quote emails** with copy buttons. **The three self-assessment passes** — plain English (load `clear-writing`), layout, honesty — run over the built page before publishing.

Two constraints. Remote images and external stylesheets are blocked in a self-contained page — the hero is CSS or inline SVG, never a vendor's logo pulled from the web. And **no table scrolls sideways** — budget columns before writing, reflow to stacked blocks under ~760px; the template's table rules apply to every matrix in the report.
