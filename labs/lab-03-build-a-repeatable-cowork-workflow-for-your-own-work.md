# Lab 3 — Build a Repeatable Cowork Workflow for Your Own Work

- **Course:** Claude Cowork Masterclass
- **Version:** v1.0 (3 August 2026)
- **Topic 3:** Advanced Cowork Workflows
- **Maps to:** LO4 and LO5: convert a successful multi-step session into a parameterised playbook, choose tools and integrations deliberately, control parallel work with human gates, rerun the workflow on a new period, and define a safe team rollout
- **Tools:** Claude Cowork projects, project instructions, local files, parallel workstreams, office artifact creation, optional trusted connectors, human review gates

**Duration:** 85 minutes

---

## What You Will Do

You turn the verified Lab 2 run into a reusable weekly-operations playbook instead of saving one long prompt. The playbook defines parameters, source contracts, parallel workstreams, dependency gates, deliverables, control checks, exception paths, and ownership. You then change the reporting-week parameter to Week 33, run the workflow, reconcile the new outputs, and document whether local files, connectors, browser actions, or scheduled execution are appropriate.

## What You Will Build

A parameterised playbook, integration decision, verified Week 33 pack, quality record, and bounded rollout plan.

## Prerequisites

- Labs 1 and 2 are complete or the Lab 3 rejoin baseline has been reconstructed and verified.
- The protected inbox matches the Lab 1 baseline and the Lab 2 quality review has a clear final state.
- The Lab 2 workbook reconciles to the Week 32 controls and the report and presentation agree with it.
- Week 33 source files are present in inbox/ and have not been analysed or altered for this lab.
- On macOS, python3 --version succeeds; the independent controls and revision-hash records require Python 3.

> **Rejoin path.** If a prerequisite artifact is missing, use the Rejoin Path in [the labs index](README.md), reconstruct the named checkpoint, and verify it before continuing.

> **Data note.** Use only the supplied fictional data. Keep inbox/ unchanged, create outputs in new folders, verify important values, and obtain clear authority before any external write, sharing action, source replacement, or removal.

## Steps

**1. Verify the connected checkpoint before deriving a reusable process. Confirm the Lab 2 artifacts and quality review exist, read the final result and remaining owner questions, and recalculate the inbox hash comparison. Create the playbook and Week 33 output directories only after the source boundary is confirmed.**

```text
Windows PowerShell:
$required = @('.\outputs\lab-01\00-inbox-baseline.csv','.\outputs\lab-01\01-file-inventory.md','.\outputs\lab-01\01-file-inventory.csv','.\outputs\lab-01\01-verification.md','.\outputs\lab-02\02-source-register.md','.\outputs\lab-02\02-evidence-register.md','.\outputs\lab-02\02-operations-analysis.xlsx','.\outputs\lab-02\02-management-report.docx','.\outputs\lab-02\02-leadership-brief.pptx','.\outputs\lab-02\02-quality-review.md','.\outputs\lab-02\02-run-log.md','.\inbox\northstar-sales-w33.csv','.\inbox\customer-feedback-w33.csv','.\inbox\operations-notes-w33.md')
$required | ForEach-Object { if (-not (Test-Path -LiteralPath $_)) { throw "Missing checkpoint: $_" } }
$before = Import-Csv .\outputs\lab-01\00-inbox-baseline.csv
$after = Get-ChildItem .\inbox -File | Sort-Object Name | ForEach-Object { [pscustomobject]@{Name=$_.Name;Bytes=$_.Length;SHA256=(Get-FileHash -Algorithm SHA256 $_.FullName).Hash} }
if (Compare-Object $before $after -Property Name,Bytes,SHA256) { throw 'Inbox changed; restore the verified checkpoint' }
New-Item -ItemType Directory -Force .\playbook, .\outputs\lab-03\week-33 | Out-Null

macOS Terminal:
set -euo pipefail
command -v python3 >/dev/null 2>&1 || { echo 'Python 3 is required; ask the trainer before continuing'; exit 1; }
python3 --version
for f in outputs/lab-01/00-inbox-baseline.sha256 outputs/lab-01/01-file-inventory.md outputs/lab-01/01-file-inventory.csv outputs/lab-01/01-verification.md outputs/lab-02/02-source-register.md outputs/lab-02/02-evidence-register.md outputs/lab-02/02-operations-analysis.xlsx outputs/lab-02/02-management-report.docx outputs/lab-02/02-leadership-brief.pptx outputs/lab-02/02-quality-review.md outputs/lab-02/02-run-log.md inbox/northstar-sales-w33.csv inbox/customer-feedback-w33.csv inbox/operations-notes-w33.md; do test -f "$f" || { echo "Missing $f"; exit 1; }; done
shasum -a 256 -c outputs/lab-01/00-inbox-baseline.sha256
mkdir -p playbook outputs/lab-03/week-33

85-minute phase budget: checkpoint and playbook 18; integration and project rules 7; independent controls and Stage 1 15; reconciliation gate 7; Stage 2 artifact generation 13; artifact and visual review 10; rollout planning 7; final reconciliation, hash review, release decision, and close-out 8. If the playbook is not approved by minute 20, adapt checkpoints/lab-03-playbook-starter.md. If Stage 1 has not reconciled by minute 47, use checkpoints/lab-03-week33-reconciliation.md to locate and correct the mismatch. If Stage 2 is incomplete by minute 62, use checkpoints/lab-03-stage2-review-checkpoint.md to focus the remaining review; no checkpoint replaces either human gate.
```

**2. In the Northstar Operations Lab project, ask Claude to inspect the task brief, run log, quality review, source register, and final artifacts from Lab 2 without changing them. Require it to distinguish stable workflow rules from Week 32-specific parameters and conclusions.**

```text
Read these Lab 2 artifacts without changing files: 02-source-register.md, 02-evidence-register.md, 02-quality-review.md, 02-run-log.md, the workbook structure and definitions, the report structure, and the presentation structure. Produce a response with two tables: (A) stable workflow elements that should repeat every week, and (B) Week 32-specific parameters, values, exceptions, and conclusions that must never be copied into a new run. Cite the artifact behind each item.
```

**3. Ask Claude to draft the reusable workflow files below. The playbook must describe a process, not preserve Week 32 results. Project instructions must remain concise and durable. The quality checklist must contain observable checks and a named evidence location for each stage.**

```text
Using the stable elements you identified, create three files.

1. playbook/weekly-operations-review.md with: purpose; owner; trigger; parameters REPORTING_WEEK, SOURCE_FOLDER, OUTPUT_FOLDER, AUDIENCE, and TARGET_SET; required-source contract; stop conditions; three parallel extraction workstreams; dependency and reconciliation gate; artifact-generation stage; draft-review gate; deliverables; metric definitions; quality checks; exception paths; run log; release owner; and version history.

2. playbook/project-instructions.md with no more than 12 concise rules covering synthetic or approved data, read-only sources, output boundaries, evidence versus inference, weighted rates, owner verification, human gates, no external action without approval, run logs, and final reconciliation.

3. playbook/quality-checklist.md as a table with stage, check, expected evidence, owner, and response when the check fails. Include source completeness, freshness, control totals, weighted rates, formula preservation, cross-artifact consistency, visual review, inbox comparison, unresolved questions, and release decision.

Do not copy Week 32 values, exception locations, or recommendations into reusable rules. Do not change the project settings yet.
```

**4. Review the three files. Search for Week 32 values, location conclusions, or recommendations that were accidentally hard-coded. Confirm the playbook contains every required parameter, gate, exception path, and owner. Revise the files before using them if any required element is missing or any old conclusion survives.**

```text
Windows PowerShell:
Select-String -Path .\playbook\*.md -Pattern '339,350|92.80|5.65|Woodlands|Jurong' -CaseSensitive:$false

Expected result: no Week 32 value or exception is encoded as a reusable rule. A location name may appear only in an explicitly labelled example that cannot affect execution; remove it for this lab.

Manual playbook check:
- five parameters present
- source contract and stop conditions present
- parallel workstreams and dependency gate present
- reconciliation and draft-review gates present
- deliverables and metric definitions present
- exception paths, owner, run log, and version history present
```

**5. Create an integration decision record with Claude. Require one row each for local files, a remote connector, a desktop capability, browser interaction, computer use, and scheduled execution. For this lab, choose an on-demand local-file run. Distinguish a remote built-in schedule, which cannot be tied to a computer folder, from a manually configured schedule that requires local files or apps and therefore runs only locally. Any future schedule requires an approved source, an available execution surface, and a fresh control review.**

```text
Create playbook/integration-decision.md as a decision table with capability, candidate use, data location, access scope, read or write actions, reliability, key risk, human gate, fallback, owner, and decision. Include local connected folder, remote connector, desktop capability, browser interaction, computer use, and scheduled task.

Decision for this training run: use the connected local working copy on demand; use no external connector, browser action, computer use, or scheduled task. Record both scheduling modes: remote built-in schedules run without the computer and must use connectors or files saved to the Claude account, not a computer folder; a manually configured schedule that requires local files or apps runs locally and depends on the local device and required app being available. Before either mode is approved, review source access, freshness, availability, monitoring, failure handling, and release authority.
```

**6. Compare playbook/project-instructions.md with the current project instructions. In the Cowork project settings, update the instructions only after reading the final text. Preserve the original local-source protections, and do not paste Week 32 values or the Week 33 task brief into durable instructions.**

```text
Project-instruction review:
- stable across reporting weeks
- no metric values or location conclusions
- no broad folder or connection authority
- explicit read-only source and output rules
- explicit evidence, owner-verification, and release gates

Then paste the reviewed contents of playbook/project-instructions.md into the Northstar Operations Lab project instructions and save.
```

**7. Calculate Week 33 control totals independently from northstar-sales-w33.csv and record them in a new outputs/lab-03/03-week-33-quality-review.md before the run. This proves the playbook processes a new period instead of repeating Week 32 values.**

```text
Windows PowerShell:
$rows = Import-Csv .\inbox\northstar-sales-w33.csv
$orders = ($rows | Measure-Object orders -Sum).Sum
$onTime = ($rows | Measure-Object fulfilled_on_time -Sum).Sum
$revenue = ($rows | Measure-Object revenue_sgd -Sum).Sum
$returns = ($rows | Measure-Object returns -Sum).Sum
$hours = ($rows | Measure-Object labour_hours -Sum).Sum
$controls = [pscustomobject]@{Orders=$orders;OnTime=$onTime;RevenueSGD=$revenue;Returns=$returns;LabourHours=$hours;OnTimeRate=('{0:P2}' -f ($onTime/$orders));ReturnRate=('{0:P2}' -f ($returns/$orders));RevenuePerOrder=('{0:N2}' -f ($revenue/$orders))}
$controls | Format-List
@"
# Week 33 Quality Review

## Independent controls
$($controls | Format-List | Out-String)
## Source contract
## Reconciliation gate
## Draft-review gate
## Artifact and visual review
## Cross-artifact consistency
## Revision hash comparison
## Inbox comparison
## Exceptions and owner questions
## Release decision
"@ | Set-Content -Encoding utf8 .\outputs\lab-03\03-week-33-quality-review.md

macOS Terminal:
python3 - <<'PY'
from pathlib import Path
import csv
with open('inbox/northstar-sales-w33.csv', newline='', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))
def total(name): return sum(float(r[name]) for r in rows)
orders, on_time = total('orders'), total('fulfilled_on_time')
revenue, returns = total('revenue_sgd'), total('returns')
hours = total('labour_hours')
lines = [
    '# Week 33 Quality Review', '', '## Independent controls',
    f'- Orders: {orders:.0f}', f'- Fulfilled on time: {on_time:.0f}',
    f'- Revenue: SGD {revenue:.0f}', f'- Returns: {returns:.0f}',
    f'- Labour hours: {hours:.0f}', f'- On-time fulfilment: {on_time/orders:.2%}',
    f'- Return rate: {returns/orders:.2%}', f'- Revenue per order: SGD {revenue/orders:.2f}',
    '', '### Exceptions below 95%',
]
lines += [f"- {r['location']}: {float(r['fulfilled_on_time'])/float(r['orders']):.2%}" for r in rows if float(r['fulfilled_on_time'])/float(r['orders']) < .95]
lines += ['', '## Source contract', '## Reconciliation gate', '## Draft-review gate', '## Artifact and visual review', '## Cross-artifact consistency', '## Revision hash comparison', '## Inbox comparison', '## Exceptions and owner questions', '## Release decision']
Path('outputs/lab-03/03-week-33-quality-review.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('\n'.join(lines[:15]))
PY

Expected controls:
Orders = 2100
Fulfilled on time = 1985
Revenue = SGD 358050
Returns = 101
Labour hours = 2777
On-time fulfilment = 94.52%
Return rate = 4.81%
Revenue per order = SGD 170.50
Exceptions below 95% = Woodlands 90.91% and Jurong 92.11%
```

**8. Start a new Cowork task and run the playbook with explicit Week 33 parameters. Require a plan and source-contract check first, then a pause at the reconciliation gate. The workstreams may run in parallel, but dependent narrative work must wait.**

```text
Run playbook/weekly-operations-review.md with these parameters:
REPORTING_WEEK = Week 33
SOURCE_FOLDER = inbox
OUTPUT_FOLDER = outputs/lab-03/week-33
AUDIENCE = Head of Operations
TARGET_SET = the targets in management-brief.md

Use only inbox/northstar-sales-w33.csv, inbox/customer-feedback-w33.csv, inbox/operations-notes-w33.md, management-brief.md, and brand-style.md. Do not use Week 32 values, exception locations, or recommendations as evidence for Week 33.

First show the parameter resolution, exact source set, write set, parallel workstreams, dependencies, stop conditions, two human gates, and quality checks. Wait for approval. After approval, complete Stage 1 and create only source-register.md, evidence-register.md, operations-analysis.xlsx, and reconciliation.md in the Week 33 output folder. Pause at the reconciliation gate with those four paths, the calculated controls, exceptions, and unresolved questions. Do not generate the report, slides, or run log until I approve the gate.
```

**9. Review and approve the plan only if it resolves the correct Week 33 files and paths. After extraction, compare Claude's reconciliation with the independent controls. Confirm the overall rates are weighted and the workflow identified Week 33 exceptions from Week 33 data. Record the checks, discrepancies, corrections, and approval decision in 03-week-33-quality-review.md.**

```text
Required Stage 1 paths:
- outputs/lab-03/week-33/source-register.md
- outputs/lab-03/week-33/evidence-register.md
- outputs/lab-03/week-33/operations-analysis.xlsx
- outputs/lab-03/week-33/reconciliation.md

Expected Week 33 reconciliation:
- Orders: 2,100
- Fulfilled on time: 1,985
- Revenue: SGD 358,050
- Returns: 101
- Labour hours: 2,777
- Weighted on-time fulfilment: 94.52%
- Weighted return rate: 4.81%
- Revenue per order: SGD 170.50
- On-time exceptions against 95%: Woodlands 90.91% and Jurong 92.11%

If any path or value differs, do not approve the gate. Give the observed and expected state, metric definition, and source file; require a focused correction and rerun all controls.
```

**10. Approve Stage 2 only after the reconciliation gate. The source register, evidence register, workbook, and reconciliation already exist from Stage 1; Stage 2 creates only the report, presentation, and run log. Require a second pause at the draft-review gate before any release decision.**

```text
Reconciliation gate approved. Continue the playbook and create only these remaining Week 33 artifacts inside outputs/lab-03/week-33:
- management-report.docx
- leadership-brief.pptx
- run-log.md

Use the four approved Stage 1 artifacts as the reconciled Week 33 fact base. Preserve the playbook's structures, definitions, checks, and owner fields, but derive all values, exceptions, customer themes, and recommendations from Week 33 sources. In run-log.md, record the exact Stage 1 gate evidence and decision. Pause at the draft-review gate. Do not share, send, publish, replace a source, or mark the pack released.
```

**11. At the draft-review gate, open the workbook, document, and every slide. Run the quality checklist: file presence, source completeness, formulas and controls, metric definitions, period labels, evidence versus inference, owner questions, layout, cross-artifact consistency, and inbox comparison. Before any revision, record hashes for all seven Week 33 artifacts. Record exact locations for defects and request focused revisions. Repeat every affected check after a change. After the reviewer makes the draft-review decision, update the run log with the actual second-gate evidence before final reconciliation.**

```text
Windows PowerShell:
Get-ChildItem .\outputs\lab-03\week-33 -File | Sort-Object Name | ForEach-Object { [pscustomobject]@{Name=$_.Name;SHA256=(Get-FileHash -Algorithm SHA256 $_.FullName).Hash} } | Export-Csv -NoTypeInformation -Encoding utf8 .\outputs\lab-03\03-pre-revision-hashes.csv

macOS Terminal:
python3 - <<'PY'
from hashlib import sha256
from pathlib import Path
folder = Path('outputs/lab-03/week-33')
files = sorted((p for p in folder.iterdir() if p.is_file()), key=lambda p: p.name)
Path('outputs/lab-03/03-pre-revision-hashes.sha256').write_text(''.join(f"{sha256(p.read_bytes()).hexdigest()}  {p.as_posix()}\n" for p in files), encoding='utf-8')
print(f'Recorded {len(files)} pre-revision hashes')
PY

Artifact review:
- all seven named files exist: source and evidence registers, reconciliation, workbook, report, presentation, and run log
- every artifact says Week 33
- workbook and reconciliation agree with the independent controls
- report and slides use 94.52%, 4.81%, SGD 358,050, and the same rounding
- no Week 32 value or conclusion appears as Week 33 evidence
- source register names the Week 33 inputs
- unsupported claims are labelled OWNER TO VERIFY
- report has no blank or clipped page
- slides have no overlap, cut-off text, or unreadable density

After all revisions and repeated checks, record the draft-review decision in 03-week-33-quality-review.md. Then say:
Update only outputs/lab-03/week-33/run-log.md. Record the actual draft-review gate reviewer, evidence examined, corrections, decision, date and time, and precisely permitted next action. Do not invent approval, share a file, or change another artifact. Reopen run-log.md and verify this second-gate record before continuing.
```

**12. Ask Claude for a read-only final reconciliation. Compare its evidence with your quality review, then make the release decision for the local training pack. The decision authorises only retaining the files in the workspace; it does not authorise sharing or any external action.**

```text
Read the Week 33 artifacts, playbook, quality checklist, and current quality review without changing them. Reconcile the source set, period, metric definitions, values, rounding, exceptions, recommendations, owner questions, file list, gate decisions, and run log. Report mismatches and limitations. If none remain, state the evidence for local training-pack readiness. Do not share, send, publish, or change a file.
```

**13. Create the rollout plan with Claude, then edit it to your own work context without naming real data or credentials. Keep the first pilot draft-only and bounded. Include a baseline, owner, approved source class, access process, evidence, review burden, monitoring, incident response, and stop conditions.**

```text
Create outputs/lab-03/03-rollout-plan.md for a four-week pilot of one recurring knowledge-work process. Include: use-case boundary and non-goals; accountable owner and reviewers; permitted data classes and prohibited data; source and access provisioning; task and playbook owner; current time and quality baseline; draft-only Week 1 run; success and guardrail metrics; human gates; run evidence; exception and incident response; access removal; weekly review; version control; criteria to continue, narrow, pause, or stop. Use placeholders rather than real names, systems, data, or credentials.
```

**14. Run the final inbox hash comparison and inspect the project for all promised outputs. Complete the quality review's Inbox comparison, Exceptions and owner questions, and Release decision sections. Record one playbook improvement discovered during the Week 33 run and update the playbook version history to v1.1 only if you actually make that improvement.**

```text
Windows PowerShell:
$before = Import-Csv .\outputs\lab-01\00-inbox-baseline.csv
$after = Get-ChildItem .\inbox -File | Sort-Object Name | ForEach-Object { [pscustomobject]@{Name=$_.Name;Bytes=$_.Length;SHA256=(Get-FileHash -Algorithm SHA256 $_.FullName).Hash} }
if (Compare-Object $before $after -Property Name,Bytes,SHA256) { throw 'Inbox changed' } else { 'Inbox unchanged' }
$postRevision = Get-ChildItem .\outputs\lab-03\week-33 -File | Sort-Object Name | ForEach-Object { [pscustomobject]@{Name=$_.Name;SHA256=(Get-FileHash -Algorithm SHA256 $_.FullName).Hash} }
$postRevision | Export-Csv -NoTypeInformation -Encoding utf8 .\outputs\lab-03\03-post-revision-hashes.csv
Compare-Object (Import-Csv .\outputs\lab-03\03-pre-revision-hashes.csv) $postRevision -Property Name,SHA256 | Format-Table -AutoSize
Get-ChildItem .\playbook -File | Select-Object Name,Length
Get-ChildItem .\outputs\lab-03\week-33 -File | Select-Object Name,Length
if (-not (Test-Path .\outputs\lab-03\03-week-33-quality-review.md)) { throw 'Missing quality review' }
if (-not (Test-Path .\outputs\lab-03\03-rollout-plan.md)) { throw 'Missing rollout plan' }

macOS Terminal:
set -euo pipefail
shasum -a 256 -c outputs/lab-01/00-inbox-baseline.sha256
python3 - <<'PY'
from hashlib import sha256
from pathlib import Path
folder = Path('outputs/lab-03/week-33')
files = sorted((p for p in folder.iterdir() if p.is_file()), key=lambda p: p.name)
Path('outputs/lab-03/03-post-revision-hashes.sha256').write_text(''.join(f"{sha256(p.read_bytes()).hexdigest()}  {p.as_posix()}\n" for p in files), encoding='utf-8')
print(f'Recorded {len(files)} post-revision hashes')
PY
diff -u outputs/lab-03/03-pre-revision-hashes.sha256 outputs/lab-03/03-post-revision-hashes.sha256 || true
find playbook outputs/lab-03 -maxdepth 2 -type f -print
test -f outputs/lab-03/03-week-33-quality-review.md
test -f outputs/lab-03/03-rollout-plan.md

Record which artifact hashes changed and why in the Revision hash comparison section. Only intended revision targets should differ. Confirm run-log.md contains the actual second-gate reviewer, evidence, decision, time, and permitted next action before making the release decision.
```

## Test It

Confirm the four playbook files contain the required parameters, source contract, workstreams, dependencies, two human gates, deliverables, controls, exception paths, ownership, and tool decision, with no Week 32 conclusion hard-coded. Confirm Stage 1 produced source-register.md, evidence-register.md, operations-analysis.xlsx, and reconciliation.md before approval, then Stage 2 produced management-report.docx, leadership-brief.pptx, and run-log.md. Reconcile the seven Week 33 artifacts to 2,100 orders, 1,985 fulfilled on time, SGD 358,050 revenue, 101 returns, 2,777 labour hours, 94.52% on-time fulfilment, 4.81% return rate, and SGD 170.50 revenue per order. Open and visually inspect the report and every slide, confirm the registers, reconciliation, and run log describe Week 33, confirm both human gates are recorded, confirm the pre/post revision hash comparison explains only intended changes, confirm the inbox is unchanged, and confirm the rollout plan names the bounded use case, data rules, owner, baseline, evidence, monitoring, incident response, and stop criteria.

## Checkpoint for the Next Lab

Retain the verified local Week 33 pack, playbook files, quality review, and rollout plan as the final C1382 learning portfolio. Before applying the workflow to real work, obtain the relevant data and system approvals, substitute an explicitly approved source contract, and rerun every control in a draft-only pilot.

## Troubleshooting

- **The playbook contains Week 32 values or recommendations:** Remove results from the reusable procedure. Replace them with parameters, definitions, target references, and instructions for deriving the new period's exceptions.
- **Parallel workstreams produce conflicting definitions:** Stop at the dependency gate. Select the definitions in the playbook, reconcile the upstream outputs, update the shared source register and control sheet, then restart dependent work.
- **Week 33 output repeats a Week 32 conclusion:** Treat it as contamination from prior context. Name the copied claim, require Claude to locate Week 33 evidence, remove unsupported carry-over, and rerun the complete reconciliation across every artifact.
- **A scheduled run cannot access its source:** Keep this lab on demand while diagnosing the execution mode. A remote built-in schedule cannot be tied to a computer folder, so use an approved connector or a file saved to the Claude account. A manually configured schedule that requires local files or apps runs locally, so confirm the device and required app are available. Re-review access, freshness, monitoring, failure handling, and release authority before enabling either route.
- **A connector is unavailable or not approved:** Use the local synthetic source for this lab. Record the connector as Not approved or Not available in integration-decision.md and keep the workflow's source contract independent of that tool.
- **The project instructions become a long task prompt:** Keep only durable rules that apply across reporting weeks. Move parameters, sources, audience, and one-run deliverables back into the task invocation.
- **The run log omits a human gate:** Do not declare the local pack ready. Add the actual reviewer, evidence examined, decision, time, and permitted next action; never fabricate an approval that did not occur.

## Challenge

If the trainer provides an approved connector to a synthetic cloud folder, clone the playbook as a connector variant. Compare source resolution, access scope, evidence, latency, failure mode, and fallback with the local run. Do not add a real business connection and do not enable a schedule during class.

## Reflection

Which element transformed the successful Lab 2 session into an operational playbook, and where did the Week 33 run reveal that a saved prompt alone would not have been enough?

---

[← Lab 2](lab-02-turn-a-messy-folder-into-a-management-ready-report.md) · [Labs index →](README.md)
