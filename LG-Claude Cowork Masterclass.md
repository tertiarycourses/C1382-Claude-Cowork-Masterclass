# Learner Guide — Claude Cowork Masterclass (C1382)



v2.1 · 16 September 2026 · One day · 7.5 instructional hours



# Document Version Control Record

# How to use this guide

Work through the labs in order or choose a scenario that matches your job. Each lab folder is independent: it has mock data, a Cowork skill, a tools guide, ready-to-paste prompts, detailed instructions, expected evidence and a checklist. Keep mock-data unchanged and save finished work in outputs/.

# Set up Claude Cowork

Open Claude and choose Cowork. A paid plan is required.

For local files, use Claude Desktop and keep it open while the task uses your computer.

Create a project or session from only the lab folder you are using.

Open TOOLS.md and enable only the tools needed for the task.

Add the lab SKILL.md as project instructions or an enabled custom skill.

Review the proposed plan before allowing file changes or connected-app actions.

# The simple task pattern

Every automation follows five questions: What outcome is needed? Which inputs may Cowork use? What file should it create? How will you verify it? Which actions require human approval?

# Use Case 01 — Create a Cowork Project

Scenario: Files and instructions live in different places. Ask Cowork to give cowork one project, one folder and clear rules. The result is a reusable workspace for every finance task.

## What goes in

Project brief

Close checklist

Dedicated lab folder

## What Cowork does

Create project

Connect one folder

Add finance skill

## Skills and tools

Cowork Projects

Local folder access

Project instructions

## Human check

File map lists every source; originals stay unchanged

## Lab 01 — step-by-step

C1382 · Topic 1 · 35 minutes

### Goal

Create a simple Cowork project with a dedicated finance folder, clear instructions and safe output locations.

### What you will build

A reusable Finance Task Automation project with folder instructions and a first file inventory.

### Prerequisites

Open this lab folder as the Cowork project context. Read TOOLS.md, enable the named skill in skill/finance-project-organiser/SKILL.md, and use only the fictional files in mock-data/.

### Steps

Open `TOOLS.md` and confirm the available tools and access boundary.

Review the files in `mock-data/`; copy any file you will change into `working/`.

Add or enable `skill/finance-project-organiser/SKILL.md` in the Cowork project.

Open `prompts/prompt-01.txt`, paste the prompt into Cowork and review its proposed plan.

Allow only the reads and writes needed for this lab. Keep consequential actions paused.

Open the generated files and compare them with `CHECKLIST.md`. Correct any mismatch in the output, then repeat the check.

Save the finished artifacts in `outputs/` and record the evidence used.

### Test it

The project shows the correct folder, the file map lists every mock-data file, and no source file changed.

### Troubleshooting

**Cowork selects the wrong file:** name the expected date format and require it to list candidates before choosing.

**A workbook does not refresh:** open it in Excel, recalculate, and ask Cowork to inspect formulas and chart source ranges.

**A claim has no source:** remove it or add a direct file, cell or URL reference.

### Challenge

Change the reporting period or audience and rerun the task without changing the skill's stable rules.

### Reflection

Which part of this task should always remain a human review point?

# Use Case 02 — Refresh an Excel Dashboard

Scenario: The dashboard shows last month’s figures. Ask Cowork to find the newest dated file and refresh the workbook. The result is current kpis and charts in one excel file.

## What goes in

Three dated CSV files

Dashboard template

Expected KPI check

## What Cowork does

Find latest file

Update Data sheet

Refresh charts

## Skills and tools

Cowork files

Spreadsheet skill

Microsoft Excel

## Human check

September: revenue S$128k, expenses S$89.5k, net S$38.5k

## Lab 02 — step-by-step

C1382 · Topic 1 · 55 minutes

### Goal

Find the newest dated finance file, update an Excel dashboard and refresh its charts.

### What you will build

An updated monthly-finance-dashboard.xlsx with current KPIs and two charts.

### Prerequisites

Open this lab folder as the Cowork project context. Read TOOLS.md, enable the named skill in skill/latest-finance-dashboard/SKILL.md, and use only the fictional files in mock-data/.

### Steps

Open `TOOLS.md` and confirm the available tools and access boundary.

Review the files in `mock-data/`; copy any file you will change into `working/`.

Add or enable `skill/latest-finance-dashboard/SKILL.md` in the Cowork project.

Open `prompts/prompt-02.txt`, paste the prompt into Cowork and review its proposed plan.

Allow only the reads and writes needed for this lab. Keep consequential actions paused.

Open the generated files and compare them with `CHECKLIST.md`. Correct any mismatch in the output, then repeat the check.

Save the finished artifacts in `outputs/` and record the evidence used.

### Test it

The output identifies 2026-09 as latest, displays September revenue S$128,000, expenses S$89,500 and net S$38,500, and contains refreshed charts.

### Troubleshooting

**Cowork selects the wrong file:** name the expected date format and require it to list candidates before choosing.

**A workbook does not refresh:** open it in Excel, recalculate, and ask Cowork to inspect formulas and chart source ranges.

**A claim has no source:** remove it or add a direct file, cell or URL reference.

### Challenge

Change the reporting period or audience and rerun the task without changing the skill's stable rules.

### Reflection

Which part of this task should always remain a human review point?

# Use Case 03 — Research AI-in-Finance News

Scenario: Interesting news is scattered across many websites. Ask Cowork to find six recent, credible developments and cite each source. The result is a structured excel research tracker.

## What goes in

Research brief

Excel tracker template

Live web sources

## What Cowork does

Search recent sources

Check dates and links

Write to Excel

## Skills and tools

Cowork web search

Web fetch

Spreadsheet skill

## Human check

Six direct links open; every date and summary is sourced

## Lab 03 — step-by-step

C1382 · Topic 2 · 50 minutes

### Goal

Research recent AI technology news relevant to finance and compile a sourced Excel tracker.

### What you will build

An AI-finance-news-tracker.xlsx with source, date, summary, finance relevance and follow-up columns.

### Prerequisites

Open this lab folder as the Cowork project context. Read TOOLS.md, enable the named skill in skill/finance-news-researcher/SKILL.md, and use only the fictional files in mock-data/.

### Steps

Open `TOOLS.md` and confirm the available tools and access boundary.

Review the files in `mock-data/`; copy any file you will change into `working/`.

Add or enable `skill/finance-news-researcher/SKILL.md` in the Cowork project.

Open `prompts/prompt-03.txt`, paste the prompt into Cowork and review its proposed plan.

Allow only the reads and writes needed for this lab. Keep consequential actions paused.

Open the generated files and compare them with `CHECKLIST.md`. Correct any mismatch in the output, then repeat the check.

Save the finished artifacts in `outputs/` and record the evidence used.

### Test it

The workbook contains six distinct recent items, six direct links that open, dates, concise summaries, and a completed Research Notes sheet.

### Troubleshooting

**Cowork selects the wrong file:** name the expected date format and require it to list candidates before choosing.

**A workbook does not refresh:** open it in Excel, recalculate, and ask Cowork to inspect formulas and chart source ranges.

**A claim has no source:** remove it or add a direct file, cell or URL reference.

### Challenge

Change the reporting period or audience and rerun the task without changing the skill's stable rules.

### Reflection

Which part of this task should always remain a human review point?

# Use Case 04 — Turn Finance Data into Slides

Scenario: Leaders receive a dense workbook. Ask Cowork to turn the numbers into a five-slide update. The result is clear charts, messages and next actions.

## What goes in

Quarterly workbook

Manager brief

Brand guide

## What Cowork does

Read the brief

Choose the story

Build editable slides

## Skills and tools

Cowork files

Spreadsheet skill

PowerPoint skill

## Human check

Five slides; Q3 revenue S$378k and net S$108.5k match Excel

## Lab 04 — step-by-step

C1382 · Topic 2 · 55 minutes

### Goal

Transform a finance workbook and manager brief into a clear five-slide presentation.

### What you will build

A five-slide management update with KPI chart, variance story, cash outlook and actions.

### Prerequisites

Open this lab folder as the Cowork project context. Read TOOLS.md, enable the named skill in skill/finance-deck-builder/SKILL.md, and use only the fictional files in mock-data/.

### Steps

Open `TOOLS.md` and confirm the available tools and access boundary.

Review the files in `mock-data/`; copy any file you will change into `working/`.

Add or enable `skill/finance-deck-builder/SKILL.md` in the Cowork project.

Open `prompts/prompt-04.txt`, paste the prompt into Cowork and review its proposed plan.

Allow only the reads and writes needed for this lab. Keep consequential actions paused.

Open the generated files and compare them with `CHECKLIST.md`. Correct any mismatch in the output, then repeat the check.

Save the finished artifacts in `outputs/` and record the evidence used.

### Test it

The deck has five slides, editable charts, correct Q3 revenue S$378,000, expense S$269,500, net S$108,500, and three actions from the manager brief.

### Troubleshooting

**Cowork selects the wrong file:** name the expected date format and require it to list candidates before choosing.

**A workbook does not refresh:** open it in Excel, recalculate, and ask Cowork to inspect formulas and chart source ranges.

**A claim has no source:** remove it or add a direct file, cell or URL reference.

### Challenge

Change the reporting period or audience and rerun the task without changing the skill's stable rules.

### Reflection

Which part of this task should always remain a human review point?

# Use Case 05 — Build an AP Tracker from Invoices

Scenario: Invoice details are copied one file at a time. Ask Cowork to extract five invoices and flag anything uncertain. The result is a tidy ap tracker ready for review.

## What goes in

Five mock invoice PDFs

AP tracker template

Review rules

## What Cowork does

Read invoices

Extract fields

Flag exceptions

## Skills and tools

Document reading

PDF skill

Spreadsheet skill

## Human check

Five rows; duplicate INV-204 and missing PO are visible

## Lab 05 — step-by-step

C1382 · Topic 3 · 45 minutes

### Goal

Read a folder of mock invoices and create a tidy accounts-payable tracker.

### What you will build

An AP-tracker.xlsx with invoice number, supplier, date, due date, amount, currency and review status.

### Prerequisites

Open this lab folder as the Cowork project context. Read TOOLS.md, enable the named skill in skill/invoice-to-ap-tracker/SKILL.md, and use only the fictional files in mock-data/.

### Steps

Open `TOOLS.md` and confirm the available tools and access boundary.

Review the files in `mock-data/`; copy any file you will change into `working/`.

Add or enable `skill/invoice-to-ap-tracker/SKILL.md` in the Cowork project.

Open `prompts/prompt-05.txt`, paste the prompt into Cowork and review its proposed plan.

Allow only the reads and writes needed for this lab. Keep consequential actions paused.

Open the generated files and compare them with `CHECKLIST.md`. Correct any mismatch in the output, then repeat the check.

Save the finished artifacts in `outputs/` and record the evidence used.

### Test it

The tracker contains five invoice rows, flags duplicate INV-204, marks one missing purchase order for review, and reconciles each invoice total.

### Troubleshooting

**Cowork selects the wrong file:** name the expected date format and require it to list candidates before choosing.

**A workbook does not refresh:** open it in Excel, recalculate, and ask Cowork to inspect formulas and chart source ranges.

**A claim has no source:** remove it or add a direct file, cell or URL reference.

### Challenge

Change the reporting period or audience and rerun the task without changing the skill's stable rules.

### Reflection

Which part of this task should always remain a human review point?

# Use Case 06 — Write Budget Variance Commentary

Scenario: Managers see variances but not the story. Ask Cowork to calculate material variances and explain them simply. The result is a reviewed workbook and one-page commentary.

## What goes in

Budget vs actual

Department notes

Materiality rule

## What Cowork does

Calculate variance

Highlight material items

Draft commentary

## Skills and tools

Cowork files

Spreadsheet skill

Document skill

## Human check

Each comment links to a line item or is marked as a question

## Lab 06 — step-by-step

C1382 · Topic 3 · 45 minutes

### Goal

Calculate material variances and write concise management commentary.

### What you will build

A variance-review.xlsx and a one-page management-commentary.md.

### Prerequisites

Open this lab folder as the Cowork project context. Read TOOLS.md, enable the named skill in skill/variance-commentary/SKILL.md, and use only the fictional files in mock-data/.

### Steps

Open `TOOLS.md` and confirm the available tools and access boundary.

Review the files in `mock-data/`; copy any file you will change into `working/`.

Add or enable `skill/variance-commentary/SKILL.md` in the Cowork project.

Open `prompts/prompt-06.txt`, paste the prompt into Cowork and review its proposed plan.

Allow only the reads and writes needed for this lab. Keep consequential actions paused.

Open the generated files and compare them with `CHECKLIST.md`. Correct any mismatch in the output, then repeat the check.

Save the finished artifacts in `outputs/` and record the evidence used.

### Test it

The workbook uses formulas, material items are highlighted, and the commentary names Marketing, Contractors and Travel with traceable evidence or questions.

### Troubleshooting

**Cowork selects the wrong file:** name the expected date format and require it to list candidates before choosing.

**A workbook does not refresh:** open it in Excel, recalculate, and ask Cowork to inspect formulas and chart source ranges.

**A claim has no source:** remove it or add a direct file, cell or URL reference.

### Challenge

Change the reporting period or audience and rerun the task without changing the skill's stable rules.

### Reflection

Which part of this task should always remain a human review point?

# Use Case 07 — Build a Cash-Flow Watchlist

Scenario: Receipts and payments sit in separate files. Ask Cowork to combine them into a 14-day running balance. The result is a cash watchlist and reviewed email draft.

## What goes in

Receivables

Payments

Cash assumptions

## What Cowork does

Merge dates

Calculate balance

Draft alert

## Skills and tools

Cowork files

Spreadsheet skill

Outlook draft

## Human check

Low-balance day and top payments match the workbook

## Lab 07 — step-by-step

C1382 · Topic 3 · 45 minutes

### Goal

Combine receivables and payment schedules into a two-week cash watchlist and draft an email.

### What you will build

A cashflow-watchlist.xlsx and a ready-for-review Outlook email draft.

### Prerequisites

Open this lab folder as the Cowork project context. Read TOOLS.md, enable the named skill in skill/cashflow-watchlist/SKILL.md, and use only the fictional files in mock-data/.

### Steps

Open `TOOLS.md` and confirm the available tools and access boundary.

Review the files in `mock-data/`; copy any file you will change into `working/`.

Add or enable `skill/cashflow-watchlist/SKILL.md` in the Cowork project.

Open `prompts/prompt-07.txt`, paste the prompt into Cowork and review its proposed plan.

Allow only the reads and writes needed for this lab. Keep consequential actions paused.

Open the generated files and compare them with `CHECKLIST.md`. Correct any mismatch in the output, then repeat the check.

Save the finished artifacts in `outputs/` and record the evidence used.

### Test it

The running-balance formula works, the lowest-balance day is flagged, and the email remains a draft with figures matching the workbook.

### Troubleshooting

**Cowork selects the wrong file:** name the expected date format and require it to list candidates before choosing.

**A workbook does not refresh:** open it in Excel, recalculate, and ask Cowork to inspect formulas and chart source ranges.

**A claim has no source:** remove it or add a direct file, cell or URL reference.

### Challenge

Change the reporting period or audience and rerun the task without changing the skill's stable rules.

### Reflection

Which part of this task should always remain a human review point?

# Use Case 08 — Schedule a Weekly Finance Briefing

Scenario: The same briefing is rebuilt every Monday. Ask Cowork to rehearse a scheduled task using only an approved workbook. The result is a controlled weekly routine ready for approval.

## What goes in

Approved workbook

Release checklist

Test recipient

## What Cowork does

Run on demand

Check approval

Prepare delivery flow

## Skills and tools

Scheduled tasks

OneDrive

Outlook + Power Automate

## Human check

Draft stays on demand; unapproved workbook is rejected

## Lab 08 — step-by-step

C1382 · Topic 3 · 45 minutes

### Goal

Package a reviewed weekly workbook and configure an on-demand rehearsal for scheduled delivery.

### What you will build

A scheduled-task prompt, release checklist and Power Automate attachment-flow specification.

### Prerequisites

Open this lab folder as the Cowork project context. Read TOOLS.md, enable the named skill in skill/scheduled-finance-briefing/SKILL.md, and use only the fictional files in mock-data/.

### Steps

Open `TOOLS.md` and confirm the available tools and access boundary.

Review the files in `mock-data/`; copy any file you will change into `working/`.

Add or enable `skill/scheduled-finance-briefing/SKILL.md` in the Cowork project.

Open `prompts/prompt-08.txt`, paste the prompt into Cowork and review its proposed plan.

Allow only the reads and writes needed for this lab. Keep consequential actions paused.

Open the generated files and compare them with `CHECKLIST.md`. Correct any mismatch in the output, then repeat the check.

Save the finished artifacts in `outputs/` and record the evidence used.

### Test it

The on-demand rehearsal finds one approved workbook, the checklist blocks unapproved files, and the flow specification maps filename and ContentBytes correctly without sending.

### Troubleshooting

**Cowork selects the wrong file:** name the expected date format and require it to list candidates before choosing.

**A workbook does not refresh:** open it in Excel, recalculate, and ask Cowork to inspect formulas and chart source ranges.

**A claim has no source:** remove it or add a direct file, cell or URL reference.

### Challenge

Change the reporting period or audience and rerun the task without changing the skill's stable rules.

### Reflection

Which part of this task should always remain a human review point?

# Scheduling and connected tools

Cowork scheduled tasks can use connected tools and cloud files. A schedule that needs local files or desktop applications runs locally. Start every scheduled workflow as an on-demand rehearsal. Keep the lab schedule disabled after the exercise.

The Microsoft 365 connector can work with Outlook when organisation write tools are enabled. For an actual file attachment, the lab documents a Power Automate flow: OneDrive Approved Reports trigger, Get file content, then Outlook Send an email (V2) with Name and ContentBytes. Use a test mailbox and do not send during the lab.

# Current references

Claude Cowork: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork

Cowork projects: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork

Scheduled tasks: https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork

Microsoft 365 connector: https://support.claude.com/en/articles/15183774-connect-to-microsoft-365

Outlook Power Automate actions: https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/office365outlook
