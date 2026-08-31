# Services RAC report template

## Contents
- [The cost stamp](#the-cost-stamp--top-right-of-the-page)
- [The Hire Box](#the-hire-box--non-negotiable)
- [Sections, in this order](#sections-in-this-order)
- [The quote-request emails](#the-quote-request-emails)
- [The Final Verdict](#the-final-verdict--required-and-it-goes-last)
- [Design](#design)
- [Before you publish — self-assessment](#before-you-publish--self-assessment)
- [Revision mode](#revision-mode)

---

## The cost stamp — top right of the page

Every RAC report carries a small stamp in the **top right corner of the page**, above everything else. Once, covering the whole job — research, verification and build.

```
Token: 184,300
Cost:  $2.94
```

Two lines, labels exactly `Token:` and `Cost:`. Small muted type, right-aligned, tabular numerals, beside the banner and never inside it. Token is the total for the whole job; cost is that count priced at the model's published rates, in USD, to the cent, with the arithmetic in a tooltip or one-line footnote. If the exact count is unavailable, estimate and write `est.` after both numbers. Not fixed-position — it must not repeat on every printed page.

## The Hire Box — non-negotiable

Every vendor that could plausibly be hired carries a Hire Box: in full in the candidate profile, linked from the matrix, and consolidated near the end.

| Field | Requirement |
|---|---|
| **Vendor** | Legal name and trading name, both, when they differ |
| **License** | Number with a **copy button**, linked to the board's own record, status and expiry dated |
| **Insurance** | Verified / stated-only / unknown — never "licensed and insured" as one unchecked phrase |
| **Phone** | With a copy button |
| **URLs** | Vendor site and the board record, both printed **visibly as text** under any button |
| **Availability** | Taking work or not, earliest start, how confirmed, dated |
| **Price picture** | Published range vs written quote — say which; all-in exposure named (permits, disposal, change orders) |
| **Review consensus** | One sentence: what customers agree on, the dominant complaint theme, and the owner's response style |
| **Verdict** | One sentence: hire / back-up / skip, and why in twelve words or fewer |

## Sections, in this order

1. **Status + confidentiality banner** — date facts were read, assumptions used (each marked by consequence: flips verdict / kills candidate / moves total), which self-assessment passes ran, and a confidentiality line — the report contains the reader's address and project details
2. **Hero** titled `<Topic> RAC`, then a **table of contents**
3. **"The call"** — green verdict box: the pick with license number and phone right there, the runner-up, any special-role vendor · four stat cards · one callout headed **"The finding that reframes everything"**
4. **What we're working with** — the reader's evidence read closely, ending in the single rule that eliminates candidates
5. **The gate** — hard requirements down the left (licensed · insured · serves the area · does this scope · available in the window), candidates across, pass/fail cells, eliminations before merit. Open with the discovery line: considered N, kept 5–7, one line per cut
6. **Comparison matrix** — criteria down the left, candidates across in **final rank order, pick leftmost**, each column headed by the **rank number**, the **vendor name**, and the **license number linked to the board record**. Green fill = wins that row; **blue rail down the pick's column** (thinner rail for the runner-up, `THE PICK` / `RUNNER-UP` badges) = the verdict — two different marks, so a column can win rows and still not be the pick. All-in total row, final `Verdict` row. One line under the matrix per candidate: why it holds its rank — priority fit first, then risk, then total
7. **Ratings** — the trust-ranked platform matrix (tiers from the research standards): one platform per row, most-trusted first, rows numbered, tier chip per row, left rail on T1 rows, `MOST TRUSTED` badge on row one only, `Blocked` / `Empty` / `Paywalled` status kept for platforms that returned nothing, one-line tier footnote under the table. Then per-candidate ratings with the pooling question answered: do these reviews belong to this location and this license?
8. **Candidate profiles, ranked** — one-line factsheet · **Hire Box** · verbatim customer quotes with attribution and date · **how the owner responds to reviews, quoted** · known failure patterns and when they show up · the honest case against
9. **What this should cost** — line-item table with published ranges, the all-in total (permits, disposal, materials tiers, change-order exposure), the **legal deposit cap for the reader's state with the statute named**, and a two-sided sanity check
10. **The policy layer** — the governing law with its effective date and what the reader loses if it goes wrong · vendor policies side by side · third-party and lien risk · warranty and guarantee terms as written · the contract protections to insist on
11. **Claim-by-claim audit** of whichever vendor's marketing started this
12. **"My assessment, in plain English"** — no jargon, short sentences: the situation simply · why the priority beats price · the recommendation with one headline reason plus three ranked ones and **the honest catch** · the runner-up · who you didn't pick and why · the uncomfortable part · **what you'd actually do, in order**
13. **Copy-paste-ready emails** — see *The quote-request emails*
14. **Numbered sources** — live links, retrieval dates, including the failures, grouped by type, each with its italic one-line explanation
15. **FINAL VERDICT** — the last section on the page

This order is the default, not a law. A reader who has already half-decided wants the Hire Box and the emails directly behind "The call"; a reader starting cold reads best in the order above. Keep the banner first and the verdict last, and keep the table of contents honest.

## The quote-request emails

One email per top vendor, **identical scope so the quotes compare** — this is the section that converts the report into prices. Each email asks for:

- **Itemized pricing** against the exact written scope
- **An insurance certificate sent directly by their broker** — not a PDF from the vendor
- **The guarantee in writing**
- Earliest start date and estimated duration

Each email carries a **copy button**. Differences between emails are limited to the vendor's name — any scope difference quietly breaks the comparison the reader will make later.

## The Final Verdict — required, and it goes last

Commit to **one choice**. Not a shortlist, not "it depends."

- **The pick in one sentence** — name, license number, phone, and what the reader does next.
- **Why you chose it** — reasoning tied to the stated priority; what evidence convinced you and how much weight each piece got.
- **Why each of the others is out — one by one, by name** — what it was genuinely good at, what knocked it out, whether it stays as back-up.
- **What would change your mind** — the one fact that flips the call to a named runner-up.
- **Your confidence level**, and what's still unconfirmed underneath the call.

Written as a decision the reader could act on today. No new evidence in this section; closing argument, not a summary.

## Design

Clean professional document: light grey ground, white rounded cards with soft shadows, 1060px column, system fonts, blue accents with green / amber / red status chips and callouts. Works on mobile, prints cleanly, holds in light and dark and the un-stamped system theme — every colour from a token.

- **No table scrolls sideways — failure state, not a layout.** Budget columns before writing: six including the row label is the ceiling on the 1060px column, three on a phone. Below ~760px, reflow every comparison table into one stacked block per candidate (`display:block` rows, `::before` labels from `data-label`). `overflow-x: auto` on the container is the safety net, never the plan; if a table still needs it, restructure the table. Platform matrices are rows-per-platform for exactly this reason.
- **Every button prints its destination URL as visible text underneath** — buttons die on paper, and the reader needs the domain before trusting it. Trim tracking parameters.
- **Copy buttons** on every phone number, license number and email draft.
- The hero is CSS or inline SVG — remote images are blocked in a self-contained page, and a vendor's logo is marketing, not evidence.
- Matrix marking discipline: **row wins are background fill, the verdict is a border rail** — never the same device, so a cell can show both. Watch specificity: a column rule that sets `background` erases the row-win signal. When tables reflow on a phone, carry the pick's rail into its stacked block and append the badge to its label.

## Before you publish — self-assessment

Run three passes over the built page, in order. Fix what they surface.

**Pass 1 — Plain English.** Load the `clear-writing` skill and apply it to every word. One name per vendor throughout — never rotate between the legal name, the trading name and "our pick". One idea per sentence, 25 words max, no semicolons. Active voice with a named actor. No hedging, no marketing adjectives. Every legal or trade term defined in parentheses at first use ("mechanic's lien (a legal claim on your home a subcontractor can file if the contractor doesn't pay them)"). The *plain English* section is held stricter still: kitchen-table voice.

**Pass 2 — Layout.** No sideways scroll at 1060px or 380px. A decision element reachable from every screen. Source beside every claim. Headings alone tell the whole story. Chips mean one thing each, everywhere. Prints legibly — URLs survive as text. Both themes hold.

**Pass 3 — Honesty.** Every fact dated. Every unproven claim chipped. Dead ends printed with the number or URL to close them. Every rejected vendor got its fair word. The verdict commits to one name.

**State in the banner which passes ran.** A skipped pass is stated, not hidden.

## Revision mode

When the user asks to update an existing report — a revision, not a rewrite, and never a silent patch:

- **Re-open every cited link; re-verify license status and availability** for every finalist. Anything not re-opened keeps its old date, visibly.
- **Chip every change** — `Was $4,800`, `New in rev 2`, `License renewed`, `No longer taking work`.
- **Bump the revision number in the banner**, with one paragraph on what changed.
- **Never silently drop a prior finding** — print the correction instead.
- **Keep the artifact URL** — republish the same artifact; a new URL is a last resort, stated when it happens.
- A revision follows every rule in this template, including the three self-assessment passes.
