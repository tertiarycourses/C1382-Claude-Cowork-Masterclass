# Lab 1 — Delegate Your First Task to Claude Cowork

- **Course:** Claude Cowork Masterclass
- **Version:** v1.0 (3 August 2026)
- **Topic 1:** Getting Started with Claude Cowork
- **Maps to:** LO1 and LO2: explain the Cowork task lifecycle and permission boundary, create a narrow project, brief a bounded file-inventory task, monitor its execution, and verify the result against the source folder
- **Tools:** Claude Cowork, Claude Desktop, local file access, File Explorer or Finder, PowerShell or Terminal, supplied Northstar Operations starter

**Duration:** 75 minutes

---

## What You Will Do

You create a personal working copy of the fictional Northstar Retail Operations folder, establish an immutable source baseline, and connect only that narrow copy to a new Cowork project. You then use the DELEGATE framework to ask Claude for a complete file inventory, review its plan before execution, watch the session for scope drift, and compare the finished manifest with the actual source files.

## What You Will Build

A protected synthetic workspace, reviewed project instructions, a complete file inventory, and a verification record.

## Prerequisites

- The latest Claude Desktop application is installed and the Cowork mode is available on your paid plan.
- On Windows, install Claude Desktop with administrator privileges for Cowork support, enable Windows Virtual Machine Platform, and Restart the computer. Ask the trainer or IT owner before changing a managed device.
- On macOS, Python 3 is installed and python3 --version succeeds; the supplied hashing and reconciliation commands require it.
- The C1382 repository is available locally and contains labs/starter/northstar-operations.
- You can create a new local folder outside the course repository for a disposable working copy.
- Use only the supplied fictional Northstar data; do not connect a personal, customer, finance, human-resources, or company drive folder.

> **Data note.** Use only the supplied fictional data. Keep inbox/ unchanged, create outputs in new folders, verify important values, and obtain clear authority before any external write, sharing action, source replacement, or removal.

## Steps

**1. From the C1382 repository root, create a new sibling working copy named C1382-northstar-workspace. Stop if the destination already exists so an earlier learner workspace is never overwritten. Move into the new copy and create the Lab 1 output folder.**

```text
Windows PowerShell:
$source = (Resolve-Path .\labs\starter\northstar-operations).Path
$target = Join-Path (Split-Path (Resolve-Path .).Path -Parent) 'C1382-northstar-workspace'
if (Test-Path -LiteralPath $target) { throw "Destination exists: $target" }
Copy-Item -Recurse -LiteralPath $source -Destination $target
Set-Location -LiteralPath $target
New-Item -ItemType Directory -Force .\outputs\lab-01 | Out-Null

macOS Terminal:
command -v python3 >/dev/null 2>&1 || { echo 'Python 3 is required; ask the trainer before continuing'; exit 1; }
python3 --version
source_dir="$(pwd)/labs/starter/northstar-operations"
target_dir="$(dirname "$(pwd)")/C1382-northstar-workspace"
test ! -e "$target_dir" || { echo "Destination exists: $target_dir"; exit 1; }
cp -R "$source_dir" "$target_dir"
cd "$target_dir"
mkdir -p outputs/lab-01
```

**2. Read 00_READ_ME_FIRST.md and management-brief.md. Confirm aloud that the scenario is fictional, inbox is the protected source set, outputs is the only writable area, and the Week 32 control values will be used later. Do not open Cowork until this boundary is clear.**

```text
Open these files in a text editor:
00_READ_ME_FIRST.md
management-brief.md
```

**3. Create a baseline manifest for the inbox before Claude receives access. Record each filename, byte length, and SHA-256 hash in outputs/lab-01/00-inbox-baseline.csv, then count the source files. Keep this file for the final comparison.**

```text
Windows PowerShell:
Get-ChildItem -LiteralPath .\inbox -File | Sort-Object Name | ForEach-Object {
  $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash
  [pscustomobject]@{Name=$_.Name; Bytes=$_.Length; SHA256=$hash}
} | Export-Csv -NoTypeInformation -Encoding utf8 .\outputs\lab-01\00-inbox-baseline.csv
(Import-Csv .\outputs\lab-01\00-inbox-baseline.csv).Count

macOS Terminal:
python3 - <<'PY'
from hashlib import sha256
from pathlib import Path
files = sorted((p for p in Path('inbox').iterdir() if p.is_file()), key=lambda p: p.name)
lines = [f"{sha256(p.read_bytes()).hexdigest()}  {p.as_posix()}\n" for p in files]
Path('outputs/lab-01/00-inbox-baseline.sha256').write_text(''.join(lines), encoding='utf-8')
print(len(files))
PY
```

**4. Open Claude Desktop and confirm it is current. Select Cowork in the message-box mode selector. In the left navigation choose Projects, choose the plus control, select Use an existing folder, and select only C1382-northstar-workspace. Name the project Northstar Operations Lab.**

```text
Project name: Northstar Operations Lab
Connected folder: <ABSOLUTE_PATH_TO_C1382-northstar-workspace>
```

**5. Add the following durable project instructions. Read the saved version back and correct any line that is missing. These are stable boundaries for all three labs, not the task brief for one run.**

```text
This project contains fictional training data for C1382. Treat inbox/ as read-only. Create or revise files only inside outputs/ and playbook/. Never remove, rename, move, or overwrite a source file. Never send, share, publish, upload, or connect another system without explicit approval in the current task. Separate source evidence, inference, and unresolved questions. Label unsupported business claims OWNER TO VERIFY. Before reporting completion, list created files and the checks performed.
```

**6. Start a new task inside the project. Paste the task brief below. It requires a plan before work and limits the first task to inventory; do not ask Claude to organise, analyse, or write a management report yet.**

```text
Outcome: Create a reliable inventory of the protected inbox for an operations manager.

Sources: Read 00_READ_ME_FIRST.md, management-brief.md, and every file directly inside inbox/. Do not read outside this connected project.

Deliverables: Create outputs/lab-01/01-file-inventory.md with a table containing filename, type, reporting period, apparent purpose, key fields or sections, likely owner, sensitivity note, and any ambiguity. Create outputs/lab-01/01-file-inventory.csv with the same source rows and these columns: filename, type, reporting_period, apparent_purpose, key_fields_or_sections, likely_owner, sensitivity_note, ambiguity. End the Markdown file with source count, likely duplicates, missing expected inputs, and questions for an owner.

Constraints: Treat inbox/ as read-only. Do not rename, move, remove, overwrite, reorganise, or summarise the business results. Do not use external sources. Put uncertain classifications in an Unknown or OWNER TO VERIFY state instead of guessing.

Process: First show your plan, intended reads and two intended writes. Wait for my approval. After approval, execute the plan.

Evidence: Account for every direct inbox file exactly once in each inventory, name both created files, and state how you checked completeness.
```

**7. Review Claude's plan against the task contract. It should read only the named local files and write the Markdown and CSV inventories in outputs/lab-01. If the plan includes source changes, broad folder access, external research, or another destination, steer it with the correction below. Approve only when the route matches the boundary.**

```text
Revise the plan to remain inside the connected C1382-northstar-workspace. Read the named sources only. Leave inbox/ unchanged. Create only outputs/lab-01/01-file-inventory.md and outputs/lab-01/01-file-inventory.csv. Treat ambiguity as OWNER TO VERIFY. Show the corrected read set and write set, then wait again.
```

**8. Allow the bounded plan to run. Watch the progress indicators, filenames, and tool requests. If Claude asks for another folder, an external connection, a deletion, or a write outside outputs/lab-01, deny it and restate the boundary. When the task finishes, open the actual inventory file rather than relying on the completion message.**

```text
Expected output paths:
outputs/lab-01/01-file-inventory.md
outputs/lab-01/01-file-inventory.csv
```

**9. Compare the machine-readable inventory with the source directory as a multiset. Continue only when the filename sets and counts match exactly, every source appears once, no extra or duplicate row exists, and the Markdown table agrees with the CSV. Ask for a focused revision if any check fails.**

```text
Windows PowerShell:
$sourceNames = @(Get-ChildItem -LiteralPath .\inbox -File | Sort-Object Name | Select-Object -ExpandProperty Name)
$inventoryNames = @((Import-Csv .\outputs\lab-01\01-file-inventory.csv) | ForEach-Object { $_.filename })
$duplicates = @($inventoryNames | Group-Object | Where-Object Count -ne 1)
$diff = @(Compare-Object ($sourceNames | Sort-Object) ($inventoryNames | Sort-Object))
if ($duplicates -or $diff -or $sourceNames.Count -ne $inventoryNames.Count) {
  $duplicates | Format-Table Name,Count
  $diff | Format-Table -AutoSize
  throw 'Inventory is not an exact one-row-per-source match'
}
$markdown = Get-Content -LiteralPath .\outputs\lab-01\01-file-inventory.md -Raw
$badMentions = @($sourceNames | Where-Object { ([regex]::Matches($markdown,[regex]::Escape($_))).Count -ne 1 })
if ($badMentions) { $badMentions; throw 'Markdown inventory does not mention every source exactly once' }
'PASS exact filename multiset match; no duplicates or extras'

macOS Terminal:
python3 - <<'PY'
from collections import Counter
from pathlib import Path
import csv
source = sorted(p.name for p in Path('inbox').iterdir() if p.is_file())
with open('outputs/lab-01/01-file-inventory.csv', newline='', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))
inventory = [row['filename'] for row in rows]
if Counter(source) != Counter(inventory) or len(source) != len(inventory):
    raise SystemExit(f'FAIL source={Counter(source)} inventory={Counter(inventory)}')
markdown = Path('outputs/lab-01/01-file-inventory.md').read_text(encoding='utf-8')
bad = [name for name in source if markdown.count(name) != 1]
if bad:
    raise SystemExit(f'FAIL Markdown occurrences: {bad}')
print('PASS exact filename multiset match; no duplicates or extras')
PY
```

**10. Recalculate the inbox hashes and compare them with the baseline. Create outputs/lab-01/01-verification.md with the project name, connected folder, source count, inventory path, filename check, baseline comparison, any denied requests, and the final result. Use a truthful note if your operating system used the alternative hash file.**

```text
Windows PowerShell:
$before = Import-Csv .\outputs\lab-01\00-inbox-baseline.csv
$after = Get-ChildItem -LiteralPath .\inbox -File | Sort-Object Name | ForEach-Object {
  [pscustomobject]@{Name=$_.Name; Bytes=$_.Length; SHA256=(Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash}
}
$diff = Compare-Object $before $after -Property Name,Bytes,SHA256
@"
# Lab 1 Verification

- Project: Northstar Operations Lab
- Connected folder: $((Resolve-Path .).Path)
- Source count: $($after.Count)
- Inventories: outputs/lab-01/01-file-inventory.md and outputs/lab-01/01-file-inventory.csv
- Exact filename multiset match in both inventories: <YES_OR_DETAILS>
- Inbox hash comparison: $(if ($diff) {'CHANGED - REVIEW REQUIRED'} else {'UNCHANGED'})
- Denied or corrected scope requests: <NONE_OR_DETAILS>
- Result: <VERIFIED_OR_ACTION_REQUIRED>
"@ | Set-Content -Encoding utf8 .\outputs\lab-01\01-verification.md
if ($diff) { $diff | Format-Table -AutoSize } else { 'Inbox unchanged' }

macOS Terminal:
shasum -a 256 -c outputs/lab-01/00-inbox-baseline.sha256
# Then create outputs/lab-01/01-verification.md with the same fields in a text editor.
```

**11. Close the loop in Cowork. Ask Claude to compare the task contract with the finished state and report only the deliverable, checks, limitations, and remaining owner questions. Add any useful omission to the verification record without changing inbox.**

```text
Compare the original task brief with the current workspace. Do not create or change a file. Report: (1) the deliverable path, (2) completeness evidence, (3) boundary evidence, (4) unresolved OWNER TO VERIFY items, and (5) one improvement to the next task brief.
```

## Test It

Open outputs/lab-01/01-file-inventory.md and 01-file-inventory.csv and confirm both contain one row for every direct inbox file and no duplicate or extra rows. Confirm the Markdown file contains the expected columns, source count, duplicate observations, missing-input observations, and owner questions. Run the executable filename-multiset comparison and require PASS. Run the hash comparison and confirm the protected inbox is unchanged. Open outputs/lab-01/01-verification.md and confirm it records the project, connected folder, source count, both inventory paths, exact filename result, hash result, scope interventions, and final verified state.

## Checkpoint for the Next Lab

Keep the connected C1382-northstar-workspace, unchanged inbox, reviewed project instructions, 00-inbox-baseline file, 01-file-inventory.md, 01-file-inventory.csv, and 01-verification.md. Lab 2 uses this complete verified source boundary to build the management-ready pack.

## Troubleshooting

- **Cowork is not visible:** Confirm you are signed in to a paid plan, update Claude Desktop, restart the application, and ask the organisation owner whether Cowork is enabled. Use the web surface only if the trainer confirms it provides the required capability for this lab.
- **Cowork is unavailable on Windows or reports a virtualization error:** Confirm Claude Desktop was installed with administrator privileges. In an elevated PowerShell window, run Get-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform. If the approved IT procedure permits it and the feature is disabled, run Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -All, then use Restart rather than shut down. On a managed device, ask IT to make the change; do not bypass policy.
- **python3 is unavailable on macOS:** Stop before creating the baseline. Install an organisation-approved Python 3 build and confirm python3 --version, or use the trainer-supported Windows route. Do not substitute a weaker hash or skip the executable controls.
- **Projects or Use an existing folder is not visible:** Update Claude Desktop. If the project feature is unavailable on the current surface, start a Cowork task on desktop, connect only the working-copy folder, paste the same instructions at the start, and record the limitation in 01-verification.md.
- **The folder selector points at the course repository:** Cancel and select the sibling C1382-northstar-workspace only. The course repository contains build sources that are outside the lab's data boundary.
- **Claude proposes moving or renaming files:** Do not approve the plan. Restate that Lab 1 is inventory-only, inbox is protected, and the only permitted writes are outputs/lab-01/01-file-inventory.md and outputs/lab-01/01-file-inventory.csv.
- **A filename is absent from the inventory:** Provide the exact missing filename and ask Claude for a focused inventory revision. Rerun the complete filename comparison after the revision.
- **The hash comparison reports a change:** Stop. Identify the changed source file from the comparison, restore the working copy from labs/starter/northstar-operations, regenerate the baseline, and rerun Lab 1. Never copy a changed training source back into the course repository.

## Challenge

Extend 01-verification.md with a file-type count derived from 01-file-inventory.csv, then compare that count with the Markdown summary. Explain any Unknown classification without changing a source file.

## Reflection

Which part of the task contract prevented the largest possible scope error, and which observable check proved that the boundary held?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-turn-a-messy-folder-into-a-management-ready-report.md)
