# CRM › Events · Assigned to — Improvement request

**Status:** For review · **Date:** 5 Sep 2026 · **Applies to:** Assigned to / Owner field in Events and Leads
**Presentation:** published artifact "Events Assigned To" (Before → Requested change → Expected result).

## Issue

Cams / Camiesha does not appear as an option under **Assigned to**. The options available today are Vince, Leon and "Alvin (Admin)". Alvin is also the name of a venue, Alvin Studio & Courtyard (DBA of Crown Prince Hall), shown on the same lead screen. Assigning a record to "Alvin (Admin)" hides who is actually responsible.

Evidence: lead records supplied 5 Sep 2026 show Owner = Vince, Owner = Leon, and Owner / Assigned To = "Alvin (Admin)".

## Requested change

1. Add Cams / Camiesha as an available Assigned to user.
2. Keep Vince and Leon available, provided they are active team members.
3. Review the "Alvin (Admin)" entry: confirm whether it is a person or a shared admin login, and rename or remove it so the venue name is not treated as a staff member.
4. Distinguish people from venues and event halls in the list.
5. Apply the corrected list everywhere Assigned to / Owner is used: events, leads, filters, lists, reports.

**Business rule:** Assigned to should only ever offer people. Venues belong in the Venue field.

## Expected result

| Before | After |
|---|---|
| Vince · Leon · Alvin (Admin) | Vince · Leon · Cams / Camiesha |

Alvin Studio stays in the Venue field only. If "Alvin (Admin)" is a real person, the entry carries their actual name; if it is a shared admin login, it is not offered as an assignee.

**Done when**

- [ ] Cams / Camiesha can be selected on a new and an existing record
- [ ] Vince and Leon remain selectable
- [ ] The venue name no longer appears as an assignee
- [ ] People and venues are clearly separated wherever Assigned to is shown
- [ ] Records currently assigned to "Alvin (Admin)" are reviewed and reassigned
- [ ] Filters, lists and reports using Assigned to show the corrected names

## Open questions

- Is "Alvin (Admin)" a person, or a shared admin login named after the venue?
- Should records currently assigned to "Alvin (Admin)" be reassigned in bulk or reviewed one by one?
- Are Vince and Leon both still active team members?
