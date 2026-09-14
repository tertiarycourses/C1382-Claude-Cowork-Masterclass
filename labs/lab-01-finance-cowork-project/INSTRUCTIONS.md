# Lab 01 — Create the finance Cowork project

**C1382 · Topic 1 · 55 minutes**

## Goal
Create a scoped Cowork project and a source inventory.

## What you will build
A bounded finance Cowork workflow and its review evidence. All data is fictional.

## Prerequisites
Claude Cowork on a paid plan; Excel or an Excel-compatible viewer; for Lab 3, a work Microsoft 365 account with enabled connector and Power Automate. Earlier labs provide context, but this folder includes its own workbook and instructions.

## Steps
1. Open Cowork in Claude Desktop and create a project named Finance Month-End Lab. Select only this lab folder as its local context. If Projects is unavailable, use a Cowork session connected only to this folder and put the same rules in folder instructions.
2. Copy `mock-data/finance-aug-2026.xlsx` to `working/finance-aug-2026.xlsx`. Keep `mock-data/` unchanged.
3. Add the supplied `skill/finance-control/SKILL.md` as project instructions or an enabled custom skill. Read its stop conditions aloud.
4. Paste `prompts/01-project-and-inventory.txt` into a Cowork task. Approve read access only to `mock-data/` and write access only to `working/` and `outputs/`.
5. Inspect Claude's file manifest. It must identify 14 data rows plus the header and call out one repeated `BILL-012` and one Pending `INV-013`.
6. Save the manifest in `outputs/source-inventory.md`; compare the input workbook hash before and after the task using `shasum -a 256 mock-data/finance-aug-2026.xlsx`.

## Test it
The raw workbook hash is unchanged; inventory names all seven columns, 14 rows, one duplicate ID and one pending item.

## Troubleshooting
- Cowork cannot access the workbook: connect only this lab folder in the desktop project, confirm file permissions, then retry read-only inventory.
- Formula totals disagree: check duplicate-ID and approval filters, recalculate Excel formulas, then compare each eligible row with the source.
- Outlook delivery is unavailable: verify Microsoft 365 work-account/admin write access. The native connector cannot attach files; use the approved OneDrive link or the Power Automate attachment flow. Do not claim a send occurred without Sent Items and flow history.

## Challenge
Add a second approval gate that checks the workbook file name, reviewed period and row counts before moving it to Approved Reports.

## Reflection
Which control would stop a plausible-looking but incorrect finance report from being emailed?
