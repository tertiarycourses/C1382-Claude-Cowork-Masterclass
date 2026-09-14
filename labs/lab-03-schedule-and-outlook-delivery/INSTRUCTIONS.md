# Lab 03 — Schedule the report and send the completed Excel via Outlook

**C1382 · Topic 3 · 85 minutes**

## Goal
Create a repeatable September run and controlled Outlook attachment flow.

## What you will build
A bounded finance Cowork workflow and its review evidence. All data is fictional.

## Prerequisites
Claude Cowork on a paid plan; Excel or an Excel-compatible viewer; for Lab 3, a work Microsoft 365 account with enabled connector and Power Automate. Earlier labs provide context, but this folder includes its own workbook and instructions.

## Steps
1. Use `mock-data/finance-sep-2026.xlsx` as a new-period input. Copy it to `working/` and rerun the finance skill with `prompts/03-schedule-and-deliver.txt`; save `outputs/finance-report-sep-2026.xlsx`.
2. Reconcile the new workbook against `checks/control-totals.csv`; record the file name, period, totals, exception count and review initials in `outputs/release-manifest.csv`.
3. For a cloud schedule, place the approved input and output folders in your organisation's OneDrive for Business or SharePoint and give the project exact paths. In Cowork Scheduled, create a weekly Monday task at 09:00 Asia/Singapore that acts only when a new approved month input is present. First set it to manual/on-demand and test. A schedule tied to local files or desktop apps runs locally and requires the desktop available.
4. Connect the Microsoft 365 connector using an authorised work account. The admin must enable email write tools. The native connector cannot attach files, so use it only to draft/send an approved link to the completed workbook if attachment delivery is unavailable.
5. To send the actual `.xlsx` attachment automatically, create a Power Automate cloud flow: OneDrive for Business `When a file is created` on a dedicated `Approved Reports` folder → condition filename begins `finance-report-` and ends `.xlsx` → `Get file content` → Office 365 Outlook `Send an email (V2)` to your own authorised test mailbox with the file name and file content as its attachment. The human gate is moving the reconciled final workbook into `Approved Reports`; never trigger from a working folder.
6. Run once with the synthetic September workbook. Open Sent Items and the received email. Verify attachment name, workbook sheets and totals. Check flow run history for exactly one send; avoid a second copy into the trigger folder.
7. Keep the Cowork task in manual mode after the lab unless your organisation approves the real schedule and recipient. Document the final state in `outputs/delivery-log.md`.

## Test it
September approved revenue S$48,100; approved expense S$16,960; net S$31,140. One approved workbook, one flow run and one Outlook test email with the exact `.xlsx` attachment.

## Troubleshooting
- Cowork cannot access the workbook: connect only this lab folder in the desktop project, confirm file permissions, then retry read-only inventory.
- Formula totals disagree: check duplicate-ID and approval filters, recalculate Excel formulas, then compare each eligible row with the source.
- Outlook delivery is unavailable: verify Microsoft 365 work-account/admin write access. The native connector cannot attach files; use the approved OneDrive link or the Power Automate attachment flow. Do not claim a send occurred without Sent Items and flow history.

## Challenge
Add a second approval gate that checks the workbook file name, reviewed period and row counts before moving it to Approved Reports.

## Reflection
Which control would stop a plausible-looking but incorrect finance report from being emailed?
