# Research standards for a RAC report

## Contents
- [Finding the field — how candidates get chosen](#finding-the-field--how-candidates-get-chosen)
- [Source hierarchy](#source-hierarchy)
- [Never cite](#never-cite)
- [Product verification — the rules that decide this category](#product-verification--the-rules-that-decide-this-category)
- [Citation format](#citation-format)
- [Rules — no exceptions](#rules--no-exceptions)

---

## Finding the field — how candidates get chosen

The verdict can only be as good as the field it beat. "Work to 5–7 candidates" is the output of this section, never the starting point — a great verdict over a badly chosen field is still a bad answer.

**Decompose the anchor first.** When the user gives one product, break it into the attributes that define what "comparable" means: category, size or capacity class, price band, the defining architecture or feature, and the sales channel. These attributes are the walls of the comparison set. A candidate outside them is a different purchase, not a competitor.

**Run all five discovery sweeps.** Each looks from an angle the others are blind to, and skipping one is how a field ends up biased:

1. **Lab winners** — what the Tier-1 testing outfits currently rank top in this category. Used for *discovery* here; their rankings still need verifying like any other claim. Catches the best product the user has never heard of.
2. **Same brand, one step up and one step down** — the anchor's own siblings. Catches "you're paying for the wrong tier of the right product."
3. **Each rival brand's equivalent** — one candidate per major brand in the category, matched to the anchor's class. Catches the direct competitor the marketing page pretends does not exist.
4. **Retailer category listings** — the anchor's own category at two or more major retailers, filtered by the hard constraints, sorted by rating and by best-selling. Catches the boring incumbent that owns the market.
5. **Owner communities' "buy this instead"** — what real owners recommend when someone asks about the anchor. Tier-4 evidence, discovery-only. Catches what labs have not tested yet.

**Long list first, then the cut.** The sweeps should produce 10–20 names. Cut to 5–7 against these rules:

- Every survivor must plausibly pass the hard constraints and be **purchasable today from an authorized seller**.
- The field must **span the price band** — include the credible budget floor and one stretch candidate.
- Include **at least one different-architecture challenger** — a candidate that disagrees with the anchor's whole approach, so the report has to argue for the architecture rather than assume it.
- **The anchor itself is always a candidate**, audited as honestly as its rivals.
- No more than **half the field from one brand, and no more than half found through one retailer**. A field that one storefront chose is that storefront's ad.

**Print the discovery.** The report states how many candidates were considered, where each finalist was found, and one line per long-list cut — "LG LRMDS3006S — cut: $600 over ceiling." A reader who can see what was considered and rejected can trust the field; a reader shown only the final five is being asked to take it on faith.

## Source hierarchy

Work down this order and always prefer the higher tier. When a lower tier contradicts a higher one, the higher tier wins and the contradiction gets printed in the report.

1. **Government, regulator and safety records** — CPSC recall database and SaferProducts.gov, FTC EnergyGuide, Energy Star product finder, EPA WaterSense, FDA for anything ingested, applied or medical, FCC ID lookup, NHTSA, EU Safety Gate, UK OPSS. Use the equivalents for the reader's country.

2. **The manufacturer's own published material** — the **spec sheet PDF**, the **use and care manual**, the **written warranty document**, the parts diagram, the firmware changelog. The manual and the warranty PDF outrank the marketing page every single time: marketing pages round numbers and omit the conditions, manuals don't.

3. **Independent testing labs, standards and certification bodies** — Consumer Reports, Good Housekeeping Institute, Wirecutter, RTINGS, DPReview, AHAM directory, UL / ETL / Intertek listings, OEKO-TEX STANDARD 100, GOTS, CertiPUR-US, GREENGUARD, NSF, Woolmark, USDA Organic. **Verify the certificate number in the issuing body's own database.** A badge printed on a product page is a graphic, not a certification, and unverifiable badges are common enough that checking is the point.

4. **First-party and authorized retailer product pages** — for exact SKU, live price, stock, delivery and return policy, plus their verified-purchase review corpora read at scale.

5. **Trade press, repair technicians, teardowns and parts availability** — iFixit repairability scores, authorized parts distributors, appliance and device repair channels. Directional; label it as such.

6. **Forums, Reddit, X, YouTube, social** — supporting colour only, never load-bearing, always labelled. One exception worth naming: long-running owner threads are often the only existing source of multi-year failure data. Use them for failure **modes**, never for failure **rates** — the people posting are self-selected for having a problem.

**Rank every review platform before you cite it.** The report prints a trust-ranked platform matrix, so decide the ranking during research, not while writing. Which platforms even apply is a judgement about the product: testing labs and retailer corpora carry a shelf item, while BBB, Google Reviews and Yelp carry an installer or a contractor and say nothing about a compressor. Separate what reviews the **product** from what reviews the **seller** — they answer different questions and never belong in one table. The tier definitions and the matrix specification are in `report-template.md` under *Review platforms — rank them by how much they can be trusted*; collect what they ask for while the pages are open, because going back for a variant-true review count later is expensive.

## Never cite

Affiliate "best of" listicles, AI-generated roundups, SEO content farms, dropshipper sites, marketplace listings from unauthorized sellers, aggregator scores with undisclosed methodology, sponsored "reviews" with no published test protocol, or anything you cannot open and read yourself.

Verify **every checkable claim** and **every marketing claim**, one by one, against an independent record. **Surface every contradiction you find** — a spec sheet that disagrees with the marketing page is one of the most useful things a report like this can hand someone.

## Product verification — the rules that decide this category

**The exact model number is the unit of analysis** — not the product family. Verify the full model string including its suffix, and flag derivative and retailer-exclusive SKUs. Big-box chains routinely carry a differently-suffixed variant of the "same" model with different features, a different warranty and a different price, which is why comparing families instead of models produces confident nonsense. Say plainly when two candidates are not actually the same product.

**Review pooling is a trap.** Many retailers pool reviews across size, colour and generation, so a headline "4.6 stars from 8,400 reviews" can belong mostly to a different product. State how many reviews belong to **this exact variant**; if you can't isolate them, say so and downgrade the signal.

**Stock is part of the price.** Check stock for the **exact variant** — finish, size, capacity — and print it, dated, in the Buy Box. Stock is per-variant: one finish can be sold out while another sits in stock at the same price on the same page, and a report that says "buy this" without "your variant is in stock" sends the reader to a dead end. When the recommended variant is out but another finish is stocked at the same price, say so and let the reader make the trade.

**A gated price is not a price.** Some retailers hide price, stock and delivery dates behind member sign-in. Never present a benchmark as the real number: print "member price unverified — benchmark $X at [vendor], read [date]", and name what the gate hides. Signing into the reader's account is out of scope, always.

**Price is a snapshot.** Date-stamp every price, and time-stamp it too. Say whether it's a sale price, when the sale ends if published, what the typical price has been if you can source it, and whether this category has a known sale cycle worth waiting for.

**Landed cost, not sticker.** Tax, shipping, delivery, installation, haul-away, required accessories, first-year consumables, subscription or app fees, and what it costs to send back if it's wrong. Estimate sales tax from the reader's ZIP and print the rate you used. Sticker price comparisons between products with different delivery and install requirements are simply wrong, not merely incomplete.

**Authorized sellers only.** Many manufacturer warranties are void when the item is bought through an unauthorized marketplace seller. Link the first-party or authorized listing. If the cheapest price comes from an unauthorized seller, state exactly what that discount costs in warranty terms and let the reader decide.

**The warranty is the document, not the headline number.** Read the PDF. A "10-year warranty" is usually one year of parts and labour plus ten years on a single component. Report: length by part, what voids it, who pays labour and return shipping, whether registration is required and by when, and whether it transfers.

**Capture the official product image of the exact variant** while you're on the manufacturer's page — you'll embed it later (see the template's *Product images*). Note the source URL; a photo of a lookalike SKU or the wrong colour misleads the reader at the exact moment they're matching the box in the store.

**Run a recall and safety check on every candidate by model number** — and print the result either way, because "checked, nothing found" is information the reader can't get by looking at the page themselves.

**Discontinued is not a bargain** unless parts and service availability are confirmed.

**Re-open before you publish.** Prices move inside a single day. Before the report ships, re-open the buy links of the pick and the runner-up and re-read their prices and stock; chip anything that moved. If research spanned more than a day, re-open every finalist.

**Second price point per finalist.** Each finalist carries one authorized-retailer price besides the main vendor's, read and dated — it is the reader's price-match ammunition at checkout. If no second authorized listing opens, say so; a stated dead end beats a silent gap.

**Fit before features.** Anything failing a hard constraint is eliminated at the gate, before merit is ever discussed. A product that can't fit through the door doesn't get a fair hearing on its cooling performance.

## Citation format

**Cite inside each section, at the point of the claim.** Any figure, price, rating, spec, certification or safety fact carries its source right there. Nobody should have to scroll to a bibliography to find out where a number came from.

**Under every source, add a one-line explanation in italics, in parentheses** — what the source is, who runs it, why it's authoritative here, and the date read:

> Source: **CPSC Recall Database — model WRX735SDHZ** · [cpsc.gov](https://www.cpsc.gov)
> *(US Consumer Product Safety Commission — the federal agency that issues and records product recalls; the authoritative record for safety actions on consumer goods. Read 16 Aug 2026, no recalls returned for this model.)*

**Every citation carries the date it was read.** Prices carry date and time.

**When a source is weak, say so in the italic line** — "brand-sponsored test, no published protocol — treat as directional". Naming a source's limits inside the citation is far more useful than quietly excluding it or silently relying on it.

The full **numbered source list still goes at the end**, grouped by type. Inline citations are in addition to it, not instead of it.

## Rules — no exceptions

- **Label, don't assert.** Tag anything unproven `Verified` / `Unconfirmed` / `Not verified` / `Ask`.
- **A failed registry or recall search is not proof something doesn't exist.** Say so in the report.
- **An empty platform is meaningless, not a red flag**, when that platform doesn't serve this category.
- **Date-stamp every fact.**
- **A filtered or anonymous review is never a finding.**
- **Volume never beats method.** Ten thousand unverified ratings do not outrank forty lab measurements, and the report says so out loud whenever the raw numbers invite the opposite conclusion.
- **Print your own dead ends** — with the URL or phone number for the reader to close them out themselves.
- **Be generous to the candidates you reject.** A product that conflicts with the reader's priority is wrong for them, not bad. Written any other way, the report reads as advocacy and the reader stops trusting the pick.
- **If the reader named a brand or model they're leaning toward, audit it honestly** — including the case that they should not buy it. That audit is often the most valuable page in the report.
