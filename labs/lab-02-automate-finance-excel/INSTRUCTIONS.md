# Lab 02 — Automate and reconcile the finance Excel workbook

**C1382 · Topic 2 · 120 minutes**

## Goal
Produce a formula-driven August finance report from mock transactions.

## What you will build
A bounded finance Cowork workflow and its review evidence. All data is fictional.

## Prerequisites
Claude Cowork on a paid plan; Excel or an Excel-compatible viewer; for Lab 3, a work Microsoft 365 account with enabled connector and Power Automate. Earlier labs provide context, but this folder includes its own workbook and instructions.

## Steps
1. Copy the Lab 1 workbook into this lab's `working/` folder and record the source file name, period and row count in `outputs/reconciliation.md`.
2. Open `mock-data/finance-aug-2026.xlsx` in Excel and inspect rows 2–15. Do not delete the duplicate or Pending row in the source.
3. Paste `prompts/02-build-reconciled-workbook.txt` into the same Cowork project. Require `outputs/finance-report-aug-2026.xlsx` with `Raw`, `Eligible`, `Summary`, and `Exceptions` sheets.
4. Ask Claude to copy raw rows verbatim. In `Eligible`, include Approved rows with unique Document IDs only. In `Exceptions`, show duplicate `BILL-012` and Pending `INV-013` with reasons. In `Summary`, calculate revenue, expenses, net, count and source count using Excel formulas.
5. Before accepting the workbook, independently total the six approved revenue lines and six approved expense lines from the source. Compare with `checks/control-totals.csv`. Open workbook in Excel and recalculate formulas.
6. Enter discrepancies in `outputs/reconciliation.md` and ask Cowork to fix only the defective cell or rule. Recheck all totals and the two exception rows.
7. Export no client data. Keep only the fictional output in `outputs/`.

## Test it
Approved revenue S$46,700; approved expense S$16,500; net S$30,200; 12 eligible rows; two excluded rows. The workbook has formulas and the source is unchanged.

## Troubleshooting
- Cowork cannot access the workbook: connect only this lab folder in the desktop project, confirm file permissions, then retry read-only inventory.
- Formula totals disagree: check duplicate-ID and approval filters, recalculate Excel formulas, then compare each eligible row with the source.
- Outlook delivery is unavailable: verify Microsoft 365 work-account/admin write access. The native connector cannot attach files; use the approved OneDrive link or the Power Automate attachment flow. Do not claim a send occurred without Sent Items and flow history.

## Challenge
Add a second approval gate that checks the workbook file name, reviewed period and row counts before moving it to Approved Reports.

## Reflection
Which control would stop a plausible-looking but incorrect finance report from being emailed?
