---
name: scheduled-finance-briefing
description: Package a reviewed weekly workbook and configure an on-demand rehearsal for scheduled delivery.
---
# Schedule a Weekly Finance Briefing skill

## Inputs
Use only the files in `mock-data/` and the sources explicitly named in the task.

## Method
1. Confirm the requested period, audience and output filename.
2. Inventory inputs and identify missing or ambiguous data.
3. Work on a copy and retain source filenames or URLs.
4. Create the requested output with editable tables, formulas or charts where relevant.
5. Run the verification in `CHECKLIST.md` and report exceptions.
6. Pause before email, schedule activation, publication, deletion or any irreversible action.

## Output rule
A scheduled-task prompt, release checklist and Power Automate attachment-flow specification.

## Stop conditions
Stop if the newest source is ambiguous, a source cannot be verified, totals disagree, approval is missing, or a requested action would use real credentials or recipients.
