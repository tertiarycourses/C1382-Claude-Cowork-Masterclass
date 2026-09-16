# Lab 02 — Pull the Latest Finance Data and Refresh Excel

**C1382 · Topic 1 · 55 minutes**

## Goal
Find the newest dated finance file, update an Excel dashboard and refresh its charts.

## What you will build
An updated monthly-finance-dashboard.xlsx with current KPIs and two charts.

## Prerequisites
Open this lab folder as the Cowork project context. Read `TOOLS.md`, enable the named skill in `skill/latest-finance-dashboard/SKILL.md`, and use only the fictional files in `mock-data/`.

## Steps
1. Open `TOOLS.md` and confirm the available tools and access boundary.
2. Review the files in `mock-data/`; copy any file you will change into `working/`.
3. Add or enable `skill/latest-finance-dashboard/SKILL.md` in the Cowork project.
4. Open `prompts/prompt-02.txt`, paste the prompt into Cowork and review its proposed plan.
5. Allow only the reads and writes needed for this lab. Keep consequential actions paused.
6. Open the generated files and compare them with `CHECKLIST.md`. Correct any mismatch in the output, then repeat the check.
7. Save the finished artifacts in `outputs/` and record the evidence used.

## Test it
The output identifies 2026-09 as latest, displays September revenue S$128,000, expenses S$89,500 and net S$38,500, and contains refreshed charts.

## Troubleshooting
- **Cowork selects the wrong file:** name the expected date format and require it to list candidates before choosing.
- **A workbook does not refresh:** open it in Excel, recalculate, and ask Cowork to inspect formulas and chart source ranges.
- **A claim has no source:** remove it or add a direct file, cell or URL reference.

## Challenge
Change the reporting period or audience and rerun the task without changing the skill's stable rules.

## Reflection
Which part of this task should always remain a human review point?
