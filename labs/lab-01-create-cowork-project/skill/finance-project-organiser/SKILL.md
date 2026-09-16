---
name: finance-project-organiser
description: Create a simple Cowork project with a dedicated finance folder, clear instructions and safe output locations.
---
# Create a Cowork Project for Finance Tasks skill

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
A reusable Finance Task Automation project with folder instructions and a first file inventory.

## Stop conditions
Stop if the newest source is ambiguous, a source cannot be verified, totals disagree, approval is missing, or a requested action would use real credentials or recipients.
