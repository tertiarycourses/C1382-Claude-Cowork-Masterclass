# Lab 07 — Build the Meridian Claude Project

**Topic 03 · Claude Projects**

> Meridian Capital Partners Pte Ltd — all data in this lab is synthetic and for training only.

## Goal

Everything you have built so far lives in separate places — a dashboard in your sidebar, files in Drive, a skill, and rules you have been restating by hand. In this final lab you gather them into one Cowork Project: a dedicated folder on your computer where context builds over time, and which a colleague can open and be immediately productive in.

## You'll build

A Meridian Finance Reporting project holding the data, instructions, skill and dashboard.

**Tools:** Claude Cowork, Projects, Agent Skills, Live Artefacts, Google Drive connector

## Mock data

The files for this lab are in `mock-data/`:

- `meridian-brand-guidelines.md`

Leave these files unchanged — let Claude write its output elsewhere.

## The prompt

Copy this into Claude (it is also in [PROMPT.md](PROMPT.md)):

```text
This project is Meridian Finance Reporting. Write the project
instructions that should apply to every task I run in here:

- We are the finance team at Meridian Capital Partners Pte Ltd.
  Our four revenue desks are Advisory, Asset Management, Private
  Credit and Corporate Finance.
- All money in Singapore dollars, thousands separators, no decimals.
- Variances show both the absolute figure and the percentage.
- Every report carries the title "Meridian Capital Partners" and
  the reporting period, and the footer "internal use only".
- Headings in a serif font, body text in a clean sans-serif.
- Tone: factual and concise. No marketing language.
- Always show me a draft before sending anything. Never send email
  without my explicit approval.
- The finance data in this project folder is the source of truth.

Write these as clear project instructions, then confirm what you
will now do differently in every chat in this project.
```

> **Note:** Project instructions apply to every chat in the project — you stop restating them.

## Steps

1. **In Cowork, choose New project, then Start from scratch.**
   The other two routes on that screen are Import a project (bring one over from Chat) and Use an existing folder (point Claude at a folder you already work from).
2. **In the Start a new project dialog, type the Name: Meridian Finance Reporting.**
   The dialog has four fields — Name, Instructions, Add files and Choose project location.
3. **Paste the lab prompt's rules into the Instructions box.**
   These are the standing rules — house style, SGD formatting and the approval habit — applied to every chat in the project.
4. **Under Add files, drop in the Meridian finance data and the brand guidelines.**
   Adding them once means no chat in this project has to re-attach them.
5. **Set Choose project location to where you want the folder to live, then click Create.**
   A Cowork project is backed by a real folder on your computer — you can open the files yourself at any time.
6. **Add the daily-brief skill from Lab 6 to the project.**
   The routine now travels with the project, so anyone working in it can run it.
7. **Open the project folder on your computer and confirm the files are really there.**
   This is what distinguishes a Cowork project — the instructions and files are a folder you own, not something locked inside the app.
8. **Save the FY2025 dashboard into the project so it sits with the data it reports on.**
   The artefact, its data and its rules finally live in one place.
9. **Start a fresh chat in the project and ask for a one-paragraph Q4 summary.**
   Test the payoff: no files attached, no rules restated, and the output already follows the house style.
10. **Confirm the folder holds the data, instructions, skill and dashboard, ready to share.**
   Handing a colleague this folder hands them the whole working setup.

## Check your work

A Meridian Finance Reporting project exists, backed by a folder containing the finance data and brand guidelines, with project instructions set, the daily-brief skill available and the dashboard saved. A brand-new chat in the project produces a Q4 summary in SGD with the correct header and footer without you attaching a file or restating a single rule.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
