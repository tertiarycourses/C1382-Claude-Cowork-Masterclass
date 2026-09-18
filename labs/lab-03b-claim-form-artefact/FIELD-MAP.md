# Lab 03b — trainer reference: the real field map

For the trainer. Learners should derive this themselves in Part 1 of the prompt;
use it to check their answer, or to unstick a table that has gone wrong.

`claimants-statement-pa.pdf` is a genuine AcroForm: **4 pages, 107 fields**
(103 text, 1 checkbox, 4 signature). Most text fields are **comb** fields —
one character per printed box — with a `/MaxLen` that silently truncates
anything longer.

## The traps

1. **Names don't match labels.** Several fields are called `undefined`,
   `undefined_2` … and the field named `Gender M  F` is the **Occupation**
   row, not gender. Gender is printed "M / F *" and is deleted by hand, not
   typed. Placement must be derived from each widget's `/Rect`, not its name.
2. **`/NeedAppearances` is absent in the source.** Set it to `true` when
   writing, or values are stored but render blank in some viewers.
3. **Comb fields take no separators.** A date of birth goes in as `14031981`
   (`/MaxLen` 8), not `14/03/1981`.
4. **YES / NO answers are text fields, not checkboxes.** The only real
   checkbox is `Check Box1` (states `/Off`, `/Yes`) — the direct-credit
   option in section 3.

## Section 2 — Details of policyholder (page 1), verified by render

| Printed label | Internal field name | MaxLen |
|---|---|---|
| Policy No(s). — box 1 | `undefined` | 10 |
| Policy No(s). — box 2 | `undefined_2` | 10 |
| Policy No(s). — box 3 | `undefined_3` | 10 |
| Policy No(s). — box 4 | `undefined_4` | 10 |
| Name — line 1 | `According to` | 37 |
| Name — line 2 | `undefined_5` | 37 |
| NRIC / FIN No. | `NRIC Passport No` | 12 |
| Date of Birth | `Date of Birth ddmmyyyy` | 8 |
| **Occupation** | **`Gender M  F`** | 37 |
| Home Tel | `undefined_6` | 8 |
| Office Tel | `Office Tel` | 8 |
| HP No. | `HP No` | 8 |
| E-mail Address | `Email Address` | — |
| Date (footer) | `Date` | — |

## Section 4 — Life assured, if different (page 1)

Same shape, suffixed: `According to_2` and `NRIC Passport` (the two name
lines), `NRIC Passport No_2`, `Date of Birth ddmmyyyy_2`, `undefined_7`
(Home Tel), `Office Tel_1`, `HP No_2`.

## Section 3 — Settlement option (page 1)

`Check Box1` (direct credit), then the bank table: `Text3` (Name of Bank),
`Text4` (Branch), `Text5` (Account Number), `Text6` (Account Holder's Name).

## Sections 5 and 6 (page 2)

Occupation block: `5  DETAILS OF LIFE ASSUREDS OCCUPATION` is the
**Occupation** field itself; then `Name of Employer`, `Address of Employer`,
`Postal Code`, `Description of Duties 1`–`2`.

Accident block: `Day` / `Month` / `Year` (comb, 2/2/4), `Time of Accident`,
`Place of Accident`, `Detailed description of the Accident 1`–`4`,
`Detailed description of the injuries 1`–`3`, the alcohol/drugs follow-up,
and witnesses `Name of WitnessRow1`–`2` with `Telephone NoRow1`–`2`.

## Sections 7, 8 and 9 (pages 3–4)

Dates repeat as `Day_2`…`Day_6` with matching `Month_n` / `Year_n` for the
doctor's first attendance and the disability periods. Other insurance is a
4-row table: `Name of Employer InsurerRow1`–`4`, `Date of IssueRow1`–`4`,
`Type of PlanRow1`–`4`, `Claim AmountRow1`–`4`, `Claim Notified YES NORow1`–`4`,
`Claim Paid YES NORow1`–`4`. The declaration block closes with `Name`,
`NRIC Passport No_3` and `Date_4`.

## Minimal working fill

Verified against a render of page 1 — every value lands beside its correct
printed label:

```python
import pypdf
from pypdf.generic import NameObject, BooleanObject

SRC = "mock-data/claimants-statement-pa.pdf"
OUT = "outputs/claimants-statement-FILLED.pdf"

writer = pypdf.PdfWriter(clone_from=SRC)
writer._root_object["/AcroForm"][NameObject("/NeedAppearances")] = BooleanObject(True)

values = {
    "undefined": "PA8871234",
    "According to": "TAN WEI LING",
    "NRIC Passport No": "S8134567D",
    "Date of Birth ddmmyyyy": "14031981",   # comb: no slashes
    "Gender M  F": "FINANCE MANAGER",       # this is the Occupation row
    "undefined_6": "65550180",              # Home Tel
    "Office Tel": "65550181",
    "HP No": "91234567",
    "Email Address": "weiling.tan@example.com",
    "Date": "18/09/2026",
}

for page in writer.pages:                  # names recur across pages
    writer.update_page_form_field_values(page, values)

writer.write(OUT)
```

Verify by rendering, never by trusting the field name:

```bash
pdftoppm -png -r 80 -f 1 -l 1 outputs/claimants-statement-FILLED.pdf /tmp/page
```
