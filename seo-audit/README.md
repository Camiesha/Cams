# Crown Prince Event Hall — SEO Audit & Action Plan

**Site:** https://crownprincehall.com/ · **Business:** Crown Prince Event Hall, 1654 Burdette Dr, San Jose, CA 95121 · (408) 408-1654
**Prepared:** September 2026 · **Scope:** On-page SEO, AI Overview optimization, local schema, conversion, Google Business Profile

## How this audit was built (read first)

The audit container's network policy blocks crownprincehall.com, Yelp, Eventective and the Wayback Machine, so the raw HTML could not be pulled. Every finding below is drawn from what Google and Bing have indexed from the site (title, description snippet, package names, policies) and from third-party listings. Three things must be confirmed in 10 minutes before rollout:

1. View source on the homepage and confirm the live `<title>`, `<meta name="description">`, and whether any `application/ld+json` block already exists.
2. Run https://search.google.com/test/rich-results on the homepage to confirm schema status.
3. Run https://pagespeed.web.dev/ on mobile; a 360° tour embed usually drags the Largest Contentful Paint score and needs lazy-loading.

## Findings

| # | Finding | Evidence | Impact |
|---|---|---|---|
| 1 | **The site is a single page.** Only the homepage is indexed; no dedicated wedding, quinceañera, corporate, party or pricing URLs surface for any query. One page cannot rank for five distinct intents. | `site:crownprincehall.com` returns only `/` | High |
| 2 | **Meta description is ~255 characters** and gets truncated mid-sentence in results. | Indexed snippet: "…360° virtual tour, and 100+ gated parking." | High |
| 3 | **Title tag leads with brand, not the query.** Current: "Crown Prince Event Hall — San José Event & Banquet Venue" (55 chars). "Banquet hall" and "San Jose" (unaccented, the form people type) are not front-loaded, and "wedding" is absent. | Indexed title | High |
| 4 | **No published pricing page**, while a direct competitor (The Prestige Venue) has an indexed `/pricing` URL. "Banquet hall prices San Jose" traffic is going to them. | Search results | High |
| 5 | **Business name is inconsistent** across the web: "Crown Prince Hall" vs "Crown Prince Event Hall". NAP (name, address, phone) consistency is a core local ranking factor. | Site body copy vs Yelp vs title | High |
| 6 | **Yelp category includes "Country Dance Halls"** and hours show "Open 24 hours". Wrong categories dilute relevance; 24-hour hours look spammy to Google's profile quality checks. | Yelp listing | Medium |
| 7 | **No FAQ block or FAQ schema detected** in indexed text; policies (outside catering, no outside alcohol, 90-day refund) exist as prose, not as answerable Q&A. | Indexed snippets | Medium |
| 8 | **Three competing calls to action** (book a private tour, 360° tour, same-day quote) and no low-commitment lead magnet for the researching visitor. | Indexed CTA text | Medium |
| 9 | Accented "San José" used in title/copy. Google matches it to "San Jose" but exact-form matching in titles still wins bolding in the SERP. Keep the accent in brand voice copy; use "San Jose" in titles, metas, H1s and schema. | Indexed title | Low |

## Prioritized action plan

| Priority | Action | Where | Effort | Owner |
|---|---|---|---|---|
| **High** | Replace homepage title and meta description (Snippet A) | `<head>` | 15 min | Web |
| **High** | Add LocalBusiness/EventVenue JSON-LD (Snippet E) to every page's `<head>` | `<head>` | 30 min | Web |
| **High** | Build 4 service landing pages: `/weddings/`, `/quinceaneras/`, `/corporate-events/`, `/parties/` using the title/meta/heading specs in Snippets A–B | New pages | 1–2 days | Web + copy |
| **High** | Build `/pricing/` with package comparison and the brochure lead-capture section (Snippet F) | New page | 1 day | Web + owner (prices) |
| **High** | Google Business Profile: set primary category "Banquet hall", add secondaries, paste description and services (Snippet H), set real inquiry hours, unify name to "Crown Prince Event Hall" | GBP | 1 hour | Owner |
| **High** | Fix Yelp: remove "Country Dance Halls", set hours to match GBP, match name exactly | Yelp | 20 min | Owner |
| **Medium** | Add FAQ section (Snippet D copy) above the footer on the homepage and FAQPage JSON-LD (Snippet D schema) | Homepage | 1 hour | Web |
| **Medium** | Insert the three AI Overview answer blocks (Snippet C) directly under their H2s | Homepage, `/pricing/` | 1 hour | Copy |
| **Medium** | Reorder CTAs: primary "Get 2026 Pricing & Floor Plan", secondary "Book a Private Tour", tertiary "Take the 360° Tour"; add `tel:` click-to-call in header on mobile | Sitewide | 2 hours | Web |
| **Medium** | Image hygiene: descriptive file names (`crown-prince-event-hall-san-jose-stage.jpg`), alt text with event + city, WebP, lazy-load the 360° embed | Sitewide | 2 hours | Web |
| **Medium** | Add `rel="canonical"`, XML sitemap listing the new pages, submit in Google Search Console, link every service page from the nav and footer | Technical | 1 hour | Web |
| **Medium** | Embed Google Map and a Google reviews widget on the contact block; ask every client for a Google review at the 48-hour post-event email | Homepage | 1 hour | Web + owner |
| **Low** | Claim and match NAP on The Knot, WeddingWire, Zola, Eventective, Peerspace, Tagvenue, Quinceanera.com | Citations | 3 hours | Owner |
| **Low** | Publish two guides: "How much does a 300-guest wedding cost in San Jose?" and "Quinceañera venue checklist for San Jose families" | `/blog/` | 1 day | Copy |
| **Low** | Spanish-language quinceañera page (`/es/quinceaneras/`) with `hreflang` | New page | 1 day | Copy |
| **Low** | Add `Event` schema for any open-house or tasting dates | Events | 30 min | Web |

---

## Snippet A — Title tags and meta descriptions

All titles ≤ 60 characters; all descriptions ≤ 160 characters.

| Page | Title tag | Meta description |
|---|---|---|
| Homepage `/` | `Crown Prince Event Hall \| Banquet Hall in San Jose, CA` (54) | `Crown Prince Event Hall is a 4,100 sq ft banquet hall in San Jose, CA for up to 300 guests. Stage, dance floor, full bar, 100+ gated parking. Book a tour today.` (160) |
| `/weddings/` | `San Jose Wedding Venue for 300 Guests \| Crown Prince Hall` (57) | `Host your wedding at Crown Prince Event Hall in San Jose. Red-carpet entrance, bridal suite, dance floor and full bar for up to 300 guests. Same-day quotes.` (156) |
| `/quinceaneras/` | `Quinceañera Venue in San Jose, CA \| Crown Prince Hall` (53) | `Celebrate your quinceañera at Crown Prince Event Hall, San Jose. Grand entrance, stage, dance floor and 100+ gated parking for up to 300 guests. Book a tour.` (157) |
| `/corporate-events/` | `Corporate Event Venue San Jose \| Crown Prince Hall` (50) | `Corporate event venue in San Jose with stage, big-screen TVs, sound and planning support. Seats up to 300 for banquets, mixers and presentations. Get a quote.` (158) |
| `/parties/` | `Birthday & Party Venue San Jose \| Crown Prince Hall` (51) | `Birthday, anniversary and graduation venue in San Jose for up to 300 guests. Packages with Chiavari seating, full bar and gated parking. Book a tour.` (149) |
| `/pricing/` | `Banquet Hall Pricing & Packages San Jose \| Crown Prince` (55) | `See Crown Prince Hall packages for San Jose weddings, quinceañeras and parties. All fees up front, same-day quotes, 90-day refund policy. Get the brochure.` (155) |
| `/virtual-tour/` | `360° Virtual Tour \| Crown Prince Event Hall San Jose` (52) | `Take a 360° virtual tour of Crown Prince Event Hall, a 4,100 sq ft San Jose banquet hall for up to 300 guests. Then book a private in-person tour.` (146) |
| `/book-a-tour/` | `Book a Tour \| Crown Prince Event Hall, San Jose CA` (50) | `Book a private tour of Crown Prince Event Hall, 1654 Burdette Dr, San Jose, CA 95121. Call (408) 408-1654 or send your date and guest count for a quick quote.` (158) |

Homepage head block, ready to paste:

```html
<title>Crown Prince Event Hall | Banquet Hall in San Jose, CA</title>
<meta name="description" content="Crown Prince Event Hall is a 4,100 sq ft banquet hall in San Jose, CA for up to 300 guests. Stage, dance floor, full bar, 100+ gated parking. Book a tour today.">
<link rel="canonical" href="https://crownprincehall.com/">
<meta property="og:type" content="business.business">
<meta property="og:title" content="Crown Prince Event Hall | Banquet Hall in San Jose, CA">
<meta property="og:description" content="4,100 sq ft San Jose event venue for weddings, quinceañeras, corporate events and milestone parties. Up to 300 guests, full bar, 100+ gated parking.">
<meta property="og:url" content="https://crownprincehall.com/">
<meta property="og:image" content="https://crownprincehall.com/REPLACE/hall-wide-1200x630.jpg">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="US-CA">
<meta name="geo.placename" content="San Jose">
```

## Snippet B — Heading structure

One H1 per page. H2s carry the question or intent people search; H3s carry package and feature names. Keep every H2 followed by at least 40 words of real copy.

**Homepage `/`**
```
H1  San Jose Banquet Hall & Event Venue for Up to 300 Guests
H2  Weddings, Quinceañeras & Corporate Events at Crown Prince Event Hall
H2  What's Included in Every Crown Prince Event Hall Package
    H3  Weekday Flex (Monday–Thursday, hourly)
    H3  Weekend Essentials (Friday–Sunday)
    H3  Celebration Plus
    H3  Wedding & Debut Premium
H2  How Much Does a Banquet Hall in San Jose Cost?
H2  Venue Features: Stage, Dance Floor, Full Bar & 100+ Gated Parking
H2  Take the 360° Virtual Tour
H2  Download the 2026 Pricing & Floor Plan Brochure
H2  Frequently Asked Questions About Crown Prince Event Hall
H2  Visit Us: 1654 Burdette Dr, San Jose, CA 95121
```

**`/weddings/`**
```
H1  Wedding Venue in San Jose, CA for Up to 300 Guests
H2  Why Couples Choose Crown Prince Event Hall
H2  Wedding & Debut Premium Package: What's Included
    H3  Red-Carpet Grand Entrance
    H3  Bridal & VIP Prep Room
    H3  6-Hour Event Window Plus 2 Hours of Setup
H2  Wedding Add-Ons: DJ, Photobooth & Bar Packages
H2  How Much Does a Wedding Venue in San Jose Cost?
H2  Wedding FAQs
H2  Book a Private Wedding Tour
```

**`/quinceaneras/`**
```
H1  Quinceañera Venue in San Jose, CA (Salón para Quinceañeras)
H2  A Grand Entrance for Her Big Day
H2  Quinceañera Package: What's Included
    H3  Stage & Dance Floor for the Vals and Baile Sorpresa
    H3  Seating for Up to 300 Family and Friends
    H3  Bar Packages, with Outside Catering Welcome
H2  Quinceañera Add-Ons: DJ, Photobooth & Marquee Numbers
H2  Quinceañera FAQs
H2  Reserve Your Date
```

**`/corporate-events/`**
```
H1  Corporate Event Venue in San Jose for Meetings, Banquets & Mixers
H2  Built for Presentations: Stage, Sound & Big-Screen TVs
H2  Weekday Flex: Hourly Rates for Monday–Thursday Events
H2  Corporate Events We Host
    H3  Holiday Parties & Award Banquets
    H3  Product Launches & Networking Mixers
    H3  Trainings, Town Halls & Community Events
H2  Parking & Accessibility: 100+ Gated Spaces
H2  Request a Corporate Quote
```

**`/parties/`**
```
H1  Birthday, Anniversary & Graduation Party Venue in San Jose
H2  Celebration Plus Package: The Extras Handled
    H3  Gold Chiavari Seating, Big-Screen TVs & Dance Floor
    H3  Chafers, Table Runners & Marquee Numbers
H2  Party Add-Ons: DJ, Photobooth & Bar Packages
H2  Party FAQs
H2  Book a Tour
```

**`/pricing/`**
```
H1  Banquet Hall Pricing & Packages in San Jose
H2  How Much Does Crown Prince Event Hall Cost?
H2  Compare Packages
    H3  Weekday Flex
    H3  Weekend Essentials
    H3  Celebration Plus
    H3  Wedding & Debut Premium
H2  Popular Add-Ons & Pricing
H2  Deposits, Payments & Our 90-Day Refund Policy
H2  Download the 2026 Pricing & Floor Plan Brochure
```

## Snippet C — AI Overview answer blocks

Paste each paragraph directly under its H2, before any images or bullets. Replace bracketed figures with real numbers; do not publish the block with placeholders.

**Under H2 "How Much Does a Banquet Hall in San Jose Cost?"** (homepage and `/pricing/`)

> Banquet halls in San Jose typically cost $3,500 to $8,000 for a full weekend event rental, with weekday hourly rates from about $300 to $800 per hour and luxury venues running $8,000 to $20,000. Crown Prince Event Hall offers Weekday Flex from [$XXX per hour] and Weekend Essentials from [$X,XXX], including a 6-hour event window, 2 hours of setup, Gold Chiavari seating and 100+ gated parking spaces for up to 300 guests. All fees are stated up front and standard quotes are returned the same day.

**Under H2 "What's Included in Every Crown Prince Event Hall Package?"**

> Every weekend package at Crown Prince Event Hall includes a 6-hour event window, 2 hours of complimentary setup, 8 hours of on-site event attendants, Gold Chiavari chairs and tables, big-screen TVs, the stage, the dance floor and access to the full bar. Weekday Flex is billed hourly Monday through Thursday. Optional add-ons include a DJ, digital photobooth, bridal or VIP prep room, VIP grand entrance, bar packages, chafers, table runners and marquee numbers.

**Under H2 "How Many Guests Can Crown Prince Event Hall Hold?"** (or the Venue Features H2)

> Crown Prince Event Hall seats up to 300 guests in a 4,100 sq ft hall in San Jose, CA. The room can be set for banquet, theater or reception layouts around a permanent stage and dance floor. Guests park in a private gated lot with more than 100 spaces, with free street parking nearby and valet available for formal arrivals.

## Snippet D — FAQ section copy and FAQPage schema

Place the visible FAQ on the homepage above the footer, wrapped in `<section id="faq">`, with each question as an H3 under the H2 "Frequently Asked Questions About Crown Prince Event Hall". The schema text must match the visible text.

**Q: How many guests can Crown Prince Event Hall hold?**
Crown Prince Event Hall seats up to 300 guests in a 4,100 sq ft hall with a stage and dance floor. Gold Chiavari chairs and tables are included, and the floor plan can be arranged for banquet, theater or reception layouts.

**Q: What is included in a Crown Prince Event Hall package?**
Weekend packages include a 6-hour event window, 2 hours of complimentary setup, 8 hours of on-site event attendants, Gold Chiavari chairs and tables, big-screen TVs, the stage and dance floor, and access to the full bar. Weekday Flex is billed hourly Monday through Thursday. Add-ons include DJ, digital photobooth, bridal/VIP prep room, VIP grand entrance, bar packages, chafers, table runners and marquee numbers.

**Q: Can I bring my own caterer or alcohol to Crown Prince Event Hall?**
Outside catering is welcome with venue approval. Alcohol is served through the venue's bar packages only; outside alcohol is not permitted. The hall is all-ages and non-smoking indoors.

**Q: Is there parking at Crown Prince Event Hall in San Jose?**
Yes. The venue has a private gated lot with more than 100 spaces, plus free street parking nearby. Valet service can be added for weddings and formal arrivals.

**Q: What is Crown Prince Event Hall's cancellation and refund policy?**
Crown Prince Event Hall offers a clear 90-day refund policy: bookings cancelled at least 90 days before the event date are refunded per the written agreement. All fees are stated up front on your quote, and standard events receive a tailored quote the same day.

Schema: see `schema/faq.jsonld` (paste the whole `<script>` block into `<head>`). Note: since 2023 Google shows FAQ rich results only for government and health sites, so do not expect the dropdown in results. The markup still feeds AI Overviews and entity understanding, which is why it stays in the plan.

## Snippet E — LocalBusiness / EventVenue JSON-LD

See `schema/local-business.jsonld`. Paste into `<head>` on every page. Replace every `REPLACE` value (email, image URLs, coordinates, social URLs, package prices, accessibility flag) and confirm the `openingHoursSpecification` matches Google Business Profile exactly. Validate at https://validator.schema.org/ and https://search.google.com/test/rich-results.

## Snippet F — Connect, Convert, Close: the brochure section

**Critique of the current CTAs.** The indexed copy pushes three actions with equal weight: book a private tour, take the 360° tour, and get a same-day quote. A tour is a high-commitment ask that suits the 10–15% of visitors who are comparing finalists. The 360° tour is engagement, not conversion, and gives you no contact record. The same-day quote requires the visitor to compose a message. There is nothing for the majority who are still researching and want a price range and a floor plan they can share with a spouse, a parent, or a planning committee. Those visitors leave and come back through a directory that charges you for the lead.

**Recommended hierarchy**

1. Primary (every page, hero and sticky mobile bar): "Get 2026 Pricing & Floor Plan" → opens the brochure form.
2. Secondary: "Book a Private Tour" → form that collects date, guest count and event type so the sales team qualifies before the visit.
3. Tertiary (text link, not a button): "Take the 360° Tour".
4. Header, mobile: click-to-call `<a href="tel:+14084081654">(408) 408-1654</a>`.

**Section copy** (place after the packages section on the homepage, and as the closing section on `/pricing/`; repeat a one-line version in the footer)

```
H2   Download the 2026 Pricing & Floor Plan Brochure
Sub  Every package, every add-on and the full 4,100 sq ft floor plan, in one PDF you can share with family or your team.

What's inside
• 2026 package pricing for Weekday Flex, Weekend Essentials, Celebration Plus and Wedding & Debut Premium
• Scaled floor plan with banquet, theater and reception layouts for 100, 200 and 300 guests
• Add-on price list: DJ, photobooth, bar packages, valet, VIP prep room
• Deposit schedule and the 90-day refund policy in plain language
• Preferred caterer list and outside-catering approval checklist

Form fields (keep to six)
  First name* · Email* · Mobile* · Event type (dropdown: Wedding / Quinceañera / Corporate / Birthday or Anniversary / Other)* · Event date (or "not sure yet") · Estimated guest count (dropdown: under 100 / 100–200 / 200–300)

Button   Send Me the Brochure
Under    Delivered instantly by email. No spam, and we never share your details.
Trust    ★★★★★ "…" — [client name], [event type], [month year]   ·   90-day refund policy   ·   Same-day quotes
```

**Layout.** Two columns on desktop, stacked on mobile. Left: headline, "what's inside" list, and a photo or mockup of the brochure cover showing the floor plan. Right: the form on a slightly raised panel with the button full-width. Below both: one row of three trust items. On mobile, a sticky bottom bar with "Get Pricing" and a phone icon.

**Close sequence** (automation after submit)
- Instant: email with the PDF, plus a one-click "Book a private tour" link and the direct phone number.
- Day 1: text message: "Hi [name], this is [owner] at Crown Prince Event Hall. Did the brochure answer your questions about [event type]? Happy to hold [date] for 48 hours while you decide."
- Day 3: email: "How our 90-day refund policy protects your date" plus two recent event photos of the same event type.
- Day 7: last touch: "Dates in [month] are filling; reply with your guest count for a same-day quote."

Track brochure downloads as a conversion in Google Analytics 4 and Google Ads so paid traffic can be optimized to it.

## Snippet G — Google Business Profile

**Business name (exact, everywhere):** Crown Prince Event Hall

**Primary category:** Banquet hall
**Secondary categories (add all that apply):** Event venue · Wedding venue · Reception hall (where offered) · Party planner (only if you sell planning as a service) · Corporate event venue (if available in your region's list) · Function room facility

**Description (746 characters):**

Crown Prince Event Hall is a 4,100 sq ft banquet hall and event venue in San Jose, CA, for weddings, quinceañeras, debuts, birthdays, graduations and corporate events for up to 300 guests. The hall is event-ready with a stage, dance floor, red-carpet entrance, full bar, Gold Chiavari chairs and big-screen TVs, plus a private gated lot with 100+ parking spaces and valet on request. Choose Weekday Flex hourly rentals, Weekend Essentials, Celebration Plus or Wedding/Debut Premium packages with a 6-hour event window and 2 hours of setup. Outside catering is welcome with approval. Take the 360° virtual tour, book a private tour and get a same-day quote with all fees stated up front. Serving San Jose, Santa Clara, Milpitas and the South Bay.

**Services (GBP "Services" tab, one per line):**
- Wedding venue rental
- Wedding reception hall
- Quinceañera venue rental
- Debut and sweet 16 venue
- Birthday party venue
- Anniversary party venue
- Graduation party venue
- Corporate event venue
- Holiday party venue
- Award banquet and gala venue
- Meeting and presentation space
- Community and church event rental
- Weekday hourly hall rental
- Bar packages (full bar)
- DJ and sound services
- Digital photobooth rental
- Valet parking
- Event planning support

**Attributes / amenities (GBP "About" and "Amenities"):**
- Capacity: up to 300 guests
- 4,100 sq ft hall
- Stage and dance floor
- Full bar (in-house bar packages only)
- Red-carpet entrance
- Gold Chiavari chairs and tables included
- Big-screen TVs and sound system
- Bridal / VIP prep room
- Private gated parking lot, 100+ spaces
- Free street parking
- Valet available
- Outside catering welcome with approval
- All ages welcome
- Non-smoking indoors
- Security cameras on site
- Wheelchair accessible entrance and restroom (confirm before checking)
- 360° virtual tour available
- Same-day quotes; 90-day refund policy

**Hours:** set to the hours someone answers the phone (for example, Mon–Sun 9:00 AM – 9:00 PM), not "Open 24 hours". Match Yelp and the schema to this exactly.

**Posts cadence:** one GBP post per week alternating event type (wedding, quinceañera, corporate, birthday), each with a photo, the event type, the city and a "Get 2026 pricing" link.
