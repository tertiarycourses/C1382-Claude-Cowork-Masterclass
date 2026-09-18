# Lab 03b prompt — Build the claim-form filler

Copy everything in the block below into Claude.

```text
I have attached claimants-statement-pa.pdf — a 4-page Great Eastern
Accident / Golden Protector CLAIMANT'S STATEMENT. It is a real
fillable PDF form (an AcroForm). I want to fill it by typing into a
Live Artefact instead of clicking around the PDF.

Build this in two parts.

PART 1 — Inspect the form first, before you build anything.
List its form fields with their internal names, and for each one the
page, the /MaxLen and whether it is a comb field. Show me a short
table mapping the VISIBLE label on the page to the INTERNAL field
name. Do not trust the internal names — several are misleading
(there are fields literally called "undefined", and the field named
"Gender M  F" is actually the Occupation row). Work out the real
mapping from each field's position on the page.

PART 2 — Build the data-entry artefact.
A Live Artefact titled "PA Claim — Claimant's Statement" with one
section per part of the paper form:
  1. Policy numbers
  2. Details of policyholder
  4. Details of life assured (if different) — with a
     "same as policyholder" tickbox that copies section 2 across
  5. Life assured's occupation
  6. Details of accident and medical treatment
  7. Details of disability
  8. Other information
  9. Other insurance (4 rows)

Requirements:
- Group the fields under those numbered headings, in that order, so
  the artefact reads like the paper form.
- Use the right control for each answer: date pickers for dates,
  YES / NO radio buttons for the YES / NO questions, M / F for
  gender, a textarea for the descriptions of the accident and the
  injuries.
- Show a character counter on any field with a /MaxLen, and stop
  input at the limit. Note in the UI that the boxed comb fields put
  one character per box, so values must be short.
- Mark the fields the insurer needs as required, and show a
  validation summary if any are empty on submit.
- Clean, professional insurance-form styling. Save my answers as I
  type so a refresh does not lose them.

The Submit button:
Artefacts run in a sandbox and CANNOT write my PDF, so do NOT try to
generate the PDF inside the artefact. Instead, on Submit, validate
the form, then show the collected answers as a JSON object keyed by
the INTERNAL PDF field names, in a read-only box with a "Copy JSON"
button.

Then tell me to paste that JSON back to you in the chat, and say
that you will write it into the PDF for me.
```

> **Note:** Attach `mock-data/claimants-statement-pa.pdf` before sending the prompt.

## Follow-up prompt — Claude fills the real PDF

After you click Submit and copy the JSON, paste it back with this:

```text
Here is the JSON from the artefact:

<paste the JSON here>

Fill the real form with it and save the result to
outputs/claimants-statement-FILLED.pdf. Keep the original untouched.

Do this properly:
- Write the values into the existing AcroForm fields. Do not
  flatten the form and do not draw text on top of the page.
- Set /NeedAppearances to true, or the text will be invisible in
  some PDF viewers even though the values are stored.
- The same field name can appear on more than one page, so apply
  the values to every page.
- Dates in comb boxes have no separators: write 14031981, not
  14/03/1981.

Then VERIFY it before you tell me it is done: render each page of
the filled PDF to an image, look at it, and confirm every value
landed in the box next to its correct printed label. If anything is
in the wrong row, fix the mapping and render again. Show me the
pages and a table of what you wrote into which field.
```
