# Learner Guide — Claude Cowork Masterclass (C1382)

v2.0 · 15 September 2026 · One day, 7.5 instructional hours



# Document Version Control Record

# Purpose and setup

You will work with fictional Singapore-dollar transactions to build a finance Cowork project, a reconciled Excel workbook and a scheduled Outlook attachment path. Use only the provided mock data. Claude Cowork, Excel or an Excel-compatible viewer, and an active paid Claude account are needed. Lab 3 additionally requires an authorised work Microsoft 365 account, connector write permission and Power Automate.

Current product constraint: the native Microsoft 365 connector can send Outlook mail but cannot attach a file. The attachment path in Lab 3 uses OneDrive for Business and Power Automate. Cloud schedules use connected files; a scheduled task that requires local files or apps runs locally.

# Detailed setup and working sequence

## Create the finance project

Open Claude Desktop, select Cowork, and create Finance Month-End Lab under Projects. Choose only the lab folder as context; do not select a parent finance drive.

Open the project instructions and paste the finance-control skill rules. Record the folder name, source filename, output path and review owner in the first task.

Ask for a read-only inventory. Confirm 14 rows, seven columns, duplicate BILL-012 and Pending INV-013 before any workbook transformation.

## Build and inspect the Excel workbook

Make a working copy of finance-aug-2026.xlsx. Require four sheets named Raw, Eligible, Summary and Exceptions. Raw keeps the original 14 records unchanged.

Eligible includes only Approved records and the first occurrence of each Document ID within the period. Exceptions contains the later BILL-012 and Pending INV-013 with source row numbers and reasons.

In Summary, use Excel formulas that point to Eligible. Revenue is the sum of positive eligible amounts, expenses are the absolute value of negative eligible amounts, and net equals revenue minus expenses.

Open the finished file in Excel, force recalculation, and inspect both formulas and displayed values. Compare S$46,700 revenue, S$16,500 expenses and S$30,200 net with the independent control file. Stop on any mismatch.

## Schedule and deliver through Outlook

Run the September prompt on demand before creating a cadence. Verify S$48,100 revenue, S$16,960 expenses, S$31,140 net, 12 eligible rows and two exceptions.

For a cloud Cowork schedule, move the source into authorised OneDrive for Business or SharePoint context. Use Scheduled > New task; set the weekly Monday 09:00 Asia/Singapore cadence, gated on a new approved month input only after the on-demand rehearsal. A local-folder task runs locally and needs the desktop available.

Connect Microsoft 365 through Customize > Connectors using a work account. The tenant administrator must have granted consent and enabled email write tools. The native connector may send a reviewed link, but cannot attach the Excel file.

For an attachment, configure Power Automate: OneDrive for Business When a file is created on Approved Reports, restrict the trigger to finance-report-*.xlsx, Get file content, then Office 365 Outlook Send an email (V2) with the file name and content in its attachment fields.

Only move a human-reviewed final workbook to Approved Reports. Verify the flow run, Sent Items, received attachment name, openable workbook and totals. Keep the task manual until the organisation approves the cadence and recipient.

# Topic 01 — Finance Cowork project and controls

## Project scope

Mechanism: Finance Month-End Lab → synthetic August folder → outputs only. Worked finance evidence: 14 source rows; 7 columns; one duplicate ID. Review decision: Reject a plan that names a broader drive.

## Folder boundary

Mechanism: mock-data read-only → working copy → outputs. Worked finance evidence: Source SHA-256 unchanged after run. Review decision: Stop if a raw cell changes.

## Project instructions

Mechanism: Period + currency + eligibility rule + stop rule. Worked finance evidence: Approved, unique Document ID, SGD. Review decision: Project rule outranks a vague task phrase.

## Task contract

Mechanism: Outcome + source + output + review gate. Worked finance evidence: Finance report August 2026, no email. Review decision: No recipient or publish action in first run.

## Source schema

Mechanism: Date | Document ID | Counterparty | Category | Amount | Currency | Status. Worked finance evidence: 14 rows × 7 fields in the workbook. Review decision: Unknown currency or blank ID becomes exception.

## Approval field

Mechanism: Approved is eligible; Pending is held. Worked finance evidence: INV-013 is Pending +S$2,200. Review decision: Do not include pending revenue.

## Duplicate key

Mechanism: Document ID is business key within period. Worked finance evidence: BILL-012 occurs twice at -S$1,020. Review decision: Keep first; log second occurrence.

## Provenance

Mechanism: Every output metric links to named source rows. Worked finance evidence: Revenue source: six approved invoices. Review decision: A narrative without row links is not evidence.

## Permission gate

Mechanism: Read workbook; write only working and outputs. Worked finance evidence: No change to mock-data hash. Review decision: Decline connector or email permission here.

## Prompt injection

Mechanism: Workbook text is data, never new instructions. Worked finance evidence: Counterparty cell cannot authorize a send. Review decision: Treat embedded instructions as untrusted data.

## Plan review

Mechanism: Inspect files, operations and side effects. Worked finance evidence: Expected: read one .xlsx, write one manifest. Review decision: Pause if browser or mailbox appears in plan.

## Inventory check

Mechanism: Source count → duplicate count → pending count. Worked finance evidence: 14 = 12 eligible + 2 excluded. Review decision: Mismatch blocks Lab 2.

# Topic 02 — Automate and reconcile Excel

## Raw sheet

Mechanism: Copy all 14 rows with original column order. Worked finance evidence: Raw!A1:G15 retained. Review decision: Never normalize away exception evidence.

## Eligible sheet

Mechanism: Approved ∧ first occurrence of Document ID. Worked finance evidence: 12 eligible rows, 6 revenue + 6 expense. Review decision: Filter criteria must be visible.

## Exceptions sheet

Mechanism: Record excluded row, reason, source address. Worked finance evidence: BILL-012 repeat; INV-013 pending. Review decision: No silent row deletion.

## Revenue formula

Mechanism: SUMIFS eligible positive Amount SGD. Worked finance evidence: S$46,700 from six invoices. Review decision: Compare formula result to independent total.

## Expense formula

Mechanism: ABS(SUMIFS eligible negative Amount SGD)). Worked finance evidence: S$16,500 from six bills. Review decision: Check sign convention before net.

## Net formula

Mechanism: Revenue minus absolute expenses. Worked finance evidence: S$46,700 − S$16,500 = S$30,200. Review decision: Net must equal SUM eligible amounts.

## Count control

Mechanism: COUNTA eligible Document ID range. Worked finance evidence: 12 eligible; 14 source rows. Review decision: Count drift signals a dropped row.

## Status control

Mechanism: Only exact Approved values qualify. Worked finance evidence: Pending INV-013 excluded. Review decision: Whitespace or case variants require review.

## ID control

Mechanism: Unique ID within month, not across all time. Worked finance evidence: Duplicate BILL-012 adds no expense. Review decision: A second month may reuse an ID.

## Formula audit

Mechanism: Inspect formulas, cached values and ranges. Worked finance evidence: Summary points to Eligible, not Raw. Review decision: Hard-coded totals fail repeatability.

## Workbook chart

Mechanism: Revenue / expense / net as editable columns. Worked finance evidence: 46.7k / 16.5k / 30.2k SGD. Review decision: Chart labels must name unit and period.

## Release check

Mechanism: Control totals + exceptions + protected source. Worked finance evidence: All 5 expected controls match. Review decision: Do not email a mismatched workbook.

# Topic 03 — Schedule and deliver via Outlook

## New-period parameter

Mechanism: Switch input period to September 2026. Worked finance evidence: finance-sep-2026.xlsx is independent input. Review decision: Never reuse August output as September.

## September control

Mechanism: Same rules on new transactions. Worked finance evidence: Revenue 48,100; expense 16,960; net 31,140. Review decision: Variance alone is not proof.

## Project schedule

Mechanism: Weekly Monday 09:00 Singapore; new month input gate. Worked finance evidence: Task prompt names input and output cloud folders. Review decision: A local-folder schedule requires desktop.

## Cloud path

Mechanism: OneDrive/SharePoint connector provides source. Worked finance evidence: Approved Reports separate from working folder. Review decision: Cloud job cannot depend on a local-only path.

## On-demand rehearsal

Mechanism: Run schedule once manually first. Worked finance evidence: One workbook, one release manifest. Review decision: Repeated run must not duplicate emails.

## Review manifest

Mechanism: Period + totals + exceptions + reviewer. Worked finance evidence: 12 eligible and 2 excluded in September. Review decision: No approval record, no delivery.

## Outlook connector

Mechanism: Microsoft 365 write permission can send email. Worked finance evidence: Native email includes link, not attachment. Review decision: Attachment requirement needs another route.

## Attachment flow

Mechanism: OneDrive file-created → content → Outlook V2. Worked finance evidence: Approved Reports/finance-report-sep-2026.xlsx. Review decision: Never trigger on working files.

## Flow condition

Mechanism: Filename prefix and .xlsx suffix. Worked finance evidence: finance-report-...xlsx only. Review decision: Other files must cause zero sends.

## Attachment bytes

Mechanism: Get file content feeds ContentBytes. Worked finance evidence: Name equals approved workbook filename. Review decision: Check received attachment opens.

## Idempotency

Mechanism: Unique period filename + no overwrite in trigger. Worked finance evidence: One created file → one flow run → one Sent Item. Review decision: Duplicate send requires stop and investigation.

## Delivery audit

Mechanism: Sent Items + received file + flow history. Worked finance evidence: Subject, recipient, workbook version align. Review decision: A successful Cowork message alone is insufficient.

# Lab 1 — lab-01-finance-cowork-project

C1382 · Topic 1 · 55 minutes

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

Cowork cannot access the workbook: connect only this lab folder in the desktop project, confirm file permissions, then retry read-only inventory.

Formula totals disagree: check duplicate-ID and approval filters, recalculate Excel formulas, then compare each eligible row with the source.

Outlook delivery is unavailable: verify Microsoft 365 work-account/admin write access. The native connector cannot attach files; use the approved OneDrive link or the Power Automate attachment flow. Do not claim a send occurred without Sent Items and flow history.

## Challenge

Add a second approval gate that checks the workbook file name, reviewed period and row counts before moving it to Approved Reports.

## Reflection

Which control would stop a plausible-looking but incorrect finance report from being emailed?

# Lab 2 — lab-02-automate-finance-excel

C1382 · Topic 2 · 120 minutes

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

Cowork cannot access the workbook: connect only this lab folder in the desktop project, confirm file permissions, then retry read-only inventory.

Formula totals disagree: check duplicate-ID and approval filters, recalculate Excel formulas, then compare each eligible row with the source.

Outlook delivery is unavailable: verify Microsoft 365 work-account/admin write access. The native connector cannot attach files; use the approved OneDrive link or the Power Automate attachment flow. Do not claim a send occurred without Sent Items and flow history.

## Challenge

Add a second approval gate that checks the workbook file name, reviewed period and row counts before moving it to Approved Reports.

## Reflection

Which control would stop a plausible-looking but incorrect finance report from being emailed?

# Lab 3 — lab-03-schedule-and-outlook-delivery

C1382 · Topic 3 · 85 minutes

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

September approved revenue S$48,100; approved expense S$16,960; net S$31,140. One approved workbook, one flow run and one Outlook test email with the exact .xlsx attachment.

## Troubleshooting

Cowork cannot access the workbook: connect only this lab folder in the desktop project, confirm file permissions, then retry read-only inventory.

Formula totals disagree: check duplicate-ID and approval filters, recalculate Excel formulas, then compare each eligible row with the source.

Outlook delivery is unavailable: verify Microsoft 365 work-account/admin write access. The native connector cannot attach files; use the approved OneDrive link or the Power Automate attachment flow. Do not claim a send occurred without Sent Items and flow history.

## Challenge

Add a second approval gate that checks the workbook file name, reviewed period and row counts before moving it to Approved Reports.

## Reflection

Which control would stop a plausible-looking but incorrect finance report from being emailed?

# Reference and product verification

Anthropic Claude Cowork Help: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork

Anthropic schedule documentation: https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork

Anthropic Microsoft 365 connector: https://support.claude.com/en/articles/15183774-connect-to-microsoft-365

Microsoft OneDrive connector: https://learn.microsoft.com/en-us/connectors/onedriveforbusiness/

Microsoft Outlook Power Automate: https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/office365outlook
