---
name: rac-product-report
description: Builds a RAC report — Research · Assessment · Comparison — a self-contained HTML buying report for any physical product purchase, ending in one committed verdict where every candidate carries a live purchase link, the full landed price, the warranty terms, and the review consensus. Use this whenever the user is working out what product to buy, comparing models or brands, asking "which one should I get" or "is this one any good", researching appliances, electronics, furniture, mattresses, bedding, tools, cookware, or any physical goods, or asking for a buying guide, product comparison, shortlist, or shopping recommendation — even if they never say "RAC report". Also use it when they name a specific model and want it vetted before they buy.
---

# RAC report — Research · Assessment · Comparison

A RAC report is a buying report for a physical product. Its job is narrow and demanding: carry the reader from "I'm not sure" to a completed purchase in a single read. That shapes everything below. Every product that survives to the comparison arrives with a live purchase link, the full landed price, the warranty, the review consensus and a verdict — and the report closes by naming **one** product to buy, not a shortlist.

Deliver it as one self-contained HTML artifact.

## Phase 1 — Intake, after reconnaissance

Research aimed at the wrong constraint is wasted — but so is a questionnaire the user abandons. Every question spends the user's patience, so each one has to buy accuracy the report could not get any other way.

**If the product is not yet clear**, ask one question and wait:

> **What are you buying?** Name the product line, or lines — and any brand or model you're already leaning toward.

**Step 1 — reconnoitre before asking anything else.** Spend a short sweep — a few searches, one or two Tier-1 buying guides — learning what actually splits this category's field: the attribute that changes the winner, the constraint that kills candidates at the gate, the cost line that moves the real price. Do this **before** composing a single question. Questions written in ignorance of the category are stock questions, and stock questions are what make users quit an intake.

**Step 2 — build the question list against the impact test.** Hard cap: **seven questions**. Every candidate question must pass:

> If the answer changed, would the pick change, would a candidate die at the gate, or would the landed price move materially?

No on all three → don't ask it. Assume the sensible default and print the assumption. The standing nine (ship-to + ZIP, budget, the one priority, dealbreakers, use context, works-with, timing, condition, candidates already in play) are **candidates for the list, not entitled to it** — reconnaissance decides which survive. Ship-to, budget, the priority and the hard fit constraint almost always pass the test; timing and condition often don't. Derive category questions from the same four angles as always — **fit** (the measurement or standard that makes a product impossible), **ranking** (the use-pattern detail that reorders winners), **price** (the accessory, install or consumable that moves the real cost), **risk** (the service or return exposure that changes the deal).

**Step 3 — ask once, ranked by impact.** One message, numbered, most decision-changing question first — a user who answers only the top two has then answered the two that matter most. Each question carries one clause on *why it changes the report* ("decides which candidates fit through the door") and the best-guess default in brackets.

**Step 4 — say plainly that answering is optional.** Close the message with: *"Answer any, all, or none — 'go' runs the report on the defaults shown."* Every unanswered question becomes a printed assumption in the status banner, marked with what a wrong guess would do: flip the verdict, kill a candidate, or move the price.

Play the brief back in three lines, then start.

**Never block on the intake.** "Go", "defaults", silence-then-repeat or "just decide" means proceed immediately on the stated defaults. A report delivered on reasonable, visible assumptions is worth far more than a question that stalls the work.

If more than one product line is in scope, each gets its own gate, matrix, profiles and verdict, plus one combined basket total at the end.

## Phase 2 — Research

Read `references/research-standards.md` before searching. It carries the source hierarchy, the product-specific verification rules — exact model numbers, review pooling, landed cost, authorized sellers, warranty documents — and the citation format. Those rules are the whole difference between this and an affiliate listicle, so treat them as the method, not as background reading.

**Decide which review platforms apply, and rank them, while you research.** The report prints a trust-ranked platform matrix, and which platforms belong in it is a judgement about this specific product — labs and retailer corpora for a shelf item, BBB and Google Reviews when an installer is part of the purchase. The tiers and the matrix spec are in `references/report-template.md`.

**Find the field with the five discovery sweeps** in the standards' *Finding the field* section — lab winners, the anchor's own siblings, each rival brand's equivalent, retailer category listings, owner communities. Long-list 10–20, cut to 5–7 against the cut rules, and keep one line per cut for the report. The anchor product is always a candidate.

**Open every source you cite.** A URL you haven't loaded is not a citation. A buy link you haven't confirmed is worse than no link at all, because it sends the reader to a dead page or the wrong size at checkout — the exact failure this report exists to prevent. Before a URL goes in a Buy Box, confirm it resolves and lands on the right size, colour and capacity. While on the manufacturer's page, capture the official product image of the exact variant — the report embeds real photos as data URIs.

## Phase 3 — Write the report

Read `references/report-template.md` for the section order, the cost stamp, the Buy Box specification, the review-platform matrix, the Final Verdict requirements, the design spec and the pre-publish self-assessment.

Build it as HTML and publish it with the Artifact tool, loading the `artifact-design` skill first — the reader needs a page whose buy buttons actually work, on a link they can reopen at the store. If the Artifact tool isn't available in this environment, write the HTML to a file and send it to them instead.

Three things are required on every report and easy to forget. **The cost stamp** — `Token:` and `Cost:` in small muted type at the top right of the page, once, covering the whole job. **The review-platform matrix** — ranked most-trusted first, tier badge on every row, top row badged `MOST TRUSTED`. **The three self-assessment passes** — plain English, layout, honesty — run over the built page before you publish, with the `clear-writing` skill loaded for the first one. All three are specified in the template.

Two constraints worth knowing before you design. Remote images and external stylesheets are blocked in a self-contained page, so product photos go in as compressed data URIs (the template's *Product images* section has the sizes) and the hero is CSS or inline SVG. And **the reader must never have to drag a table sideways to read it** — budget the columns, let cells wrap, and reflow wide tables into one stacked block per candidate on narrow screens. `overflow-x: auto` on the container is the safety net that keeps the page body from scrolling, not the plan. The template's *Tables must read without sideways scrolling* section has the full rule; follow it, because this report is mostly tables and it is the detail most likely to make one unreadable.
