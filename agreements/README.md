# Crown Prince Event Hall — Fillable Rental Agreement

`Crown_Prince_Rental_Agreement_Fillable.pdf` is the venue Rental Agreement turned into an
**interactive PDF form**. It is the same 4-page agreement, with the exact legal text and
branding preserved, plus real fillable fields (AcroForm) placed on every blank, checkbox,
and signature line.

Open it in any standard PDF reader (Adobe Acrobat/Reader, Apple Preview, Chrome, Edge) and
type directly into the fields; the choice boxes (alcohol, approved areas, photo release,
payment type, accessibility) are click-to-select. Nothing needs to be printed and
hand-written.

## How it was made

The form fields are stamped directly onto the **original vector pages** — the text stays
sharp at any zoom and the contract wording is never touched. Field coordinates were tuned
against a rendered copy of each page, but the delivered PDF keeps the original vector
content. Two steps, in `generator/`:

```bash
cd generator
python3 build_overlay.py   # 1. transparent overlay carrying just the AcroForm fields
python3 merge_vector.py    # 2. graft those fields onto source_original.pdf -> ../Crown_Prince_Rental_Agreement_Fillable.pdf
```

Requires `reportlab` (overlay) and `pikepdf` (vector graft). Field positions live in
`generator/fields.py` (coordinates in PDF points, measured from the top of each page), so
nudging a field is a one-line edit followed by re-running both steps.

## Field keys

Every blank is a named field. If you are feeding this into a document/merge tool that
matches by key, use the names below (or add `{{placeholders}}` with the same names in your
own design). Page numbers are 1-based.

### Text fields (37)

| Field key | Page | Fills |
|---|---|---|
| `event_date` | 1 | Event date |
| `setup_time` | 1 | Set-up time |
| `event_time` | 1 | Event time |
| `loadout_time` | 1 | Load-out time |
| `client_name` | 1 | Client name |
| `phone_number` | 1 | Client phone |
| `email` | 1 | Client email |
| `event_type_guests` | 1 | Event type / guests |
| `expected_guests` | 1 | Expected guest count |
| `legal_occupancy` | 1 | Legal occupancy |
| `music_end_time` | 1 | Music / amplified-sound end time |
| `approved_areas_other` | 1 | "Other" approved-areas description |
| `initials_1` | 1 | Client initials — §1 Assumption of Risk |
| `initials_2` | 1 | Client initials — §2 Release of Liability |
| `initials_3` | 1 | Client initials — §3 Indemnification |
| `initials_4` | 1 | Client initials — §4 Compliance with Laws |
| `initials_5` | 2 | Client initials — §5 Alcohol Policy |
| `initials_9` | 2 | Client initials — §9 Right to Terminate |
| `overtime_rate` | 2 | §7 overtime rate ($/hour) |
| `initials_11` | 3 | Client initials — §11 Quote/Payment |
| `venue_rent_fee` | 3 | Charges — Venue Rent Fee |
| `cleaning_fee` | 3 | Charges — Cleaning Fee |
| `security_rate` | 3 | Charges — Security $/hour |
| `security_duration` | 3 | Charges — Security hours |
| `security_total` | 3 | Charges — Security total |
| `package_addons` | 3 | Charges — Package Add-Ons |
| `lineitem_desc` | 3 | Charges — extra line-item description |
| `lineitem_amount` | 3 | Charges — extra line-item amount |
| `discounts` | 3 | Charges — Discounts |
| `balance_due_date` | 3 | Balance-due date (if other than 14 days before) |
| `balance_due_amount` | 3 | Balance due before event |
| `payment_other` | 3 | "Other" payment-type description |
| `initials_12` | 3 | Client initials — §12 Insurance |
| `client_signature` | 4 | Client signature |
| `client_date` | 4 | Client signature date |
| `venue_representative` | 4 | Venue representative |
| `venue_date` | 4 | Venue signature date |

### Choice fields — pick one option each (5 groups)

| Field key | Page | Options (export values) |
|---|---|---|
| `alcohol` | 1 | `No`, `Yes` |
| `approved_areas` | 1 | `IndoorOnly`, `Other` |
| `photo_release` | 2 | `Authorize`, `NotAuthorize` |
| `payment_type` | 3 | `Cash`, `Check`, `Zelle`, `CreditCard`, `Other` |
| `accessibility` | 4 | `NotInspected`, `InspectedMeets`, `InspectedNotMeets` |

The Reservation Deposit line is pre-printed at **$1,000.00** and the Security Deposit note
is informational, so neither has a fill field — matching the source agreement.

> Note: this is a form-fillable copy of the venue's existing agreement; it is not legal
> advice and the contract wording was not changed.
