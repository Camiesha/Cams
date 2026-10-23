# Crown Prince Event Hall — Bar Packages Checklist

Client-facing bar package selection checklist, designed to be shown on venue
tours and emailed as a PDF alongside the standard venue quotation.

## Files

| File | Purpose |
|------|---------|
| `bar-packages-checklist.html` | **Editable source.** Self-contained — the logo is embedded, no external files needed. Open in any browser to view; digital checkboxes and fields are interactive. |
| `Crown-Prince-Bar-Packages.pdf` | **Print-ready / email-ready** 2-page Letter PDF generated from the HTML. |

## How to update it in the future

Open `bar-packages-checklist.html` in any text editor. Everything is plain HTML/CSS.

- **Prices** — search for the dollar amounts (`$2,000`, `$32`, `$26`, `$50`, `$30`)
  and edit them in place. Each package's `Initial Service Fee` is in a `.fee` block;
  the per-person prices are in `.price` elements.
- **Package names / descriptions** — edit inside each `<article class="card">`.
- **What's included** — the `Security / Bartender / Soft drinks` chips are in the
  `.incl` list of each card.
- **Checklist options** — edit the text inside each `<label class="check">`.
- **Brand colors** — change the color tokens at the top of the `<style>` block,
  under `:root` (`--green-900`, `--cream`, `--gold`, etc.).
- **Logo** — the logo is embedded as a data URI on the `<img class="logo">` tag.
  Replace the `src` value to swap it.

### Regenerating the PDF after edits

Print the HTML from a browser (Ctrl/Cmd + P → Save as PDF, Letter size, enable
"Background graphics"). The page includes print styles that lay it out as a tidy
2-page document automatically.

## Notes

- No taxes, gratuities, minimum guest counts, alcohol brands, or extra fees are
  stated — all final pricing and beverage selections are confirmed by the venue.
- The faint watermark present on the originally supplied logo image was trimmed
  from the embedded version; the crown and wordmark are otherwise unaltered.
