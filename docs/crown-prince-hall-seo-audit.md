# Crown Prince Event Hall — SEO Audit & Optimization Action Plan

**Site:** https://crownprincehall.com
**Business:** Event venue / banquet hall, 1654 Burdette Dr, San Jose, CA 95121
**Audiences:** Weddings, quinceañeras, corporate events, milestone parties (birthdays, anniversaries, debuts, graduations)
**Market:** San Jose / Silicon Valley / Bay Area
**Prepared:** September 2026

---

## 0. How this audit was done, and what to double-check

The audit environment could not load the website or Yelp directly (the outbound network policy blocks both domains). The on-page findings are built from two sources: what Google's index shows for the site (title tag, meta description, indexed URLs) and the **full homepage copy supplied by the venue** (navigation, every section heading, the included-items list, packages, FAQ questions, form fields, house notes and footer). Local-listing findings (hours, categories, same-address listings) come from Yelp and directory snapshots and are marked accordingly. What could **not** be checked is listed at the end (Section 7) with a short checklist to close the gaps.

Fields marked **VERIFY** are values taken from third-party listings or left as placeholders. Confirm them before pasting.

> **Pricing policy conflict — read before Section 2 and Section 4.**
> The marketing playbook in this repo (`docs/events-venue-marketing-playbook.md`) sets a standing rule: *no venue or package prices on the website, in ads, or in the brochure; custom quote only.* This request asks for a "How much does a banquet hall in San Jose cost?" answer block and a "2026 Pricing & Floor Plan Brochure." Both are delivered as requested, **and** each comes with a no-price variant that captures the same search demand without publishing a Crown Prince rate. Decide which variant to ship; do not ship both.

---

## 1. What Google currently shows for the site

| Item | Current state (as indexed) | Verdict |
|---|---|---|
| Title tag | `Crown Prince Event Hall — San José Event & Banquet Venue` (56 chars) | OK length, but the money keyword "banquet hall San Jose" is not present as a phrase, and "San José" (accented) is used instead of the form people type. |
| Meta description | Starts "Crown Prince Event Hall is a 4,100 sq ft event-ready venue in San José for weddings, quinceañeras, debuts, birthdays, graduations, and corporate celebrations — up to 300 guests, with stage, dance floor, full bar, 360° virtual tour, and 100+ gated parking." | ~250 characters. Google truncates at roughly 155–160. The strongest hooks (300 guests, parking) get cut on mobile. |
| Indexed pages | Only the homepage appears for `site:crownprincehall.com` | Confirmed: the site is **one page** with anchor sections (`#venue`, `#events`, `#included`, `#gallery`, `#faq`, `#inquiry`). There is **no dedicated URL** to rank for "wedding venue San Jose," "quinceañera venue San Jose," "debut venue San Jose" or "corporate event venue San Jose." This is the single largest organic gap. |
| H1 / hero | "A grand stage for life's celebrations" | Beautiful, but keyword-free. Google reads the H1 as the page topic. Keep the line as the sub-headline; put the keyword in the H1 (§2.1). |
| Section headings | "Celebrations We Host," "The Venue," "Event-Ready, Built In," "Packages," "Word of Mouth," "Good to Know," "Check Your Date" | Every H2 is a label, not a query. None contains "San Jose," "banquet hall," "venue" or an event type. §2.1 maps each one to a keyword-bearing replacement that keeps the voice. |
| Square footage | Hero says "4,000+" and "Over 4,000"; the reviews section says "4,100" | Pick one figure (4,100) and use it everywhere, including schema and GBP. Inconsistent facts weaken entity confidence. |
| FAQ | Eight questions already on the page (catering, alcohol, vendors, setup time, parking, family-friendly, smoking, exact price) | Good content with **no FAQPage schema**, so it earns no rich result. §4.5 supplies schema for the existing eight questions. |
| Reviews on site | "Be among the first to celebrate here" with an empty five-star block | An empty star row can read as a rating of zero to a skimming visitor. Replace with the review program in §6.7 and remove the stars until real ones exist. |
| Structured data | None visible in search features (no FAQ rich result, no sitelinks, no business rich data) | No JSON-LD detected in the index snapshot. Section 3 supplies it. |
| Brand name | "Crown Prince Event Hall" (site, Yelp) vs "Crown Prince Hall" (domain, in-copy) | Pick one legal/display name and use it identically on the site, GBP, Yelp, and every directory. Recommendation: **Crown Prince Event Hall** (matches Yelp and the indexed title). |
| Phone | 408-408-1654, verified on the site header, footer and form (tap-to-call) | Consistent. Use the same format on GBP and Yelp. Add call tracking only via a GBP-safe method (a tracking number as primary on GBP with the real number as "additional"). |
| Hours | Site says "tours available seven days a week" with no hours; Yelp shows **"Open 24 hours, 7 days"** | No hours on the site and 24-hour hours on Yelp is the worst combination for trust. Publish real inquiry/tour hours on the site footer, in schema (§3) and on GBP (§6.4). |
| Yelp categories | Venues & Event Spaces, Wedding Planning, **Country Dance Halls** | "Country Dance Halls" is a mis-category. Remove it. It dilutes relevance and attracts the wrong searches. |
| Same-address listings | "The Nobel Venue" is also listed at 1654 Burdette Dr (Yelp) | If this is a former name or a prior tenant, request a merge/closure on Google and Yelp. Two venue listings at one address split reviews and confuse the map pack. |
| Reviews | Yelp listing is new with few reviews | Reviews are the #1 map-pack ranking factor after proximity. See High-priority row in Section 1a. |

### 1a. Prioritized action table

| Priority | Action | Why it matters | Where |
|---|---|---|---|
| **HIGH** | Create four dedicated, indexable pages: `/weddings`, `/quinceaneras`, `/corporate-events`, `/parties` (birthdays, anniversaries, graduations, debuts) | Google will not rank a single homepage for four different intents. Each page owns one keyword family. | §2 |
| **HIGH** | Replace homepage title and meta description with the versions in §2 | The description is being truncated and the title lacks the primary phrase. Immediate CTR gain. | §2 |
| **HIGH** | Add `EventVenue` + `LocalBusiness` JSON-LD sitewide and `FAQPage` JSON-LD on the FAQ page/section | Feeds the Knowledge Panel, map pack, and AI Overviews with capacity, address, hours, amenities. | §3, §4 |
| **HIGH** | Fix Google Business Profile: correct hours (not 24h), one canonical name, primary category "Banquet hall," remove "Country dance hall," add services and attributes | GBP drives most venue leads. Wrong hours and categories suppress ranking. | §6 |
| **HIGH** | Resolve the "The Nobel Venue" listing at the same address (merge, close, or mark as previous name) | Duplicate venue at one address splits authority and reviews. | §6 |
| **HIGH** | Launch a review program: ask every completed event within 48 hours, target 5+ Google reviews per month, reply to all | Newest venue on the block with few reviews cannot win the map pack on proximity alone. | §6 |
| **MEDIUM** | Add the three AI Overview answer blocks under H2 headers (cost, what's included, capacity) | Captures zero-click and AI-answer traffic for the questions people actually ask. | §4 |
| **MEDIUM** | Build the brochure landing section with a 6-field form, tap-to-call, and GA4 `generate_lead` event | Current CTA choice is split between tour and contact; a single "get the brochure" micro-conversion converts colder traffic. | §5 |
| **MEDIUM** | Add FAQPage JSON-LD to the eight FAQ questions already on the page | The content exists; the schema is what earns the rich result and AI Overview eligibility. | §4 |
| **MEDIUM** | Quick win before any rebuild: rename the existing section headings and the H1 on the one-page site | Zero design work, same voice, and every H2 starts carrying a query. | §2.1 |
| **MEDIUM** | Rename the five CTA labels that all lead to the same quote form; make "Book a Tour" actually book a tour | The most visible button on the site promises something it does not do. | §5.1 |
| **MEDIUM** | Publish an XML sitemap, submit it in Google Search Console, and confirm each new page has a self-referencing canonical | Only one URL is indexed today; new pages need a clean path in. | §7 |
| **MEDIUM** | Use "San Jose" (no accent) in titles, meta descriptions, H1s and URLs; keep "San José" in body copy if it is brand style | Exact-match of the typed query in the title and H1 is still a relevance signal. | §2 |
| **LOW** | Add `sameAs` links (Instagram, Facebook, Yelp, The Knot, WeddingWire, Eventective) to the JSON-LD and to the footer | Entity confirmation for Google; also cheap referral traffic. | §3 |
| **LOW** | Image alt text on every gallery photo in the pattern "[event type] at Crown Prince Event Hall, San Jose" | Google Images is a real discovery channel for venues. | §7 |
| **LOW** | Bilingual (Spanish) quinceañera page or section: "Salón para quinceañeras en San José" | East San Jose search demand for quince venues is heavily Spanish-language. | §2 |
| **LOW** | Give "Weekday Flex" (Monday–Thursday hourly) its own H2 and, later, its own page: "Hourly Event Space Rental in San Jose" | Hourly weekday rental is a distinct, low-competition query set (meetings, rehearsals, community groups) and fills the calendar's emptiest days. | §2.1 |
| **LOW** | Add "Debut & Sweet 16" wording to the parties page and schema | The site already lists debuts; "debut venue San Jose" is a specific, under-served Filipino-community query. | §2.5, §3 |
| **LOW** | Add neighborhood and landmark mentions in body copy (East San Jose, Evergreen, Tully Rd, near Hwy 101/680, 15 min from downtown San Jose) | Local relevance for "near me" and neighborhood-modified queries. | §2 |

---

## 2. On-Page SEO — Title Tags, Meta Descriptions, Heading Structure

All titles are under 60 characters; all meta descriptions are under 160. Lengths were checked by script.

### 2.1 Homepage — `/`

**Title (54 chars)**
```
Banquet Hall in San Jose, CA | Crown Prince Event Hall
```

**Meta description (154 chars)**
```
Crown Prince Event Hall: 4,100 sq ft San Jose banquet hall for up to 300 guests. Stage, dance floor, full bar, 100+ gated parking. Book a free tour today.
```

**Heading structure — recommended for the current one-page site (rename in place, keep the sub-lines)**

| Section | Current heading | Recommended heading |
|---|---|---|
| Hero | H1 "A grand stage for life's celebrations" | **H1** San Jose Banquet Hall & Event Venue for Up to 300 Guests<br>*sub-line:* A grand stage for life's celebrations |
| #events | "Celebrations We Host" | **H2** Weddings, Quinceañeras, Debuts & Corporate Events in San Jose<br>H3 Weddings · H3 Quinceañeras · H3 Debuts & Sweet 16 · H3 Birthdays & Anniversaries · H3 Graduations · H3 Corporate & Community · H3 Concerts & Productions |
| #venue | "The Venue" | **H2** The Venue: 4,100 Sq Ft, Stage, Dance Floor & Full Bar |
| #included | "Event-Ready, Built In" | **H2** What's Included in Every Weekend Package |
| Packages | "Packages" | **H2** Event Packages for San Jose Weddings, Parties & Corporate Events<br>H3 per package (Weekend Essentials, Wedding / Debut Premium, Celebration Plus, Corporate & Community, Concert / Production, Weekday Flex) |
| Parking | "Parking & Location" | **H2** Parking & Location in East San Jose (100+ Gated Spaces) |
| Reviews | "Word of Mouth" | **H2** Reviews from San Jose Celebrations *(publish when the first three exist; hide until then)* |
| #faq | "Good to Know" | **H2** Frequently Asked Questions About Crown Prince Event Hall |
| #inquiry | "Check Your Date" | **H2** Check Your Date & Get a Same-Day Quote |
| New | — | **H2** How Much Does a Banquet Hall in San Jose Cost? (§4.1) |
| New | — | **H2** Download the 2026 Pricing & Floor Plan Brochure (§5.2) |

**Heading structure — target once the event pages exist**
```
H1  San Jose Banquet Hall & Event Venue for Up to 300 Guests
  H2  Weddings, Quinceañeras, Debuts & Corporate Events in San Jose
    H3  Weddings            → /weddings
    H3  Quinceañeras        → /quinceaneras
    H3  Corporate & Community Events → /corporate-events
    H3  Birthdays, Debuts, Graduations & Milestone Parties → /parties
  H2  What's Included in Every Weekend Package
  H2  Capacity, Layouts & Floor Plans
    H3  Banquet seating (up to 300)
    H3  Ceremony + reception layout
    H3  Stage & dance-floor layout
  H2  Event Packages
  H2  Parking & Location in East San Jose
  H2  How Much Does a Banquet Hall in San Jose Cost?
  H2  Download the 2026 Pricing & Floor Plan Brochure
  H2  Frequently Asked Questions About Crown Prince Event Hall
  H2  Check Your Date & Get a Same-Day Quote
```

### 2.2 Weddings — `/weddings`

**Title (57 chars)**
```
San Jose Wedding Venue for 300 Guests | Crown Prince Hall
```

**Meta description (156 chars)**
```
Ceremony and reception under one roof in San Jose. Stage, dance floor, full bar, AV engineer, VIP grand entrance, 100+ gated parking. Get the wedding brochure.
```

**Heading structure**
```
H1  Wedding Venue in San Jose, CA — Ceremony & Reception in One Hall
  H2  Why Couples Choose Crown Prince Event Hall
  H2  Wedding Layouts & Capacity
    H3  Ceremony seating
    H3  Reception with dance floor (up to 300)
    H3  Bridal / VIP prep room (Wedding / Debut Premium)
  H2  What's Included in a Wedding Booking
  H2  Catering, Bar & Vendor Policy
  H2  Wedding Gallery & 360° Virtual Tour
  H2  Wedding FAQ
  H2  Get the 2026 Wedding Pricing & Floor Plan Brochure
```

### 2.3 Quinceañeras — `/quinceaneras`

**Title (53 chars)**
```
Quinceañera Venue in San Jose, CA | Crown Prince Hall
```

**Meta description (150 chars)**
```
Salón para quinceañeras in San Jose: room for the court, the waltz and 300 guests. Stage, DJ lights, full bar, gated parking. Tour the hall this week.
```

**Heading structure**
```
H1  Quinceañera Venue in San Jose — Salón para Quinceañeras
  H2  Room for the Court, the Waltz, and 300 Guests
  H2  Lighting, Stage & Grand Entrance
  H2  What's Included in a Quinceañera Package
  H2  Catering, Cake & Vendor Options
  H2  Quinceañera Gallery
  H2  Preguntas Frecuentes / Quinceañera FAQ
  H2  Get the Quinceañera Brochure & Floor Plan
```

### 2.4 Corporate Events — `/corporate-events`

**Title (53 chars)**
```
Corporate Event Venue in San Jose | Crown Prince Hall
```

**Meta description (156 chars)**
```
Silicon Valley corporate event space for banquets, mixers, launches and team events. Stage, AV, big-screen TVs, 100+ parking, up to 300 guests. Get a quote.
```

**Heading structure**
```
H1  Corporate Event Venue in San Jose & Silicon Valley
  H2  Built for Banquets, Mixers, Launches & Town Halls
  H2  AV, Stage & Presentation Setup
    H3  Big-screen TVs & sound system
    H3  Stage & podium
    H3  Lighting options
  H2  Capacity & Layouts for Corporate Events
  H2  Parking & Access for Attendees
  H2  Corporate Event FAQ
  H2  Request the Corporate Event Guide & Floor Plan
```

### 2.5 Parties & Milestones — `/parties`

**Title (58 chars)**
```
Birthday & Party Venue in San Jose, CA | Crown Prince Hall
```

**Meta description (156 chars)**
```
Birthday, anniversary, graduation and debut party venue in San Jose for 50 to 300 guests. Dance floor, DJ lights, full bar, gated parking. Book a free tour.
```

**Heading structure**
```
H1  Birthday, Anniversary & Milestone Party Venue in San Jose
  H2  Parties We Host
    H3  Milestone birthdays (18th, 21st, 30th, 40th, 50th, 60th)
    H3  Anniversaries & vow renewals
    H3  Graduations & debuts
    H3  Baby showers & gender reveals
  H2  Layouts for 50 to 300 Guests
  H2  What's Included
  H2  Party Gallery
  H2  Party FAQ
  H2  Get the Party Brochure & Floor Plan
```

### 2.6 Brochure / Pricing landing page — `/pricing-brochure`

**Title (52 chars)**
```
2026 Pricing & Floor Plans | Crown Prince Event Hall
```
*No-price variant (50 chars):* `2026 Event Guide & Floor Plans | Crown Prince Hall`

**Meta description (152 chars)**
```
Download the 2026 Crown Prince Event Hall brochure: floor plans, capacities, what's included, bar packages and pricing for San Jose weddings and events.
```
*No-price variant (155 chars):* `Download the 2026 Crown Prince Event Hall guide: floor plans, capacities, what's included, bar packages and vendor policy for San Jose weddings and events.`

### 2.7 Tour / Contact — `/book-a-tour`

**Title (55 chars)**
```
Book a Venue Tour in San Jose | Crown Prince Event Hall
```

**Meta description (153 chars)**
```
See the hall in person. Book a free 30-minute venue tour at Crown Prince Event Hall, 1654 Burdette Dr, San Jose. Open 7 days. Call or pick a time online.
```

### 2.8 FAQ — `/faq` (or an on-page section on every page)

**Title (58 chars)**
```
Venue FAQ: Capacity, Parking, Catering | Crown Prince Hall
```

**Meta description (151 chars)**
```
Answers to the questions San Jose couples and planners ask most: guest capacity, parking, catering and bar rules, hours, deposits and what is included.
```

### 2.9 Global on-page rules

- One H1 per page, containing the page's primary keyword and "San Jose."
- Self-referencing `<link rel="canonical">` on every page; `https://crownprincehall.com/` (with trailing slash, https, no www) as the canonical form. Redirect all variants.
- `<html lang="en">` and, if the quinceañera page carries Spanish sections, add `hreflang` only if you build a full `/es/` version. Otherwise leave it.
- Every page ends with the same brochure block (§5) and the same NAP footer (name, address, phone as `tel:` link, hours).
- Internal links: the homepage H3 cards link to the four event pages; each event page links to the other three and to the brochure page.

---

## 3. Local SEO — JSON-LD `EventVenue` / `LocalBusiness` Schema

Paste once, in the `<head>` (or just before `</body>`) of **every** page. Fill the **VERIFY** fields.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["EventVenue", "LocalBusiness"],
  "@id": "https://crownprincehall.com/#venue",
  "name": "Crown Prince Event Hall",
  "alternateName": "Crown Prince Hall",
  "description": "Crown Prince Event Hall is a 4,100 sq ft banquet hall and event venue in San Jose, CA for weddings, quinceañeras, debuts, corporate events, birthdays and milestone celebrations for up to 300 guests, with a stage, dance floor, full bar, on-site AV engineer and 100+ gated parking spaces.",
  "url": "https://crownprincehall.com/",
  "telephone": "+1-408-408-1654",
  "email": "VERIFY@crownprincehall.com",
  "image": [
    "https://crownprincehall.com/images/hall-banquet-setup.jpg",
    "https://crownprincehall.com/images/hall-stage-dance-floor.jpg",
    "https://crownprincehall.com/images/hall-entrance.jpg"
  ],
  "logo": "https://crownprincehall.com/images/logo.png",
  "priceRange": "$$$",
  "currenciesAccepted": "USD",
  "paymentAccepted": "Cash, Credit Card, Debit Card, Zelle, Bank Transfer",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "1654 Burdette Dr",
    "addressLocality": "San Jose",
    "addressRegion": "CA",
    "postalCode": "95121",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "VERIFY (copy from Google Business Profile map pin)",
    "longitude": "VERIFY (copy from Google Business Profile map pin)"
  },
  "hasMap": "https://www.google.com/maps/search/?api=1&query=Crown+Prince+Event+Hall+1654+Burdette+Dr+San+Jose+CA+95121",
  "areaServed": [
    { "@type": "City", "name": "San Jose" },
    { "@type": "City", "name": "Santa Clara" },
    { "@type": "City", "name": "Milpitas" },
    { "@type": "City", "name": "Fremont" },
    { "@type": "City", "name": "Sunnyvale" },
    { "@type": "City", "name": "Morgan Hill" },
    { "@type": "City", "name": "Gilroy" },
    { "@type": "AdministrativeArea", "name": "Santa Clara County" },
    { "@type": "AdministrativeArea", "name": "San Francisco Bay Area" }
  ],
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "10:00",
      "closes": "19:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Saturday", "Sunday"],
      "opens": "10:00",
      "closes": "17:00"
    }
  ],
  "maximumAttendeeCapacity": 300,
  "floorSize": {
    "@type": "QuantitativeValue",
    "value": 4100,
    "unitCode": "FTK",
    "unitText": "square feet"
  },
  "isAccessibleForFree": false,
  "publicAccess": false,
  "smokingAllowed": false,
  "amenityFeature": [
    { "@type": "LocationFeatureSpecification", "name": "Gated private parking lot (100+ spaces)", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Valet parking available", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Stage", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Dance floor", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Full bar with bar packages", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Bridal / VIP prep room (add-on)", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "On-site AV engineer and event attendants", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Refrigerator and deep freezer for caterers", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Black or white tablecloths included", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Sound system and microphones", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Big-screen TVs for presentations", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "DJ lights and uplighting", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Gold Chiavari chairs and banquet tables", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Red carpet entrance", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Outside catering allowed with approval", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Outside alcohol allowed", "value": false },
    { "@type": "LocationFeatureSpecification", "name": "All ages welcome", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Wheelchair accessible", "value": "VERIFY" }
  ],
  "makesOffer": [
    { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Wedding venue rental", "areaServed": "San Jose, CA" } },
    { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Quinceañera venue rental", "areaServed": "San Jose, CA" } },
    { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Corporate event space rental", "areaServed": "San Jose, CA" } },
    { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Birthday and milestone party venue rental", "areaServed": "San Jose, CA" } },
    { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Debut and Sweet 16 venue rental", "areaServed": "San Jose, CA" } },
    { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Concert and stage production venue rental", "areaServed": "San Jose, CA" } },
    { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Weekday hourly event space rental (Monday to Thursday)", "areaServed": "San Jose, CA" } },
    { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Bar packages and bartending", "areaServed": "San Jose, CA" } }
  ],
  "sameAs": [
    "https://www.yelp.com/biz/crown-prince-event-hall-san-jose",
    "VERIFY https://www.instagram.com/…",
    "VERIFY https://www.facebook.com/…",
    "VERIFY https://www.theknot.com/marketplace/…",
    "VERIFY https://www.weddingwire.com/biz/…",
    "VERIFY https://www.eventective.com/san-jose-ca/…"
  ],
  "potentialAction": {
    "@type": "ReserveAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://crownprincehall.com/book-a-tour",
      "actionPlatform": ["http://schema.org/DesktopWebPlatform", "http://schema.org/MobileWebPlatform"]
    },
    "result": { "@type": "Reservation", "name": "Venue tour" }
  }
}
</script>
```

**Notes on the fields**
- `openingHoursSpecification` above is a *placeholder for inquiry/tour hours*. The current public listing says "Open 24 hours," which Google treats as a low-quality signal for a venue office. Publish the hours someone can actually reach you, and use the same hours in GBP.
- `priceRange`: Google accepts `$`–`$$$$`. `$$$` positions a 300-guest hall with a full bar correctly against San Jose competitors. This does **not** disclose a price, so it is compatible with the custom-quote rule.
- Remove any `sameAs` line you cannot fill; an empty or fake URL does more harm than a missing one.
- Validate at https://validator.schema.org and https://search.google.com/test/rich-results before publishing.

---

## 4. Google AI Overviews & Search Snippets

Each block goes **directly under the H2**, before any images or buttons. Keep the first sentence a direct answer; Google and AI Overviews lift the first 40–60 words.

### 4.1 H2: How Much Does a Banquet Hall in San Jose Cost?

**Version A — as requested (publishes a Crown Prince starting figure; fill VERIFY). Note the live site already says "every package is quoted transparently, with all fees stated up front" and "Request Pricing" on every package, so Version B below is the one that matches both the site and the playbook:**

> Banquet halls in San Jose typically cost between $2,500 and $12,000 for a full-day rental, and $65 to $150 per guest when catering and bar are bundled, depending on the day of the week, season, guest count and hours. Crown Prince Event Hall's 2026 venue rental starts at **$VERIFY** for up to 300 guests and includes the stage, dance floor, gold Chiavari chairs, banquet tables, sound system, lighting and 100+ gated parking spaces. Download the 2026 Pricing & Floor Plan Brochure for the full rate card.

(86 words)

**Version B — no-price variant (complies with the playbook rule):**

> Banquet halls in San Jose typically cost between $2,500 and $12,000 for a full-day rental, and $65 to $150 per guest when catering and bar are bundled, depending on the day, season, guest count and hours. Crown Prince Event Hall quotes each event individually so you only pay for the hours and setup you use. Every quote includes the stage, dance floor, Chiavari chairs, banquet tables, sound system, lighting and 100+ gated parking. Request a custom quote in under 24 hours.

(81 words)

*Market ranges are drawn from public 2026 San Jose venue listings (Tagvenue, Peerspace, Eventective). Refresh them each January.*

### 4.2 H2: What Is Included in Crown Prince Event Hall Packages?

> Every Crown Prince Event Hall weekend package includes a 6-hour event window plus 2 complimentary setup hours, event attendants for 8 hours, an on-site AV engineer, a large stage and open dance floor, gold or silver Chiavari chairs with banquet tables, black or white tablecloths, big-screen TVs, a sound system with microphone, DJ lights, uplights and house colored lighting, a refrigerator and deep freezer for your caterer, and a private gated lot with 100+ spaces. Bar packages, a bridal/VIP prep room, DJ, photobooth and VIP grand entrance are add-ons.

(89 words)

### 4.3 H2: How Many Guests Can Crown Prince Event Hall Hold?

> Crown Prince Event Hall seats up to 300 guests for a banquet with a dance floor and stage, and accommodates around 350 for a standing reception or cocktail-style corporate mixer (VERIFY standing figure with the fire-marshal occupancy; the site says final capacities depend on layout). The 4,100 sq ft floor can be set as a ceremony-plus-reception layout, a theater or classroom layout for presentations, or a full banquet with round tables of 8 to 10. Floor plans for each layout are in the free brochure.

(85 words)

### 4.4 FAQ Section — the eight questions already on the page, with paste-ready answers

The site already has the right questions under "Good to Know." Keep them, rename the H2 to "Frequently Asked Questions About Crown Prince Event Hall," and use these answers (each is a direct first sentence, then one or two supporting sentences, which is what AI Overviews lift). Where the live accordion text differs, either paste these answers in or edit the JSON-LD to match what is on the page; the two must be identical.

**H3: Can we bring our own catering?**
Yes. Outside catering is welcome at Crown Prince Event Hall with venue approval. Your caterer gets a refrigerator and deep freezer on site and two complimentary setup hours before doors open. Chafers and table runners are available as add-ons.

**H3: Can we bring our own alcohol?**
No. All alcohol is served through the venue's full bar under a structured bar package, with a bartender included, so the event stays licensed and insured. Choose your bar package when you request a quote.

**H3: Can we use our own vendors?**
Yes. Your own decorator, DJ, photographer, photobooth and caterer are welcome with approval (VERIFY any insurance requirement). Vendors load in during the two complimentary setup hours, and the house AV engineer connects your DJ or slideshow to the sound system and screens.

**H3: How much time do we get for setup?**
Weekend packages include a 6-hour event window plus 2 complimentary setup hours before doors open. Extra event or setup hours can be added to your quote. Weekday Flex bookings (Monday to Thursday) are scheduled by the hour.

**H3: Is there really enough parking?**
Yes. Crown Prince Event Hall has a private gated lot with more than 100 spaces, free onsite and street parking, and an optional valet service for formal arrivals. That covers a full 300-guest event without guests circling the block.

**H3: Is the venue family-friendly?**
Yes. All ages are welcome, including children at weddings, quinceañeras, debuts and graduations. The hall is one open level with a stage, dance floor and family-scale seating (VERIFY: add stroller/wheelchair access and changing-table details).

**H3: Is smoking allowed?**
No smoking indoors. (VERIFY: name the designated outdoor smoking area, if any.) Security cameras are in use for guest safety.

**H3: How do I get an exact price?**
Send your date, guest count, event type and bar or catering preference through the "Check Your Date" form or call or text 408-408-1654. Standard events receive a tailored quote the same day with every fee stated up front, and every inquiry gets a reply within one business hour.

### 4.5 FAQ JSON-LD (paste into the `<head>` of the homepage; one FAQPage per page only)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can we bring our own catering?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Outside catering is welcome at Crown Prince Event Hall with venue approval. Your caterer gets a refrigerator and deep freezer on site and two complimentary setup hours before doors open. Chafers and table runners are available as add-ons."
      }
    },
    {
      "@type": "Question",
      "name": "Can we bring our own alcohol?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. All alcohol is served through the venue's full bar under a structured bar package, with a bartender included, so the event stays licensed and insured. Choose your bar package when you request a quote."
      }
    },
    {
      "@type": "Question",
      "name": "Can we use our own vendors?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Your own decorator, DJ, photographer, photobooth and caterer are welcome with approval. Vendors load in during the two complimentary setup hours, and the house AV engineer connects your DJ or slideshow to the sound system and screens."
      }
    },
    {
      "@type": "Question",
      "name": "How much time do we get for setup?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Weekend packages include a 6-hour event window plus 2 complimentary setup hours before doors open. Extra event or setup hours can be added to your quote. Weekday Flex bookings (Monday to Thursday) are scheduled by the hour."
      }
    },
    {
      "@type": "Question",
      "name": "Is there really enough parking?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Crown Prince Event Hall has a private gated lot with more than 100 spaces, free onsite and street parking, and an optional valet service for formal arrivals. That covers a full 300-guest event without guests circling the block."
      }
    },
    {
      "@type": "Question",
      "name": "Is the venue family-friendly?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. All ages are welcome, including children at weddings, quinceañeras, debuts and graduations. The hall is one open level with a stage, dance floor and family-scale seating."
      }
    },
    {
      "@type": "Question",
      "name": "Is smoking allowed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No smoking indoors. Security cameras are in use for guest safety."
      }
    },
    {
      "@type": "Question",
      "name": "How do I get an exact price?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Send your date, guest count, event type and bar or catering preference through the Check Your Date form or call or text 408-408-1654. Standard events receive a tailored quote the same day with every fee stated up front, and every inquiry gets a reply within one business hour."
      }
    }
  ]
}
</script>
```

Rule: the JSON-LD answers must match the visible on-page text, or Google drops the rich result. The script above omits the VERIFY asides; once you settle those details on the page, add the same words to the script.

---

## 5. Micro-Transaction / Landing Page Conversion (Connect → Convert → Close)

### 5.1 Critique of the current calls to action

What the homepage actually does today:

| Button text | Where it appears | Where it goes |
|---|---|---|
| Book a Tour | Header nav | `#inquiry` (the quote form) |
| Book a Private Tour | Hero, reviews section | `#inquiry` |
| Inquire → | All seven event cards | `#inquiry` |
| Request Pricing | All six package cards | `#inquiry` |
| Request My Quote | The form's submit button | Submits the form |
| 360° Virtual Tour | Hero, venue section, tour section | Opens the virtual tour |

Five labels, one destination, and the destination is a quote form with seven required fields: name, phone, email, event type, preferred date (three dropdowns), guest count, and bar/catering choice.

1. **"Book a Tour" does not book a tour.** The most visible button on the site, in the header on every scroll, opens a form that asks for a preferred event date and a bar package. A visitor who clicked to see the space is now being asked to commit to a date. Either wire the button to a real tour scheduler (Google Business Profile bookings, Calendly or an appointment page with the seven-days-a-week hours) or rename it "Get a Quote."
2. **The only conversion is a full quote request.** That is the right ask for a warm visitor who already has a date. It is too much for the majority who typed "banquet hall San Jose" and are opening five tabs. There is no lower step, so they leave and you have nothing to follow up on.
3. **No exchange of value.** Every button asks for something; none offers something. Floor plans and a written "what's included" are the natural thing to trade for an email and phone number.
4. **The date field is three dropdowns.** Month, day and year selects are the slowest way to enter a date on a phone, and there is no "not sure yet" option even though most early-stage planners do not have one.
5. **"Request Pricing" on every package sets an expectation the site then declines.** The visitor expects a number; the form returns a promise of a same-day quote. The brochure section (§5.2) closes that gap honestly, and Version B does it without publishing a rate.
6. **Phone is present but not sticky.** It sits in the header and footer. On mobile, a fixed bottom bar with "Call or text" and "Get the brochure" turns scrollers into calls.
7. **What is already right, keep it:** the one-business-hour response promise, the same-day quote for standard events, the event-type and guest-count dropdowns (they pre-qualify the lead for free), the bar/catering question (it drives the quote), and the 360° tour as an engagement tool below the hero.

**Recommended CTA ladder (every page, in this order):**

| Position | CTA | Type | Who it converts |
|---|---|---|---|
| Header nav | **Get a Quote** (or a real tour scheduler labelled "Book a Tour") | Hard conversion | Warm visitors with a date |
| Hero, primary button | **Download the 2026 Pricing & Floor Plan Brochure** (no-price variant: "Get the 2026 Event Guide & Floor Plans") | Micro-conversion, 6-field form | Cold and warm traffic, typically 60–70 % of leads |
| Hero, secondary text link | **Check your date →** (existing quote form) | Hard conversion | Visitors ready to price a specific date |
| Event and package cards | **See floor plans & what's included** → brochure; **Get a quote** → form | Two labels that say what happens | Card-level intent |
| Sticky mobile bar | **Call or text 408-408-1654** · **Get brochure** | Tap-to-call + form | Mobile searchers |
| After gallery | **Take the 360° virtual tour** | Engagement | Time on page, confidence |
| Footer of every page | Brochure block repeated (§5.2) | Micro-conversion | Scrollers who read to the end |

**Fixes to the existing quote form (keep the form, tune it):**
- Replace the three date dropdowns with a single date picker plus a "Not sure yet" checkbox.
- Make "Bar & Catering" optional; keep it, it helps the quote, but do not let it block submission.
- Add an "Under 50" guest option so Weekday Flex inquiries (meetings, rehearsals) are not forced into the wrong bracket.
- Add hidden fields `utm_source`, `utm_medium`, `utm_campaign`, `landing_page`, `gclid`, and fire a GA4 `generate_lead` event on submit so each booking can be traced to what it cost to acquire.

### 5.2 Brochure section — copy and layout

**Placement:** directly below the hero on the homepage and every event page, and again as the last section before the footer. Section ID `#brochure` so every button can anchor-link to it.

**Layout (desktop: two columns 55/45; mobile: stacked, form second):**

```
┌──────────────────────────────────────────────────────────────────────┐
│  LEFT (55 %)                              │  RIGHT (45 %) — the form  │
│  Eyebrow: FREE DOWNLOAD · UPDATED FOR 2026│  Card with soft shadow    │
│  H2 headline                              │  6 fields (below)         │
│  2-sentence subhead                       │  Full-width button        │
│  Checklist (5 items, check icons)         │  Privacy microcopy        │
│  Brochure cover mockup (image, 3-page fan)│  "Response in 1 business  │
│  Trust strip: ★★★★★ Google · Yelp ·       │   hour" badge             │
│  "300 guests · 4,100 sq ft · 100+ parking"│                           │
└──────────────────────────────────────────────────────────────────────┘
```

**Copy — Version A (as requested, pricing included):**

> **Eyebrow:** FREE DOWNLOAD · UPDATED FOR 2026
>
> **H2:** Download the 2026 Pricing & Floor Plan Brochure
>
> **Subhead:** See exactly what a wedding, quinceañera or corporate event at Crown Prince Event Hall costs, what's included, and how 300 guests fit. It arrives in your inbox in under a minute.
>
> **Inside the brochure:**
> - ✓ 2026 rental rates and bar packages by day of week and season
> - ✓ Floor plans for banquet, ceremony + reception, stage and theater layouts
> - ✓ Capacity charts from 50 to 300 guests
> - ✓ What's included, add-ons, catering and vendor policy
> - ✓ Sample timelines and a booking checklist
>
> **Button:** Send Me the 2026 Brochure
>
> **Microcopy under button:** No spam, no obligation. We'll email the brochure and follow up once to see if you'd like a tour. Prefer to talk? Call (408) 408-1654.

**Copy — Version B (no published pricing; recommended under the playbook rule):**

> **Eyebrow:** FREE DOWNLOAD · UPDATED FOR 2026
>
> **H2:** Get the 2026 Event Guide & Floor Plans
>
> **Subhead:** See how 300 guests fit, what every booking includes, and what a Crown Prince event looks like from entrance to last dance. Then request a quote built for your date and guest count.
>
> **Inside the guide:**
> - ✓ Floor plans for banquet, ceremony + reception, stage and theater layouts
> - ✓ Capacity charts from 50 to 300 guests
> - ✓ Everything included in every booking, plus bar packages and add-ons
> - ✓ Catering, vendor and décor policy
> - ✓ Sample timelines, booking checklist and how quoting works
>
> **Button:** Send Me the Event Guide
>
> **Microcopy:** No spam, no obligation. We'll email the guide and reply within one business hour with availability for your date. Prefer to talk? Call (408) 408-1654.

**Form fields (6, in this order):**

| Field | Type | Required | Why |
|---|---|---|---|
| First name | text | yes | Personalized follow-up |
| Email | email | yes | Brochure delivery |
| Mobile phone | tel | yes | SMS + call follow-up; the fastest close channel |
| Event type | select: Wedding · Quinceañera · Corporate event · Birthday/anniversary · Graduation/debut · Other | yes | Routes the right brochure version and salesperson |
| Event date | date + "Not sure yet" checkbox | no | Qualification and urgency |
| Estimated guests | select: Under 100 · 100–200 · 200–300 · 300+ | no | Qualification; 300+ gets a polite redirect |

Hidden fields: `utm_source`, `utm_medium`, `utm_campaign`, `landing_page`, `gclid`. These are what let the accountant tie a booking back to what it cost to acquire.

**Button and thank-you flow:**
1. On submit, fire a GA4 event `generate_lead` with parameter `event_type` and mark it a conversion; import it into Google Ads.
2. Redirect to `/thank-you-brochure` (a distinct URL makes the conversion easy to count). Thank-you page copy: "Your brochure is on its way. Want to see the hall in person?" + embedded tour calendar + phone.
3. Within 60 seconds: email with the brochure attached, SMS "Thanks {first name}, your Crown Prince Event Hall brochure is on its way. Want to see the space? Pick a tour time: {link}."
4. A person calls within one business hour. The site already promises this; the promise should be visible next to the form.

### 5.3 Why this converts better than the quote form alone

The brochure captures the visitors who are not ready to name a date, gives you their event type and size at the moment they are most willing to share it, and turns the quote and the tour into the *second* and *third* steps, taken from the thank-you page or the follow-up text. Quote requests typically go **up**, not down, because they come from people who have already seen the floor plans and the included-items list.

---

## 6. Google Business Profile (GBP)

### 6.1 Business name

Use **Crown Prince Event Hall** — nothing else (no "San Jose," no "Banquet Hall" appended). Keyword-stuffed names violate GBP guidelines and get suspended. Make the site, Yelp, The Knot, WeddingWire and Eventective match this exactly.

### 6.2 Business description (731 characters, limit 750)

```
Crown Prince Event Hall is a 4,100 sq ft banquet hall and event venue in San Jose, CA for weddings, quinceañeras, debuts, corporate events, birthdays, anniversaries, graduations and concerts for up to 300 guests. Weekend packages arrive event-ready: a 6-hour event window plus 2 setup hours, event attendants, an on-site AV engineer, a large stage, open dance floor, Chiavari chairs, banquet tables, linens, big-screen TVs, sound system, DJ and uplighting, and a refrigerator and freezer for your caterer. Outside catering is welcome with approval; our full bar serves structured bar packages. Guests park in a private gated lot with 100+ spaces, valet available. Weekday hourly bookings Monday to Thursday. Book a free tour today.
```

### 6.3 Categories

| Slot | Category (exact GBP name) |
|---|---|
| **Primary** | Banquet hall |
| Secondary 1 | Event venue |
| Secondary 2 | Wedding venue |
| Secondary 3 | Party planner *(only if you actually coordinate; otherwise omit)* |
| Secondary 4 | Function room facility |
| Secondary 5 | Corporate entertainment service *(optional; helps "corporate event venue" queries)* |
| **Remove** | Country dance hall, Wedding planning (if present as a category rather than a service) |

Primary category is the strongest single GBP ranking lever. "Banquet hall" is the highest-volume venue category in San Jose and is what competitors that rank in the map pack use.

### 6.4 Hours (replace "Open 24 hours")

Office / tour hours, e.g. (VERIFY):
```
Monday–Friday   10:00 AM – 7:00 PM
Saturday–Sunday 10:00 AM – 5:00 PM
```
Add "More hours → Tours by appointment" if the profile supports it. Event hours (e.g. until 1:00 AM) belong in the description, not the hours field.

### 6.5 Services (paste as individual service items under each category)

**Under Banquet hall / Event venue**
- Wedding ceremony and reception venue
- Quinceañera venue (salón para quinceañeras)
- Corporate event and holiday party venue
- Birthday party venue
- Anniversary and vow renewal venue
- Graduation venue
- Debut and Sweet 16 venue
- Concert and stage production venue
- Weekday hourly event space rental (Monday to Thursday)
- Baby shower and gender reveal venue
- Cultural and community event venue
- Product launch and town-hall venue
- Full-bar service and bar packages
- Valet parking
- Venue tours (free, by appointment)
- 360° virtual venue tour

### 6.6 Attributes / amenities (tick everything that applies in GBP; mirror on Yelp)

- Capacity: up to 300 guests
- 4,100 sq ft event hall
- Private gated parking lot, 100+ spaces
- Free street parking
- Valet parking available
- Stage
- Dance floor
- Full bar
- Bridal / VIP prep room (add-on)
- On-site AV engineer and event attendants
- Refrigerator and deep freezer for caterers
- Black or white tablecloths included
- Sound system and microphones
- DJ lighting, uplighting and colored house lighting
- Big-screen TVs / presentation screens
- Gold Chiavari chairs and banquet tables included
- Red-carpet entrance
- Outside catering allowed with approval
- No outside alcohol; bar packages through the venue
- All ages welcome
- No smoking indoors
- Security cameras on premises
- Wheelchair-accessible entrance and restrooms (VERIFY)
- Wi-Fi (VERIFY)
- Onsite manager during events (VERIFY)
- Serves: San Jose, Santa Clara, Milpitas, Fremont, Sunnyvale, Morgan Hill, Gilroy, Santa Clara County, Bay Area

### 6.7 GBP hygiene checklist

- [ ] Claim or request removal of **"The Nobel Venue"** at 1654 Burdette Dr if it is a former name or defunct tenant. If Crown Prince replaced it, use "Mark as permanently closed" on that listing or request a merge through GBP support so its reviews transfer.
- [ ] Upload 30+ photos in the first month: exterior with signage, red-carpet entrance, empty hall in 3 layouts, stage, bar, prep room, parking lot, and at least 10 real-event photos. Name files `crown-prince-event-hall-san-jose-[subject].jpg` before upload.
- [ ] Post weekly (GBP Posts): one event recap, one "dates open this month," one offer or FAQ.
- [ ] Turn on messaging; respond within one business hour (the site already promises this).
- [ ] Reviews: send a review link by SMS within 48 hours of every event; reply to every review within 48 hours using the event type and "San Jose" naturally in the reply.
- [ ] Add the brochure page as the GBP "Appointment" link and the tour page as the "Booking" link.

---

## 7. What could not be verified, and a 20-minute checklist to close it

The audit environment could not load crownprincehall.com. Run these once; each takes a minute or two.

| Check | Tool | Pass criteria |
|---|---|---|
| Mobile Core Web Vitals | https://pagespeed.web.dev/ (mobile) | LCP < 2.5 s, CLS < 0.1, INP < 200 ms. Venue hero images are the usual culprit: serve WebP, ≤ 200 KB, `width`/`height` set. |
| Indexing | Google Search Console → Pages | Every event page "Indexed." If only `/` is indexed, the event sections are anchors, not pages: build the four pages in §2. |
| Sitemap | `https://crownprincehall.com/sitemap.xml` | Exists, lists every page, submitted in Search Console. |
| Robots | `https://crownprincehall.com/robots.txt` | No `Disallow: /`; sitemap line present. |
| Canonical + redirects | View source; try `http://`, `www.` | One canonical URL; all variants 301 to it. |
| Existing schema | https://validator.schema.org | Zero errors after pasting §3 and §4.5. |
| Image alt text | View source on gallery | Every `<img>` has descriptive alt: "Wedding reception banquet setup at Crown Prince Event Hall, San Jose." |
| Phone number | Verified on the site header, footer and form | Confirm GBP and Yelp show 408-408-1654 in the same format. |
| Square footage | Site copy | Change "4,000+" and "Over 4,000" in the hero and venue section to "4,100" so every mention, schema and GBP agree. |
| Tracking | GA4 DebugView | `generate_lead` fires on brochure submit; `phone_call` fires on tap-to-call. |
| NAP audit | Search "Crown Prince Event Hall" on Google, Yelp, Bing, Apple Maps, The Knot, WeddingWire, Eventective, Tagvenue, Peerspace | Identical name, address and phone on every listing. |

---

## 8. Sources used for market data and listing facts

- Crown Prince Event Hall indexed listing, https://crownprincehall.com/
- Yelp listing (categories, hours, same-address businesses), https://www.yelp.com/biz/crown-prince-event-hall-san-jose
- San Jose venue price ranges 2026: https://www.tagvenue.com/us/hire/party-venues/san-jose , https://www.tagvenue.com/us/hire/affordable-wedding-venues/san-jose , https://www.peerspace.com/venues/san-jose--ca/banquet-hall , https://vowlaunch.com/news/ultimate-guide-luxury-wedding-venues-san-jose-2025
- Competitor set for title-tag benchmarking: Casablanca Banquet Hall, The Prestige Venue, Starlite Banquet Hall, Grace Banquet Hall & Event Center, Fuze.
