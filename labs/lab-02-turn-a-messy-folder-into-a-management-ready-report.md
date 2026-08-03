# Lab 2 — Turn a Messy Folder into a Management-Ready Report

- **Course:** Claude Cowork Masterclass
- **Version:** v1.0 (3 August 2026)
- **Topic 2:** Automating Everyday Work with Cowork
- **Maps to:** LO3: organise a working copy, analyse spreadsheet data with defined metrics, synthesise notes and feedback with provenance, and produce a reconciled spreadsheet, report, and presentation from one fact base
- **Tools:** Claude Cowork, local files, spreadsheet creation and analysis, document creation, presentation creation, spreadsheet and office viewers

**Duration:** 105 minutes

---

## What You Will Do

You use the verified Northstar workspace from Lab 1 to run a staged, end-to-end management-reporting workflow. Claude inventories and organises a working copy, creates a source register and calculation workbook, pauses for a human reconciliation gate, then produces a written operations report and a short leadership presentation whose facts, period, terminology, and actions agree.

## What You Will Build

A reconciled Week 32 workbook, source and evidence registers, management report, leadership brief, quality review, and run log.

## Prerequisites

- Lab 1 is complete or its rejoin baseline has been reconstructed and verified.
- outputs/lab-01/01-file-inventory.md accounts for every direct inbox file.
- outputs/lab-01/01-file-inventory.csv contains the same exact one-row-per-source filename set.
- The current inbox hashes match outputs/lab-01/00-inbox-baseline.csv or its macOS equivalent.
- The Northstar Operations Lab project instructions still restrict writes to outputs/ and playbook/.
- On macOS, python3 --version succeeds; the independent controls and revision-hash records require Python 3.

> **Rejoin path.** If a prerequisite artifact is missing, use the Rejoin Path in [the labs index](README.md), reconstruct the named checkpoint, and verify it before continuing.

> **Data note.** Use only the supplied fictional data. Keep inbox/ unchanged, create outputs in new folders, verify important values, and obtain clear authority before any external write, sharing action, source replacement, or removal.

## Steps

**1. Open C1382-northstar-workspace and verify the Lab 1 checkpoint. Confirm the inventory and verification files exist, the verification state is clear, and the protected inbox still matches the baseline. Create the new output directory only after the check succeeds.**

```text
Windows PowerShell:
$required = @('.\outputs\lab-01\00-inbox-baseline.csv','.\outputs\lab-01\01-file-inventory.md','.\outputs\lab-01\01-file-inventory.csv','.\outputs\lab-01\01-verification.md')
$required | ForEach-Object { if (-not (Test-Path -LiteralPath $_)) { throw "Missing checkpoint: $_" } }
$verification = Get-Content -LiteralPath .\outputs\lab-01\01-verification.md -Raw
if ($verification -notmatch 'Result:\s*VERIFIED') { throw 'Lab 1 verification is not in a verified state' }
$before = Import-Csv .\outputs\lab-01\00-inbox-baseline.csv
$after = Get-ChildItem .\inbox -File | Sort-Object Name | ForEach-Object { [pscustomobject]@{Name=$_.Name;Bytes=$_.Length;SHA256=(Get-FileHash -Algorithm SHA256 $_.FullName).Hash} }
if (Compare-Object $before $after -Property Name,Bytes,SHA256) { throw 'Inbox changed; restore the verified checkpoint' }
New-Item -ItemType Directory -Force .\outputs\lab-02 | Out-Null

macOS Terminal:
set -euo pipefail
command -v python3 >/dev/null 2>&1 || { echo 'Python 3 is required; ask the trainer before continuing'; exit 1; }
python3 --version
for f in outputs/lab-01/00-inbox-baseline.sha256 outputs/lab-01/01-file-inventory.md outputs/lab-01/01-file-inventory.csv outputs/lab-01/01-verification.md; do test -f "$f" || { echo "Missing $f"; exit 1; }; done
grep -Eq 'Result:[[:space:]]*VERIFIED' outputs/lab-01/01-verification.md || { echo 'Lab 1 is not verified'; exit 1; }
shasum -a 256 -c outputs/lab-01/00-inbox-baseline.sha256
mkdir -p outputs/lab-02

105-minute phase budget: checkpoint and controls 15; Stage 1 execution 25; reconciliation gate 15; Stage 2 generation 25; visual review and revisions 20; final close-out 5. If Stage 1 has not reconciled by minute 55, compare your calculations with checkpoints/lab-02-stage1-control.md, correct the failing calculation or source mapping, and continue only after the human gate passes.
```

**2. Read management-brief.md and brand-style.md. In outputs/lab-02/02-quality-review.md, create headings for source scope, metric reconciliation, workbook review, report review, presentation review, cross-artifact consistency, inbox comparison, and owner questions. This file is your independent review record, not Claude's completion summary.**

```text
Create this file in a text editor:
outputs/lab-02/02-quality-review.md

Required headings:
# Lab 2 Quality Review
## Source scope
## Metric reconciliation
## Workbook review
## Report review
## Presentation review
## Cross-artifact consistency
## Inbox comparison
## Owner questions
## Final result
```

**3. Calculate the Week 32 control totals directly from northstar-sales-w32.csv. Record the values in the Metric reconciliation section before Claude creates the workbook. Use weighted rates from the total numerators and denominators, not the average of location percentages.**

```text
Windows PowerShell:
$rows = Import-Csv .\inbox\northstar-sales-w32.csv
$orders = ($rows | Measure-Object orders -Sum).Sum
$onTime = ($rows | Measure-Object fulfilled_on_time -Sum).Sum
$revenue = ($rows | Measure-Object revenue_sgd -Sum).Sum
$returns = ($rows | Measure-Object returns -Sum).Sum
$hours = ($rows | Measure-Object labour_hours -Sum).Sum
[pscustomobject]@{Orders=$orders;OnTime=$onTime;RevenueSGD=$revenue;Returns=$returns;LabourHours=$hours;OnTimeRate=('{0:P2}' -f ($onTime/$orders));ReturnRate=('{0:P2}' -f ($returns/$orders));RevenuePerOrder=('{0:N2}' -f ($revenue/$orders))} | Format-List
$rows | Where-Object { [double]$_.fulfilled_on_time / [double]$_.orders -lt 0.95 } | ForEach-Object { '{0}: {1:P2}' -f $_.location,([double]$_.fulfilled_on_time/[double]$_.orders) }

macOS Terminal:
python3 - <<'PY'
import csv
with open('inbox/northstar-sales-w32.csv', newline='', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))
def total(name): return sum(float(r[name]) for r in rows)
orders, on_time = total('orders'), total('fulfilled_on_time')
revenue, returns = total('revenue_sgd'), total('returns')
hours = total('labour_hours')
print(f'Orders = {orders:.0f}')
print(f'Fulfilled on time = {on_time:.0f}')
print(f'Revenue = SGD {revenue:.0f}')
print(f'Returns = {returns:.0f}')
print(f'Labour hours = {hours:.0f}')
print(f'On-time fulfilment = {on_time/orders:.2%}')
print(f'Return rate = {returns/orders:.2%}')
print(f'Revenue per order = SGD {revenue/orders:.2f}')
print('Exceptions below 95%:')
for row in rows:
    rate = float(row['fulfilled_on_time']) / float(row['orders'])
    if rate < 0.95: print(f"{row['location']}: {rate:.2%}")
PY

Expected controls:
Orders = 2000
Fulfilled on time = 1856
Revenue = SGD 339350
Returns = 113
Labour hours = 2733
On-time fulfilment = 92.80%
Return rate = 5.65%
Revenue per order = SGD 169.68
Exceptions below 95% = Orchard 94.05%, Jurong 90.41%, and Woodlands 87.30%
```

**4. Return to the Northstar Operations Lab project and start a new Cowork task. Paste the staged brief below. It requires three independent extraction workstreams and a pause after the workbook so the narrative cannot outrun reconciled evidence.**

```text
Outcome: Turn the protected Week 32 Northstar inputs into a management-ready operating pack for the Head of Operations.

Approved sources: management-brief.md, brand-style.md, outputs/lab-01/01-file-inventory.md, inbox/northstar-sales-w32.csv, inbox/customer-feedback-w32.csv, and inbox/operations-notes-w32.md. These six paths are the complete read set. Do not read, analyse, cite, or copy any Week 33 file in this task. Do not use external sources.

Stage 1 workstreams that may run in parallel:
A. File workstream - create outputs/lab-02/organised-copy/ with copies of the three Week 32 inputs and the two stable brief/style files, classified into data, notes, feedback, and reference. Leave inbox unchanged. Create outputs/lab-02/02-source-register.md with source, period, purpose, use, and limitation.
B. Data workstream - create outputs/lab-02/02-operations-analysis.xlsx with sheets Read Me, Raw Sales, KPI Summary, Location Detail, Feedback, and Sources. Preserve raw rows. Use formulas where practical. Define every KPI and show control totals.
C. Evidence workstream - create outputs/lab-02/02-evidence-register.md with observation or theme, evidence type, exact source and location, confidence, inference, OWNER TO VERIFY item, and intended downstream use.

Required Week 32 KPIs: total orders, fulfilled-on-time orders, weighted on-time fulfilment rate, revenue, returns, weighted return rate, labour hours, revenue per order, and location exceptions against the targets in management-brief.md.

Human gate: First show your plan, exact read set, write set, workstream dependencies, and checks. Wait for approval. After approval, complete Stage 1 only. Pause and show the source register, evidence register, workbook paths, KPI values, exceptions, formula or calculation method, and unresolved questions. Do not draft the report or presentation until I approve Stage 2.

Stage 2 deliverables after later approval: outputs/lab-02/02-management-report.docx, outputs/lab-02/02-leadership-brief.pptx, and outputs/lab-02/02-run-log.md. Follow brand-style.md and management-brief.md. Do not send, share, publish, remove, or overwrite anything.
```

**5. Review the proposed plan. Confirm that the three Stage 1 workstreams read the same frozen source set, write to distinct destinations, and merge through the source register and KPI summary. Confirm that report and presentation work wait for the metric gate. Correct the plan if any source write, external source, or premature narrative appears.**

```text
The approved route must show:
- only the three named Week 32 inputs and the stable brief/style files are content sources; Week 33 is excluded
- inbox/ is read-only and organised-copy/ contains copies only
- source and evidence registers have distinct destinations and jointly form shared evidence
- the workbook preserves raw rows and definitions
- Stage 1 pauses before the report and slides
- no send, share, publish, removal, or overwrite action

If needed, say: Revise the plan to match these six conditions, show the corrected read and write sets, and wait again.
```

**6. Approve Stage 1 and let Claude execute. Monitor the paths and intervening questions. When Claude pauses, open 02-source-register.md, 02-evidence-register.md, and 02-operations-analysis.xlsx. Confirm the workbook contains the six promised sheets; the source register accounts for every file used; and the evidence register gives exact provenance, separates evidence from inference, and identifies every OWNER TO VERIFY item. Do not approve Stage 2 from the completion message alone.**

```text
Expected Stage 1 paths:
outputs/lab-02/organised-copy/
outputs/lab-02/02-source-register.md
outputs/lab-02/02-evidence-register.md
outputs/lab-02/02-operations-analysis.xlsx
```

**7. Reconcile the workbook with your independent controls. Check the reporting period, total orders, fulfilled-on-time orders, revenue, returns, labour hours, weighted rates, and revenue per order. Confirm Orchard, Jurong, and Woodlands are clearly identified as on-time exceptions and that the calculation does not average location percentages. Record the observed workbook cells and results in 02-quality-review.md.**

```text
Expected workbook values:
- Reporting period: Week 32
- Orders: 2,000
- Fulfilled on time: 1,856
- On-time fulfilment: 92.80%
- Revenue: SGD 339,350
- Returns: 113
- Return rate: 5.65%
- Labour hours: 2,733
- Revenue per order: SGD 169.68
- On-time exceptions: Orchard 94.05%, Jurong 90.41%, and Woodlands 87.30%

Record the actual sheet and cell for each value in outputs/lab-02/02-quality-review.md.
```

**8. If a value, formula, sheet, source reference, or exception is wrong, give Claude a focused discrepancy report. Require correction in the workbook and source register only, then repeat the complete reconciliation. Approve Stage 2 only after every control matches or an unresolved item is explicitly labelled for an owner.**

```text
Focused correction template:
Stage 1 is not approved yet. In <FILE_AND_LOCATION>, I observed <ACTUAL>. The control is <EXPECTED> because <DEFINITION_OR_SOURCE>. Correct the root calculation or source mapping, preserve the raw rows, update any dependent Stage 1 view, and show the revised values and checks. Do not begin Stage 2.
```

**9. Approve Stage 2 with the final evidence contract below. It requires the report and slides to use the reconciled workbook, cite the source register, distinguish fact from inference, and keep recommendations reviewable.**

```text
Stage 1 is approved. Complete Stage 2 using only the reconciled workbook, source register, and evidence register as the fact base.

Report: Create outputs/lab-02/02-management-report.docx with title, period, executive summary, KPI table, location exceptions, customer-feedback themes, evidence-based drivers, three prioritised recommendations, owner and timing fields, risks, OWNER TO VERIFY items, methodology, and source and evidence register references.

Presentation: Create outputs/lab-02/02-leadership-brief.pptx with 5 to 7 slides: title, executive scorecard, exceptions, customer and operational evidence, recommended actions, decisions and owner questions. Use concise headlines and the style rules in brand-style.md.

Run log: Create outputs/lab-02/02-run-log.md listing sources read, files created, metric definitions, control checks, corrections, assumptions, owner questions, and confirmation that inbox was unchanged.

Do not invent root causes, commitments, owners, dates, or external facts. Use OWNER TO VERIFY where the supplied sources do not resolve a claim. Do not send, share, or publish the artifacts.
```

**10. Open the actual Word document and presentation in compatible applications. Review the complete report for structure, page breaks, clipped or blank content, metric consistency, evidence labels, and actionable recommendations. Review every slide for readable text, clean layout, consistent period and values, a decision arc, and no unsupported claim. Record specific findings in 02-quality-review.md.**

```text
Visual review checklist:
Report - title and period; complete sections; readable tables; no blank pages; no clipped text; sources and methodology; OWNER TO VERIFY items.
Slides - 5 to 7 slides; readable at normal presentation size; no overlaps; no cut-off text; same Week 32 values; clear decisions and owner questions.
Cross-artifact - same metric names, units, rounding, locations, targets, recommendations, and source period.
```

**11. Before requesting a revision, record pre-revision hashes for every Stage 1 and Stage 2 artifact. Then give Claude one evidence-based revision request for every real defect. Name the file, location, observed issue, expected state, and invariant that must remain unchanged. After revision, reopen every changed artifact and repeat the full cross-artifact check.**

```text
Windows PowerShell:
$reviewFiles = Get-ChildItem .\outputs\lab-02 -File | Where-Object Name -Match '^02-(?!pre-revision-hashes)'
$reviewFiles | Sort-Object Name | ForEach-Object { [pscustomobject]@{Name=$_.Name;SHA256=(Get-FileHash -Algorithm SHA256 $_.FullName).Hash} } | Export-Csv -NoTypeInformation -Encoding utf8 .\outputs\lab-02\02-pre-revision-hashes.csv

macOS Terminal:
python3 - <<'PY'
from hashlib import sha256
from pathlib import Path
folder = Path('outputs/lab-02')
excluded = {'02-pre-revision-hashes.sha256', '02-post-revision-hashes.sha256'}
files = sorted((p for p in folder.glob('02-*') if p.is_file() and p.name not in excluded), key=lambda p: p.name)
Path(folder/'02-pre-revision-hashes.sha256').write_text(''.join(f"{sha256(p.read_bytes()).hexdigest()}  {p.as_posix()}\n" for p in files), encoding='utf-8')
print(f'Recorded {len(files)} pre-revision hashes')
PY

Revision template:
Revise <FILE>. At <PAGE_SLIDE_SHEET_OR_SECTION>, I observed <ISSUE>. Change it to <EXPECTED_STATE>. Preserve the verified Week 32 source set, control totals, metric definitions, source and evidence registers, and every other correct section. After saving, list the exact changes and rerun the cross-artifact consistency check.
```

**12. Recalculate the inbox hashes against the Lab 1 baseline. Complete the Inbox comparison, Owner questions, and Final result sections in 02-quality-review.md. Ask Claude for a read-only final reconciliation across the workbook, report, presentation, source register, and run log, then compare its report with your own record.**

```text
Windows PowerShell:
$before = Import-Csv .\outputs\lab-01\00-inbox-baseline.csv
$after = Get-ChildItem .\inbox -File | Sort-Object Name | ForEach-Object { [pscustomobject]@{Name=$_.Name;Bytes=$_.Length;SHA256=(Get-FileHash -Algorithm SHA256 $_.FullName).Hash} }
$diff = Compare-Object $before $after -Property Name,Bytes,SHA256
if ($diff) { $diff | Format-Table -AutoSize; throw 'Inbox changed' } else { 'Inbox unchanged' }
$afterRevision = Get-ChildItem .\outputs\lab-02 -File | Where-Object Name -Match '^02-(?!pre-revision-hashes)' | Sort-Object Name | ForEach-Object { [pscustomobject]@{Name=$_.Name;SHA256=(Get-FileHash -Algorithm SHA256 $_.FullName).Hash} }
$beforeRevision = Import-Csv .\outputs\lab-02\02-pre-revision-hashes.csv
Compare-Object $beforeRevision $afterRevision -Property Name,SHA256 | Format-Table -AutoSize

macOS Terminal:
shasum -a 256 -c outputs/lab-01/00-inbox-baseline.sha256
python3 - <<'PY'
from hashlib import sha256
from pathlib import Path
folder = Path('outputs/lab-02')
excluded = {'02-pre-revision-hashes.sha256', '02-post-revision-hashes.sha256'}
files = sorted((p for p in folder.glob('02-*') if p.is_file() and p.name not in excluded), key=lambda p: p.name)
Path(folder/'02-post-revision-hashes.sha256').write_text(''.join(f"{sha256(p.read_bytes()).hexdigest()}  {p.as_posix()}\n" for p in files), encoding='utf-8')
print(f'Recorded {len(files)} post-revision hashes')
PY
diff -u outputs/lab-02/02-pre-revision-hashes.sha256 outputs/lab-02/02-post-revision-hashes.sha256 || true

Record which hashes changed and why in 02-quality-review.md. A requested revision should change only the intended artifacts.

Cowork prompt:
Read the current Lab 2 artifacts without changing them. Reconcile reporting period, KPI definitions, values, rounding, exception locations, recommendations, owner questions, source references, and file list across 02-operations-analysis.xlsx, 02-management-report.docx, 02-leadership-brief.pptx, 02-source-register.md, 02-evidence-register.md, and 02-run-log.md. Report every mismatch; if none, state the checks performed and any remaining limitation.
```

## Test It

Confirm outputs/lab-02 contains organised-copy and the seven named artifacts: source register, evidence register, workbook, report, presentation, quality review, and run log. Confirm organised-copy contains only the named Week 32 inputs and stable brief/style files, with no Week 33 file. Reconcile the workbook to 2,000 orders, 1,856 fulfilled on time, SGD 339,350 revenue, 113 returns, 2,733 labour hours, 92.80% on-time fulfilment, 5.65% return rate, and SGD 169.68 revenue per order; confirm Orchard, Jurong, and Woodlands are the on-time exceptions. Open and visually inspect the report and every slide. Confirm period, values, definitions, exception locations, recommendations, and owner questions agree across the workbook, report, presentation, source register, evidence register, and run log. Confirm the inbox hash comparison is unchanged, the before/after hash record explains intended revisions, and 02-quality-review.md records every check and the final result.

## Checkpoint for the Next Lab

Keep the verified Lab 2 package and unchanged inbox. Lab 3 derives a reusable weekly-operations playbook from this run, changes the reporting-week parameter to Week 33, and proves the workflow can repeat without copying Week 32 conclusions.

## Troubleshooting

- **Claude begins the report before the metric gate:** Steer immediately: stop Stage 2, retain any draft as non-authoritative, reconcile Stage 1, then replace the draft from the approved workbook rather than editing unsupported claims in place.
- **The workbook averages location rates:** Require weighted totals: sum fulfilled_on_time divided by sum orders, and sum returns divided by sum orders. Preserve each location's rate for exception analysis but do not average those percentages for the overall rate.
- **A generated file will not open:** Ask Claude to regenerate that one artifact in the same required format and path from the reconciled fact base. Keep the source register and verified workbook unchanged, then reopen the replacement.
- **The report invents a cause or owner:** Replace the unsupported statement with an evidence-labelled inference or OWNER TO VERIFY item. Add the question and intended owner to the report and quality review.
- **The slide deck is dense or clipped:** Request a focused layout revision: shorten headlines and body copy, split one overloaded slide, preserve the decision arc and all verified values, then inspect every slide again.
- **Values disagree across files:** Treat the reconciled workbook as the numerical source of truth and the source register as the provenance source. Ask Claude to rebuild the dependent report and slide statements, then rerun the full cross-artifact check.

## Challenge

Ask Claude to add an executive dashboard sheet with one trend-free Week 32 scorecard, target variance, conditional formatting, and a plain-language data dictionary. Verify that the dashboard does not imply a time trend from one week of data and that every value reconciles to the existing KPI Summary.

## Reflection

Which intermediate artifact made the final pack most trustworthy, and why would generating all three formats in one unreviewed step have increased risk?

---

[← Lab 1](lab-01-delegate-your-first-task-to-claude-cowork.md) · [Lab 3 →](lab-03-build-a-repeatable-cowork-workflow-for-your-own-work.md)
