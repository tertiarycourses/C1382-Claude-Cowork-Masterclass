# Claude Cowork Masterclass

Build a controlled finance workflow in Claude Cowork: create a project, reconcile a formula-driven Excel report, then schedule delivery of the approved workbook through Outlook.

| Course detail | Information |
|---|---|
| Course code | `C1382` |
| Programme | Non-WSQ |
| Duration | One day; 7.5 instructional hours |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/claude-cowork-masterclass.html) |
| Courseware | Version 2.0, 15 September 2026 |

## About the course

The course uses fictional Singapore-dollar finance transactions. Learners keep the raw workbook unchanged, define eligibility and duplicate rules, check independent control totals, and allow delivery only after review. The actual `.xlsx` attachment route uses OneDrive for Business and Power Automate because the native Claude Microsoft 365 connector currently cannot attach files to Outlook messages.

## Learning outcomes

- Create a scoped Cowork project with finance instructions, file boundaries and a source inventory.
- Produce an Excel workbook with raw, eligible, summary and exception sheets, then reconcile its formulas to independent controls.
- Set up a monthly on-demand rehearsal and an approved-file Outlook attachment flow, then verify the sent message and workbook.

## Topics covered

1. **Finance Cowork project and controls:** project instructions, permissions, source schema, duplicates and approval gates.
2. **Automate and reconcile Excel:** eligible transactions, formulas, exceptions, charts and release checks.
3. **Schedule and deliver via Outlook:** new-period workflow, cloud file context, Power Automate attachment flow and delivery audit.

## Labs

Each [lab folder](labs/README.md) includes a mock Excel workbook, prompt PDF and text, detailed instructions, control totals and a reusable Cowork skill.

1. [Create the finance Cowork project](labs/lab-01-finance-cowork-project/INSTRUCTIONS.md)
2. [Automate and reconcile the finance Excel workbook](labs/lab-02-automate-finance-excel/INSTRUCTIONS.md)
3. [Schedule the report and send the completed Excel via Outlook](labs/lab-03-schedule-and-outlook-delivery/INSTRUCTIONS.md)

## Public package

The [Learner Guide](LG-Claude%20Cowork%20Masterclass.md), editable PowerPoint deck and PDFs in [`courseware/`](courseware/), and three labs are learner-facing. Course references, superseded versions, build skills, QA renders, credentials and any trainer-private material stay outside the public release. All finance records are synthetic. Recheck current Cowork and Microsoft 365 capabilities before using the workflow with organisational data.

Provider: Tertiary Infotech Academy Pte Ltd / [Tertiary Courses](https://www.tertiarycourses.com.sg/claude-cowork-masterclass.html).
