# Lab 09 — Build the Meridian Claude Project

**Topic 03 · Claude Projects and Plugins**

> Meridian Capital Partners Pte Ltd — all data in this lab is synthetic and for training only.

## Goal

Everything you have built so far lives in separate places — a dashboard in your sidebar, files in Drive, two skills, a scheduled task, and rules you have been restating by hand. In this final lab you gather them into one Cowork Project: a dedicated folder on your computer where context builds over time, and which a colleague can open and be immediately productive in.

The project page has four panels — Instructions, Context, Folder and Scheduled — and you fill each in turn. The one worth pausing on is the difference between Context and Folder: Context holds documents Claude reads and never edits, while Folder is where it actually works.

## You'll build

A Meridian Finance Reporting project holding the data, instructions, skills and dashboard.

**Tools:** Claude Cowork, Projects, Agent Skills, Live Artefacts, Google Drive connector

## Mock data

The files for this lab are in `mock-data/`:

- `meridian-brand-guidelines.md`
- `meridian-desk-profiles.md`
- `meridian-reporting-calendar.md`
- `working/`

Leave these files unchanged — let Claude write its output elsewhere.

## The prompt

This lab has **two blocks**, used at different moments. Block 1 goes into the Create a project dialog as you make the project. Block 2 is the standing instructions you set once the project exists. Both are also in [PROMPT.md](PROMPT.md).

### Block 1 — CREATE

In the Create a project dialog, under **What are you trying to achieve?**, paste this:

```text
Quarterly finance reporting for Meridian Capital Partners Pte Ltd — a
Singapore investment firm with four desks: Advisory, Asset Management,
Private Credit and Corporate Finance. I produce revenue dashboards,
board decks and a daily briefing from the firm's finance data, all in
Singapore dollars and in the Meridian house style.
```

This is the standing context every chat in the project inherits, so you stop re-explaining who Meridian is.

### Block 2 — INSTRUCTIONS

Once the project exists, open its instructions and send this in the project:

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

1. **In Cowork, start a new project to open the Create a project dialog.**
   The dialog asks two questions and offers a folder — it is deliberately short, because the detail is set once the project exists.
2. **Under "What are you working on?", enter: Meridian Finance Reporting.**
   This is the project's name — it is how you will find it in the sidebar later.
3. **Under "What are you trying to achieve?", paste Block 1.**
   This is the standing context every chat in the project inherits, so you stop re-explaining who Meridian is.
4. **Click Create project.**
   The project now exists but is empty. Everything else is added from the project page, which has four panels down the right: Instructions, Context, Folder and Scheduled. You fill them in that order.
5. **INSTRUCTIONS — open the panel and set the standing rules with Block 2.**
   These are the house style, the SGD formatting and the approval habit, applied to every chat in the project. You stop restating them.
6. **CONTEXT — add the brand guidelines, the reporting calendar and the desk profiles.**
   Context holds documents Claude READS. It never edits them — they are reference material, which is why the brand rules and the calendar belong here rather than in the working folder.
7. **FOLDER — point the panel at the working/ folder from this lab's mock data.**
   Folder is where Claude WORKS: it reads the revenue CSV there and writes its output into working/reports/. That read-versus-write split is the difference between the two panels, and it is the part people get wrong.
8. **SCHEDULED — add the 9am daily-brief task you built in Lab 7 to the project.**
   Same feature as Lab 7, now scoped to the project: the task belongs to this body of work rather than floating loose in your account.
9. **Add the daily-brief skill from Lab 7 and the brand-deck skill from Lab 8 to the project.**
   Both routines now travel with the project, so anyone working in it can run them. Type / in the composer to see them listed.
10. **Open the project folder on your computer and confirm the files are really there.**
    This is what distinguishes a Cowork project — the instructions and files are a folder you own, not something locked inside the app.
11. **Save the FY2025 dashboard into the project so it sits with the data it reports on.**
    The artefact, its data and its rules finally live in one place.
12. **Start a fresh chat in the project and ask for a one-paragraph Q4 summary.**
    Test the payoff: no files attached, no rules restated, and the output already follows the house style.
13. **Confirm all four panels are populated and the folder is ready to share.**
    Handing a colleague this folder hands them the whole working setup.

## Check your work

A Meridian Finance Reporting project exists with all four panels populated: Instructions carries the house rules, Context holds the brand guidelines, reporting calendar and desk profiles, Folder points at the working folder with the FY2025 revenue data, and Scheduled carries the 9am daily-brief task. Both the daily-brief and brand-deck skills are available and the dashboard is saved. A brand-new chat in the project produces a Q4 summary in SGD with the correct header and footer without you attaching a file or restating a single rule.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
