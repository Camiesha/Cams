# RAC report template

## Contents
- [The cost stamp](#the-cost-stamp--top-right-of-the-page)
- [The Buy Box](#the-buy-box--non-negotiable)
- [Sections, in this order](#sections-in-this-order)
- [Review platforms — rank them by how much they can be trusted](#review-platforms--rank-them-by-how-much-they-can-be-trusted)
- [The Final Verdict](#the-final-verdict--required-and-it-goes-last)
- [Design](#design)
- [Before you publish — self-assessment](#before-you-publish--self-assessment)
- [Revision mode](#revision-mode)

---

## The cost stamp — top right of the page

Every RAC report carries a small stamp in the **top right corner of the page**, above everything else. It appears **once**, and it covers the whole report — research, verification and build.

```
Token: 184,300
Cost:  $2.94
```

Rules:

- **Two lines, labels exactly `Token:` and `Cost:`.** Small type, muted colour, right-aligned, tabular numerals. It sits beside the status banner, never inside it.
- **Token is the total for the whole job**, not one message — every search, page read, image fetch and draft that went into this report.
- **Cost is that token count priced at the model's published rates**, in USD, to the cent.
- **Show your arithmetic in a `title` tooltip or a one-line footnote**: input tokens, output tokens, the rate used, and the model name. A number the reader cannot check is decoration.
- **If the exact count is not available to you, estimate it and write `est.`** after both numbers. Never present an estimate as a measurement.
- It must not print on paper as a header on every page — keep it in normal page flow at the top, not in a fixed or repeating position.

Keep it quiet. It is a receipt, not a headline: roughly 11–12px, the same muted grey as the status text, no border, no card.

## The Buy Box — non-negotiable

Every product that could plausibly be bought carries a Buy Box, and it appears **three times**: linked in the comparison matrix, in full in the candidate profile, and consolidated in the buy list near the end. Repetition is deliberate — the reader decides at different points in the page, and each one has to be a place they can act from.

| Field | Requirement |
|---|---|
| **Product photo** | The official image of the **exact variant**, embedded as a data URI thumbnail — see *Product images* in the Design section |
| **Vendor** | Brand and the selling retailer, named plainly on the first line |
| **Model number** | Exact, full string including suffix, with a copy button |
| **Info URL** | The manufacturer's product page — specs, manual, warranty PDF |
| **Buy URL** | Deep link to the **exact variant** — right size, colour, capacity — first-party or authorized retailer, opened and confirmed live on the date read |
| **Stock** | In stock or out, for the **exact variant**, dated — stock is per-finish and per-size; when the recommended variant is out but another is stocked at the same price, say so |
| **Full price** | Landed, line-itemed, dated, sale status stated — unit + sales-tax estimate for the reader's ZIP (state the rate used) + delivery + install + haul-away |
| **Warranty** | Length, what's genuinely covered, registration deadline |
| **Review consensus** | One sentence: what owners agree on, plus the dominant 1-star theme |
| **Verdict** | One sentence: buy / back-up / skip, and why in twelve words or fewer |

Every recommended item also carries **at least one backup retailer URL**, for stock-outs and price moves between writing and checkout — and the backup carries **its own price and date**, because a second authorized price is the reader's price-match ammunition.

**Print the URL, visibly.** Under every buy button, show the destination as short readable URL text — `bosch-home.com/us/shp78cm5n` — not only as link text. Link text alone hides the domain from a reader deciding whether to trust the seller, and dies entirely on paper. Trim tracking parameters; keep the path that identifies the variant.

**Worked example:**

> *(photo)* **Bosch · sold by Bosch-home.com** — 800 Series dishwasher · `SHP78CM5N` ⧉
> Info: [bosch-home.com/us/shp78cm5n →](https://www.bosch-home.com)
> [Buy at Bosch-home.com →](https://www.bosch-home.com) `bosch-home.com/us/shp78cm5n` · backup: [AJ Madison →](https://www.ajmadison.com) `ajmadison.com/b/SHP78CM5N`
> **$1,242** landed — $999 unit + $93 est. sales tax (9.375%, ZIP 95122) + $0 delivery (free over $396) + $150 install kit and hookup · sale price, ends 2 Sep 2026 · read 16 Aug 2026, 09:40 PT
> **Warranty** — 1 yr parts and labour, 5 yr racks and electronics parts only, lifetime on the stainless tub against rust-through. No registration required. Labour is on you after year one.
> **Consensus** — owners consistently single out how quiet it is and how dry the load comes out; the dominant 1-star theme is the top rack adjuster clips snapping around year two.
> **Verdict** — **Buy.** Quietest in class at this price, and the failure mode is a $30 part.

## Sections, in this order

1. **Status banner** — the date and time prices and facts were read, assumptions used, and a plain "re-check price before checkout" line
2. **Hero** titled `<Product> RAC`, then a **table of contents**
3. **"The call"** — green verdict box: the pick with its model number and buy link right there, the runner-up, and the budget or splurge alternative if either is genuinely different · four stat cards · one callout headed **"The finding that reframes everything"**
4. **What we're working with** — the reader's brief read closely, ending in the single rule that eliminates candidates
5. **The fit and compatibility gate** — hard constraints down the left, candidates across, pass/fail cells, and who is eliminated before merit is discussed. Open it with the discovery line — how many candidates were considered, where the finalists were found, and one line per long-list cut (see the research standards' *Finding the field*)
6. **Comparison matrix** — criteria down the left, candidates across, winning cell in each row shaded green, status chips throughout, a **landed price row**, and a final **`Verdict` row**. Each column header carries, top to bottom: the **rank number** (`#1`…`#5`, so a reader can name a column out loud), the **brand and selling vendor** on the first line, the **product thumbnail**, and the **model number linked to its buy page**. Order the candidate columns by final rank, **pick leftmost**, and mark the pick and the runner-up as columns — see *Mark the verdict on the matrix itself*. Carry only the candidates that cleared the gate — the eliminated ones were dealt with at the gate and putting them back here is what makes the table too wide to read (see *Tables must read without sideways scrolling*). **Under the matrix, print one line per candidate naming why it holds its rank** — priority fit first, then risk, then landed price — so the ranking logic sits where the reader is actually comparing, not only in the Final Verdict
7. **Ratings and review quality** — the review-platform matrix, **ranked most-trusted first**, with a tier badge on every row, how many reviews belong to this exact variant, the dominant praise theme and dominant complaint theme, and a note on any corpus you distrust. Build it to the rules in *Review platforms — rank them by how much they can be trusted*
8. **Candidate profiles, ranked** — one-line factsheet · **Buy Box** · verbatim owner quotes with attribution and date · how the brand actually handles warranty claims and support · known failure modes and at what age they show up · the honest case against
9. **What this should cost** — landed-cost table with published figures, a **two-sided sanity check** on the total, price history and sale timing, and a straight answer on whether waiting is worth it
10. **Warranty, returns and risk** — warranty terms side by side with effective dates and what voids them · return window, restocking fee, and who pays return shipping on something heavy · recall and safety record by model number · certifications verified against the issuing body's database · **extended warranty: a yes or no, with the arithmetic**
11. **Claim-by-claim audit** of whichever product's marketing started this
12. **"My assessment, in plain English"** — no jargon, short sentences: the situation simply · why the stated priority beats price · the recommendation with one headline reason plus three ranked ones and **the honest catch** · the runner-up · who you didn't pick and why · the uncomfortable part they should know · **what you'd actually do, in order**
13. **The buy list** — consolidated table, one row per recommended item: model number, direct URL, landed price, warranty, consensus, verdict, backup link · basket total if more than one thing is being bought
14. **Checkout card** — everything needed to complete the purchase in the next ten minutes: what to click, the exact variant to select, what to **decline** at checkout, the price to price-match against, the return deadline to diary, what to inspect the moment it arrives, **retailer checkout quirks** — the traps of this specific retailer when known (member gates that hide price and stock until sign-in, one delivery ZIP per session so two addresses mean two separate orders, per-finish stock), and **"do not buy this by mistake"** — the near-identical model numbers, wrong sizes and derivative SKUs that would look right
15. **Numbered sources** — live links, retrieval dates, **including the ones that failed**, grouped by type, each with its *italic* one-line explanation of what it is and why it's credible
16. **FINAL VERDICT** — the last section on the page

This order is the default, not a law. Reassess it against the reader's state before writing: a reader who has already half-decided wants the buy list and checkout card directly after "The call", with the evidence sections behind them; a reader starting cold reads best in the order above. When you deviate, keep the status banner first and the Final Verdict last, and keep the table of contents honest.

## Review platforms — rank them by how much they can be trusted

Star ratings are the weakest evidence in a RAC report and the evidence readers weigh most heavily. The fix is not to hide them. It is to **rank the platforms openly**, so the reader can see that 4.6★ on a forum and 4.6★ from a testing lab are not the same claim.

### First, decide which platforms are even relevant

**Self-assess before you search.** Platform relevance is decided by the product, and picking from a stock list is how a report ends up citing Yelp for a refrigerator. Ask what kind of purchase this is:

| If the purchase is… | The platforms that carry real signal |
|---|---|
| A physical product bought off a shelf | Testing labs, manufacturer SKU pages, verified-purchase retailer corpora, owner forums for failure modes |
| A product that arrives with delivery, install or service | All of the above, **plus** seller-level platforms — BBB, Google Reviews — because the installer is half the purchase |
| A service, contractor or trade | BBB, Google Reviews, Yelp, state licensing boards. Testing labs do not exist here |
| Software or a subscription | Trustpilot, G2, Capterra, the app stores, plus the vendor's own status page and changelog |
| Anything ingested, applied or worn | Regulator records first (FDA, MedWatch, EU Safety Gate), then labs and certifications, then retailer corpora |

Then state in one line **which platforms you excluded and why** — "no Yelp: it rates the store, not the refrigerator" is more useful to a reader than silently leaving it out.

### The trust tiers

Assign every platform you cite to a tier, and print the tier on the row. These are the defaults; argue with them in the report when a specific case warrants it.

| Tier | What earns it | Typical platforms |
|---|---|---|
| **T1 — Measured** | Buys the unit, tests it against a **published protocol**, publishes the numbers. Reproducible. | Consumer Reports, RTINGS, Reviewed, Good Housekeeping Institute, Wirecutter, accredited test labs |
| **T2 — Accountable** | Purchase or identity is verified, and the seller must answer on the record. | BBB (complaint record and response rate), verified-purchase retailer corpora, manufacturer SKU-level pages, Trustpilot **invited** reviews |
| **T3 — Open but attributable** | Real, persistent accounts and large volume, but no purchase check and known incentive problems. | Google Reviews, Yelp, Trustpilot organic reviews, app-store ratings |
| **T4 — Unverified** | Self-selected, anonymous, no verification of any kind. | Reddit, X, YouTube, TikTok, owner forums, Facebook groups |
| **T5 — Never cite** | Affiliate listicles, AI-generated roundups, SEO farms, aggregator scores with undisclosed methodology, sponsored posts with no protocol. | — |

**A tier is not a verdict on quality.** T4 is where multi-year failure data actually lives, and a RAC report is worse without it. The tier tells the reader *what kind of claim the source can support*: T1 supports "this measures X", T2 supports "buyers of this exact item report Y", T4 supports "this failure mode exists" and never "this failure rate is Z".

### The matrix

Build it as a table with **one platform per row, most-trusted at the top**. Rows, not columns — a report often cites eight or more platforms, which blows the column budget in *Tables must read without sideways scrolling*.

Columns, left to right: `#` · `Platform` · `Tier` · `Rating` · `Reviews` · `Belongs to this exact variant?` · `What it can support`

Marking, following the same logic as the comparison matrix — **fill means "this row scored well", rail means "this row is authoritative"**, so the two never collide:

- **Number the rows `#1`, `#2`, `#3`…** in trust order, so the ranking is stated and not merely implied by position.
- **Tier chip in its own column**, colour-graded from the accent hue: T1 strongest, fading to grey by T4. Never red — a T4 source is not an error.
- **Give every T1 row a left rail** in the accent colour, and a `MOST TRUSTED` badge on the first row only. That badge is the "highlight the trustworthy platform first" marking; one badge, not five.
- **Print a one-line footnote under the table** naming the tier rules, so a reader who has never seen a RAC report can decode the chips without scrolling.
- If a platform returned nothing, **keep the row** and mark the status — `Blocked`, `CAPTCHA`, `Empty`, `Paywalled`. A missing row reads as "not checked".

### Separate the product from the seller

**Two different things get reviewed and they must not share a table.** BBB, Yelp and Google Reviews rate the *retailer, installer or brand's service arm*. Testing labs and retailer corpora rate the *product*. A 4.8★ Google rating for a showroom tells the reader nothing about whether the compressor lasts.

When delivery, installation or warranty service is part of what is being bought, run **two matrices**: one for the product, one for the seller — and say plainly which risk each one covers. When the purchase is a plain shelf item, run the product matrix only and say why the seller matrix was dropped.

### Rules that stop the common failures

- **Pooling is the default failure.** A five-figure review count on an appliance page is almost always pooled across finishes, sizes and generations. Hunt for the variant-true number, print both when they disagree, and believe the smaller one.
- **Volume is not trust.** 10,000 T3 reviews do not outrank 40 T1 measurements. Say so in the report when the numbers invite the opposite conclusion.
- **BBB is a complaint record, not a rating.** Report the letter grade, the number of complaints, how many closed, and the response rate. The response rate is the useful number.
- **Trustpilot has two corpora.** Invited reviews (T2) and organic ones (T3) sit on the same page under one score. Split them or say you could not.
- **A rating with no readable review text is a number, not evidence.** Quote at least one verbatim review per platform you lean on, with date and attribution.
- **When tiers disagree, the higher tier wins and the disagreement gets printed.** That contradiction is often the most valuable paragraph in the section.

## The Final Verdict — required, and it goes last

Close by **committing to one choice**. Not a shortlist, not "it depends" — name the single product to buy, and own the call. A report that ends in options has handed the decision back to the reader, which is the one thing it was built not to do.

- **The pick, stated in one sentence** — model number, retailer, price, and the link. What to do next with it.
- **Why you chose it** — the reasoning in your own voice, tied directly to the stated priority. What evidence convinced you, and how much weight you gave each piece.
- **Why you eliminated each of the others — one by one, by name.** Every candidate gets its own line: what it was genuinely good at, the specific thing that knocked it out, and whether it stays as a back-up.
- **What would change your mind** — the one fact that, if it came back different, would flip the recommendation to a named runner-up.
- **Your confidence level**, and what's still unconfirmed underneath the call.

Write it as a purchase that could be completed today. **No new evidence in this section** and no repeating the earlier walkthrough — this is the closing argument, not a summary.

## Design

Clean professional document: light grey background, white rounded cards with soft shadows, 1060px column, system fonts, blue accents with **green / amber / red** status chips and callouts. Works on mobile, prints cleanly.

Two details that carry real weight here:

- **Buy links styled as buttons and always visible** — never behind a hover, since hover doesn't exist on the phone this will be read on in the store. The destination URL is printed under the button as plain text — see *Print the URL, visibly*.
- **Copy buttons on every model number**, because the reader's next move is pasting it into a retailer's search box.

### Product images

Real photos, embedded. Remote images are blocked in a self-contained page, so every photo is a **data URI**:

- Pull the **official product image of the exact variant** from the manufacturer or an authorized retailer — never a lookalike SKU, never a different colour.
- Downscale and compress before embedding: matrix thumbnails ~120px wide, profile images ~400px wide, JPEG or WebP, target 20–80KB each.
- Photos appear in the **matrix column headers**, the **candidate profiles / Buy Boxes**, and the **buy list**.
- Budget the page: total embedded images should stay under ~2MB; the artifact hard cap is 16MB.
- If no clean official image exists, draw an inline-SVG placeholder and say so — a wrong photo is worse than none.

Build the hero from CSS or inline SVG; external stylesheets are blocked too.

### Mark the verdict on the matrix itself

The matrix ends in a `Verdict` row, and that row sits at the bottom of a tall table. A reader halfway up it — comparing warranty terms, or capacity — has no idea which column is the one you're telling them to buy. They are reading the most decision-dense object in the report with the decision stripped out of it. Fix that by marking the pick and the runner-up **as columns**, not just as cells in the last row.

- **Order the columns by final rank**, pick leftmost, runner-up beside it. The reader's eye starts at the left of a table; put the answer there. Never order by price, brand or the sequence you happened to research in.
- **Give the pick's column a full-height rail** down both edges in the accent colour, capped top and bottom so it reads as one continuous frame rather than a stack of separate borders.
- **Give the runner-up a thinner rail of the same hue** — same family, visibly less emphasis. A different colour would read as a different *kind* of thing rather than second place.
- **Badge both column headers** — `THE PICK` and `RUNNER-UP` — so the marking is labelled and not left to be inferred from a colour.

**The one trap.** You now have two marking systems on one table: per-row green shading for "wins this criterion" and per-column marking for "this is the verdict". They must not be the same visual device, or a column that loses six rows still looks like a winner. Keep **row wins as background fill** and **column verdict as a border rail**, so the two compose instead of competing — and so a cell can show both at once, which is exactly what the pick's strongest rows should do. Watch specificity here: a column rule that sets `background` will silently override the row-win class and erase the other signal.

When the table reflows to stacked blocks on a phone, the rails collapse with the columns — carry the marking over by railing the pick's line inside each block and appending the badge to its label.

### Tables must read without sideways scrolling

This report is mostly tables, and a table the reader has to drag sideways is the fastest way to lose them. Horizontal scroll is a **failure state, not a layout** — treat it as a bug to design out, not a feature to enable.

The specific failure to avoid: the reader scrolls right to reach the last candidate, the row-label column slides out of view, and every cell becomes an unlabelled number. They now have to scroll back and forth to read a single row. Assume the reader is standing in a store on a phone.

Build every comparison table to this rule, in order:

1. **Budget the columns before you write the table.** On the 1060px column, six columns including the row label is the practical ceiling; on a phone it is three. If you have seven candidates, you do not have a seven-column table — you have two tables, or a table of the finalists plus prose for the rest. Splitting the matrix at the gate (survivors get the full matrix, eliminated candidates get a short list with the reason) is almost always the right cut.
2. **Let cells wrap and keep them terse.** Long sentences in cells are what actually blows the width. Cells carry a figure, a chip and at most a short phrase; the argument belongs in the prose underneath. Set `table-layout: fixed` with explicit column widths when a single verbose column is dragging the rest out of shape.
3. **Reflow, don't scroll, on narrow screens.** Below roughly 760px, break each comparison table into one stacked block per candidate — every cell on its own line with its criterion label beside it, via `display:block` rows and a `::before` drawn from a `data-label` attribute. One block per candidate reads far better on a phone than any amount of panning.
4. **Only then, the safety net.** Keep `overflow-x: auto` on the table's own container so the page body can never scroll sideways — but if a table still needs it after steps 1–3, the table is too wide and wants restructuring. When a scroll genuinely is unavoidable, `position: sticky; left: 0` the row-label column with an opaque background and a right-hand border, so the labels stay put and the reader never loses their row.

The same applies to any wide block — a landed-cost breakdown, a warranty comparison, a source table. If it only works by dragging, redesign it.


## Before you publish — self-assessment

The report is not finished when the research is finished. Run these three passes over the built page, in order, and fix what they surface. A RAC report that is correct but unreadable has failed at its only job.

### Pass 1 — Plain English

**Load the `clear-writing` skill and apply it to every word of the report.** This is not optional and not a style preference: the reader is deciding how to spend real money, often on a phone, often in a hurry.

The rules that matter most here:

- **One name per thing, all the way through.** The pick is called the same thing in the hero, the matrix, the buy list and the verdict. Never rotate between "the Samsung", "the Bespoke", "the 4-Door Flex" and "our pick" for one refrigerator.
- **One idea per sentence, 25 words maximum.** No semicolons. No em dash joining two thoughts.
- **Verbs, not noun phrases** — "the compressor fails", not "compressor failure occurs".
- **Active voice with a named actor** — "Costco collects the return", not "returns are collected".
- **No hedging and no marketing adjectives.** Delete "it is worth noting", "may potentially", "seamless", "robust", "comprehensive". State the fact that earns the claim.
- **Define every technical term in parentheses the first time** — "sealed system (the compressor and the cooling loop it drives)". Assume the reader knows nothing about the category and is not embarrassed about it.
- **Numbered steps carry the warning before the step**, one action per step, 20 words maximum per step.

The one exception: the *"My assessment, in plain English"* section is held to a stricter standard still. No jargon at all, short sentences, the voice of someone explaining it across a kitchen table.

### Pass 2 — Layout and readability

Walk the built page and check each of these. Fix, do not note.

- **Does any table scroll sideways at 1060px, or at 380px?** If yes, it is too wide — split it or reflow it. See *Tables must read without sideways scrolling*.
- **Can the reader act from every screen?** A buy button or a jump link should be reachable from anywhere in the page without hunting.
- **Is every claim's source next to the claim**, not only in the bibliography?
- **Does the page read top to bottom without backtracking?** If a section depends on a definition given later, move the definition.
- **Is there a visible hierarchy?** Section number, heading, then content. A reader skimming only the headings should get the whole argument.
- **Do the status chips mean one thing each**, consistently, everywhere they appear?
- **Does it print?** Backgrounds drop, links become invisible. Check that the buy URLs still read as text on paper — this is why *Print the URL, visibly* exists.
- **Both themes.** Light and dark, and the un-stamped system default. Every colour comes from a token.

### Pass 3 — Honesty

- Every number carries a date. Every price carries a date and a time.
- Every unverified claim carries a chip — `Verified` / `Unconfirmed` / `Not verified` / `Ask`.
- Every dead end is printed, with the URL or phone number for the reader to close it themselves.
- Every rejected candidate gets a fair word before it gets knocked out.
- The Final Verdict commits to one product. If it reads as a shortlist, rewrite it.

**Then state, in one line at the end of the status banner, which of these three passes you ran.** If you skipped one, say so. A reader who knows the report was not proofread reads it differently, and that is their right.

## Revision mode

When the user asks to update an existing RAC report, the update is a revision, not a rewrite — and not a silent patch.

- **Re-open every cited buy link and re-read every price and stock status.** Anything not re-opened keeps its old date, visibly.
- **Chip every change** — `Was $1,999`, `New in rev 2`, `Now out of stock`. A reader of rev 2 must be able to see what moved since rev 1 without a diff.
- **Bump the revision number in the status banner**, with a one-paragraph "what changed in this revision" at the top of it.
- **Never silently drop a prior finding.** If something no longer holds, print the correction — "rev 1 reported the Spend & Save deadline as 19 Aug; today's read no longer prints one."
- **Keep the artifact URL** — republish the same artifact so the reader's saved link stays live. A new URL is a last resort, stated when it happens.
- New evidence changes the report, not the standards: a revision follows every rule in this template, including the three self-assessment passes.
