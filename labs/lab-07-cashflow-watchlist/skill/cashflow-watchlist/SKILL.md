---
name: cashflow-watchlist
description: Combine receivables and payment schedules into a two-week cash watchlist and draft an email.
---
# Build a Cash-Flow Watchlist and Email Draft skill

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
A cashflow-watchlist.xlsx and a ready-for-review Outlook email draft.

## Stop conditions
Stop if the newest source is ambiguous, a source cannot be verified, totals disagree, approval is missing, or a requested action would use real credentials or recipients.
