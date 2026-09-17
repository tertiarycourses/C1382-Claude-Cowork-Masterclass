# Claude Cowork Masterclass — Learner Guide

**Course Code:** C1382  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v3.1 · 17 September 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Claude Cowork Fundamentals](#topic-01--claude-cowork-fundamentals)
  - [Lab 1 — Process a Folder of Invoices](#lab-1--process-a-folder-of-invoices)
  - [Lab 2 — Your First Live Artefact](#lab-2--your-first-live-artefact)
  - [Lab 3 — The Meridian Sales Dashboard](#lab-3--the-meridian-sales-dashboard)
- [Topic 02 — Tools and Skills](#topic-02--tools-and-skills)
  - [Lab 4 — Connect Google Drive](#lab-4--connect-google-drive)
  - [Lab 5 — Refresh the Dashboard and Send the Summary](#lab-5--refresh-the-dashboard-and-send-the-summary)
  - [Lab 6 — Build a /daily-brief Skill](#lab-6--build-a-daily-brief-skill)
- [Topic 03 — Claude Projects](#topic-03--claude-projects)
  - [Lab 7 — Build the Meridian Claude Project](#lab-7--build-the-meridian-claude-project)
- [Wrap-Up](#wrap-up)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

Claude Cowork is the desktop agent in the Claude family built for people who work with files and reports rather than code. This course teaches it through one continuous scenario: you are on the finance team at Meridian Capital Partners Pte Ltd, and over seven labs you process a year of invoices, build a live sales dashboard, connect it to the firm's data in Google Drive, deliver an approved summary by Gmail, wrap that routine into a reusable daily-brief skill, and finish by gathering everything into one Claude Project your whole team can work from.

Meridian Capital Partners is a fictitious Singapore-based investment and advisory firm with four revenue desks — Advisory, Asset Management, Private Credit and Corporate Finance. All figures, clients, staff and documents in this course are synthetic and used for training only.


## Course Learning Outcomes

- LO1: Set up the Cowork desktop workspace and have Claude process a folder of documents into a structured summary.
- LO2: Build, save and download a Live Artefact, including an interactive sales dashboard from supplied data.
- LO3: Connect the Google Drive connector so Claude can read finance data held outside the chat.
- LO4: Refresh a Live Artefact from connected data and send an approved summary with the Gmail connector.
- LO5: Turn a verified routine into an Agent Skill with /skill-creator, update it, and explain a skill's three layers.
- LO6: Assemble a Claude Project that holds the data, instructions, skill and dashboard as one reusable team workspace.


## Before You Start — Preparation

**What you need**

- A laptop (Mac or Windows) with the Claude desktop app installed from claude.ai/download.
- A Claude account on a paid plan — Cowork and Live Artefacts are paid-plan desktop features.
- A Google account with Google Drive and Gmail, used for the connector labs.
- The lab folder for this course, copied to your machine.

**Verify your setup**

Open the Claude desktop app, sign in, and confirm you can see Cowork in the sidebar. Ask Claude to build a small test artefact and check it appears in the preview pane beside the chat. If it does, your setup is ready.

**Conventions used in every lab**

- Prompts shown in a bordered box are meant to be copied into Claude as they are.
- Placeholders such as <YOUR FOLDER> are replaced with your own values.
- All Meridian Capital data is synthetic; use only the supplied mock data.
- Every lab ends with a check step — confirm the output before moving on.


## Topic 01 — Claude Cowork Fundamentals

The Claude family · Cowork setup · Live Artefacts · working with documents

**Key concepts**

- ('Claude Cowork', 'The desktop agent that works on your files and tasks — built for non-developers, not coders.')
- ('Live Artefacts', 'Interactive tools that persist in your workspace and refresh their data when reopened.')
- ('Desktop, not browser', 'Live Artefacts and local file access need the Claude desktop app on a paid plan.')
- ("Describe, don't code", 'You describe the tool you want in plain English; Claude writes and runs the code.')
- ('Save to the sidebar', 'A saved artefact is reopenable and reusable — it is not lost in the chat history.')
- ('Download to share', 'Export the artefact so it can be filed, attached or handed to someone without Claude.')


### Lab 1 — Process a Folder of Invoices

Learning outcome: extract structured data from a folder of PDFs and reorganise the files.

Goal: Meridian's accountant needs the 2025 supplier invoices summarised and filed. You point Cowork at a folder of 126 PDFs — a full year of invoices, a few expense receipts, and the untidy filenames a real downloads folder collects — and have it read every document, build one CSV, and sort the files into month folders. This is work no dashboard can do: reading documents and acting on your file system. It is also far more than you would ever do by hand, which is the point.

**What you'll build**

An invoices_2025.csv summary plus the PDFs filed into YEAR-MONTH folders.   (Tools: Claude Cowork, local files, PDF reading.)

**The prompt**

Copy the block below into Claude exactly as it is.

```text
In this folder are all my invoices from 2025. I need you to process
these so I can send them to my accountant.

Read each invoice and extract the following data points:

- invoice number
- invoice sender
- invoice sender address
- invoice date
- invoice due date
- total amount due
- currency

Then create a CSV called invoices_2025.csv where you store all this
information as well as the filename.

After you have extracted the information, move each invoice PDF into
sub folders based on the YEAR-MONTH of the invoice date, using the
naming convention 2025-01, 2025-02 and so on.

Flag anything that does not look like a normal supplier invoice, or
that you think I should check. Do not delete any file.
```

> **Note:** Work on a copy of the folder — tell Claude to move files, never to delete them.

**Step-by-step**

1. Open the Claude desktop app, sign in, and choose Cowork in the sidebar.  —  Cowork is a desktop feature on a paid plan — the browser version cannot reach your files.
2. Copy the lab's "2025 Invoices" folder somewhere you can work on it.  —  Always run a file-moving task against a copy the first time, so a mistake costs nothing.
3. Open the folder yourself and skim it before you start — 126 files.  —  Two have machine-generated names and one looks like a duplicate. You cannot check 126 documents by hand, but you can check that the summary adds up.
4. Start a Cowork session pointed at that folder, then paste the lab prompt.  —  Cowork needs access to the folder itself, not an attachment, because it must move files as well as read them.
5. Let Claude work through the PDFs — this one takes a few minutes.  —  It is reading each document, not guessing from the filename, which is why the oddly-named files still land correctly.
6. Open invoices_2025.csv and check the row count against the folder.  —  Expect 121 invoice rows — 117 in SGD and 4 in USD — with the receipts and the duplicate flagged rather than silently mixed in.
7. Total the SGD column and compare it against S$777,954.81.  —  Spot-check a few rows against the PDFs too: a total that reconciles tells you the extraction held across all 126 files.
8. Check the currency column — four invoices are in US dollars.  —  Never sum a mixed-currency column. This is exactly the kind of thing a human check is for.
9. Confirm the PDFs now sit in 2025-01 … 2025-12 folders and nothing was deleted.  —  The file dates come from inside each document, so a file named Jan can still be filed by its real invoice date.
10. Read Claude's list of flagged items and decide what to do about each.  —  Claude surfaces the exceptions; you make the call — that is the working relationship this course is teaching.

**Test it**

invoices_2025.csv lists every invoice with all seven fields plus the filename. The 117 SGD invoices total S$777,954.81; the four USD invoices are marked USD rather than added to that total. The duplicated invoice and the four expense receipts are flagged rather than counted as ordinary invoices. The PDFs now sit in 2025-01 … 2025-12 folders and all 126 files are still present.

> **Note:** Full commands and screenshots are in labs/lab-01-*.md. Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.

---


### Lab 2 — Your First Live Artefact

Learning outcome: set up the Cowork workspace and build, save and download a Live Artefact.

Goal: Now you have seen Cowork do a real piece of work, meet the other thing it makes: a Live Artefact. You build a small tool rather than ask a question, so you can see how an artefact differs from a chat answer — it persists, it is interactive, it pulls fresh data every time you open it, and you can save and download it.

**What you'll build**

A saved, downloaded Live Artefact — an FX converter on live rates.   (Tools: Claude desktop app, Claude Cowork, Live Artefacts.)

**The prompt**

Copy the block below into Claude exactly as it is.

```text
Build me a Live Artefact: a currency converter for Meridian Capital
Partners that uses the LATEST exchange rates, not fixed ones.

Requirements:
- Convert between SGD, USD, EUR and GBP.
- Fetch current rates from a free, no-key exchange rate API each time
  the artefact is opened, and refresh them when I click a Refresh
  button.
- One amount box, a from-currency and a to-currency selector, and a
  large result.
- Under the result show the rate used and the time the rates were
  last fetched.
- If the rate lookup fails, say so plainly and show the last rate you
  had rather than a wrong number.
- Clean, professional finance styling. Label it "Meridian Capital
  Partners".

Make it interactive so I can change the amount and see the result update.
```

> **Note:** Because the rates are live, your figures will differ from the screenshots — that is the point of a Live Artefact.

**Step-by-step**

1. Start a new Cowork session — this lab needs no files.  —  Lab 1 gave Claude a folder to work in; here you are asking it to build something from nothing.
2. Paste the lab prompt into the composer and send it.  —  Claude writes the code and renders the converter in the preview pane beside the chat.
3. Try the converter: change the amount and switch the currencies.  —  This is what makes it an artefact rather than an answer — you can interact with it.
4. Check the live rate against a search for "1 USD to SGD".  —  The artefact fetched this rate seconds ago, so it should match. A fixed rate in a spreadsheet would already be out of date.
5. Click Refresh, and note the 'last fetched' time updates.  —  This is the 'Live' in Live Artefact — reopening or refreshing pulls current data rather than replaying a snapshot.
6. Ask for one refinement in plain English, for example: Add a thousands separator to the result.  —  Refining by conversation is the normal way to work — you never edit the code yourself.
7. Save the artefact so it appears in your sidebar.  —  A saved artefact persists as a reusable tool; an unsaved one scrolls away with the chat.
8. Download a copy of the artefact to your lab folder.  —  Downloading gives you a file you can keep, attach or hand to someone without Claude.

**Test it**

Converting S$10,000 to USD gives a figure that matches a live search for the SGD/USD rate, and the artefact shows when the rates were last fetched. Clicking Refresh updates that time. The artefact appears in your sidebar after saving, still works when you reopen it, and a downloaded copy is in your lab folder.

> **Note:** Full commands and screenshots are in labs/lab-02-*.md. Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.

---


### Lab 3 — The Meridian Sales Dashboard

Learning outcome: turn supplied finance data into an interactive Live Artefact dashboard.

Goal: Meridian's head of finance wants to see how the four revenue desks performed this year without opening a spreadsheet. You take the supplied sales data and build it into a Live Artefact dashboard — KPI tiles, a trend chart and a desk breakdown — then save it. This dashboard is the artefact every later lab builds on.

**What you'll build**

A saved Live Artefact dashboard showing Meridian's FY2025 revenue by desk.   (Tools: Claude Cowork, Live Artefacts, local files.)

**The prompt**

Copy the block below into Claude exactly as it is.

```text
Using the attached meridian-sales-fy2025.csv, build me a Live Artefact:
an interactive sales dashboard for Meridian Capital Partners.

Include:
- KPI tiles: total revenue, total deals, average deal size, best desk.
- A monthly revenue trend chart for the full year.
- A breakdown of revenue by desk (Advisory, Asset Management,
  Private Credit, Corporate Finance).
- A filter to show one desk at a time or all desks.

Format all money as Singapore dollars with thousands separators.
Use a clean, professional finance layout. Title it
"Meridian Capital Partners — FY2025 Revenue".
```

> **Note:** Attach the CSV from your lab's mock-data folder before sending the prompt.

**Step-by-step**

1. Open the lab folder and look at meridian-sales-fy2025.csv so you know what the data holds.  —  Always know your source before you ask Claude to summarise it — that is how you spot a wrong figure later.
2. Start a Cowork session and attach the CSV, or point Claude at the lab folder.  —  Scope Claude to the one folder for this task rather than your whole drive.
3. Paste the lab prompt and send it.  —  Claude reads the file, works out the totals and builds the dashboard in the preview pane.
4. Check the KPI tiles against the CSV: total revenue should be S$24,850,000 across 214 deals.  —  This is the verification habit — read the artefact's numbers back against the source.
5. Use the desk filter to view Advisory on its own, then return to all desks.  —  Interactivity is the point of a Live Artefact: the reader explores instead of asking you for another cut.
6. Refine the layout in plain English, for example: Move the KPI tiles above the chart.  —  Keep refining by conversation until the dashboard reads the way you want it to.
7. Save the dashboard to your sidebar with a clear name, then download a copy.  —  You will refresh this same artefact from connected data in Lab 5.

**Test it**

The dashboard shows total revenue S$24,850,000 and 214 deals, Advisory is the best desk at S$8,420,000, the desk filter changes the chart, and the artefact reopens from your sidebar after you close it.

> **Note:** Full commands and screenshots are in labs/lab-03-*.md. Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.

---


## Topic 02 — Tools and Skills

Google Drive · Gmail · Agent Skills · /skill-creator · a reusable /daily-brief automation

**Key concepts**

- ('Connectors', 'Toggle Gmail, Calendar and Drive on from the + menu so Claude can reach data outside the chat.')
- ('Google Drive', 'Claude reads Sheets, Docs, Slides and PDFs from Drive, and can upload files back to a folder.')
- ('Scope the folder', 'Point Claude at one Drive folder for the task — not your whole Drive.')
- ('Gmail', 'Claude drafts, sends, replies and labels — sending asks for explicit approval by default.')
- ('Agent Skills', 'A folder of instructions Claude loads on demand, so a task runs the same way every time.')
- ('Three layers', 'Metadata is always in context; the SKILL.md loads when triggered; resources load only when needed.')
- ('/skill-creator', 'Do the task once, verify the output, then let skill-creator write the SKILL.md for you.')
- ('Skills evolve', 'Update a skill as you learn what you want — saving over it replaces the old version, so re-run to confirm.')
- ('Skills use tools', 'A skill can drive the connectors for you — one command that checks Drive and Gmail and reports back.')


### Lab 4 — Connect Google Drive

Learning outcome: enable the Google Drive connector and read finance data held outside the chat.

Goal: Meridian's finance data does not live on your laptop — it sits in a shared Google Drive folder. You upload the firm's wider finance files to Drive, enable the Google Drive connector, and confirm Claude can read them without you attaching anything by hand.

**What you'll build**

A working Google Drive connection scoped to the Meridian finance folder.   (Tools: Claude Cowork, Google Drive connector.)

**The prompt**

Copy the block below into Claude exactly as it is.

```text
Using the Google Drive connector, open the folder "Meridian Finance"
in my Drive and tell me what you find.

For each file, give me:
- The file name and what kind of data it holds.
- The period it covers.
- The three figures you would use in a quarterly revenue summary.

Do not change, move or delete anything — read only.
List anything that looks inconsistent between the files.
```

> **Note:** Claude asks for approval before it moves, shares or deletes a Drive file.

**Step-by-step**

1. Upload the lab's mock-data files to a new Google Drive folder named Meridian Finance.  —  The lab supplies the quarterly workbook, the desk targets and the client list as mock data.
2. In Claude, click the plus sign in the composer and hover over Connectors.  —  This is where you turn individual connectors on and off for your account.
3. Toggle Google Drive on and sign in to your Google account.  —  On a Team or Enterprise plan an owner must enable connectors for the organisation first.
4. Approve the permissions Google asks for.  —  Approve only what you are willing to let Claude reach — you can revoke access later.
5. Paste the lab prompt so Claude reads the Meridian Finance folder.  —  Naming the folder scopes the task; Claude does not need access to your whole Drive.
6. Compare Claude's file summary against what you actually uploaded.  —  Confirm it found every file and read the right periods before you rely on it.
7. Note any inconsistency Claude reports between the files.  —  The Q4 Advisory target deliberately disagrees between two files — a real check.

**Test it**

Claude lists all three Meridian Finance files with their periods, reports FY2025 revenue of S$24,850,000, and flags that the Q4 Advisory target disagrees between the two files — S$2,320,000 in the targets file against S$2,410,000 in the workbook. Nothing in Drive has been changed.

> **Note:** Full commands and screenshots are in labs/lab-04-*.md. Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.

---


### Lab 5 — Refresh the Dashboard and Send the Summary

Learning outcome: update the Live Artefact from connected data and deliver an approved summary by Gmail.

Goal: Quarter end has arrived. You refresh the dashboard you built in Lab 3 using the data Claude now reads from Drive, then have it draft a quarterly summary email to the head of finance. You read the draft against the figures and approve it before a single message leaves your outbox.

**What you'll build**

An updated dashboard plus an approved quarterly summary email sent to yourself.   (Tools: Claude Cowork, Live Artefacts, Google Drive connector, Gmail connector.)

**The prompt**

Copy the block below into Claude exactly as it is.

```text
Two tasks, in order.

1. Open my saved "Meridian Capital Partners — FY2025 Revenue"
   dashboard and update it from the Meridian Finance folder in Google
   Drive. Add a Q4 column to the desk breakdown and show each desk's
   actual against its target.

2. Then draft an email to <YOUR OWN ADDRESS> with the subject
   "Meridian FY2025 — Q4 revenue summary". In the body:
   - Total FY2025 revenue and the Q4 figure.
   - Each desk's Q4 actual against target, best and worst first.
   - Two sentences explaining the largest variance.
   - A closing line noting the Q4 Advisory target discrepancy.

Show me the draft. Do not send it until I approve it.
```

> **Note:** Replace <YOUR OWN ADDRESS> with your own email — never a real client's.

**Step-by-step**

1. Reopen the dashboard you saved in Lab 3 from your sidebar.  —  You are extending the artefact you already built, not starting a new one.
2. Enable the Gmail connector from the plus menu, alongside Google Drive.  —  Turn on only the connectors this task needs.
3. Paste the lab prompt, replacing the placeholder with your own email address.  —  Class exercises always go to a test recipient — yourself.
4. Watch Claude refresh the dashboard from Drive and add the Q4 target comparison.  —  The data comes from the connector now; you are not attaching files by hand.
5. Check the refreshed dashboard: Q4 revenue should be S$6,980,000 across the four desks.  —  Verify the artefact before you let it feed an email to your head of finance.
6. Read the drafted email in full and compare every figure against the dashboard.  —  Claude asks for explicit approval before sending — this is the moment to use it.
7. Approve the send, then confirm the message arrived in your own inbox.  —  Approve only once the figures match; if anything is wrong, ask for a correction first.

**Test it**

The dashboard shows a Q4 column with actual against target per desk and Q4 revenue of S$6,980,000. The email arrives in your own inbox with the correct totals and a closing note about the Advisory target discrepancy.

> **Note:** Full commands and screenshots are in labs/lab-05-*.md. Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.

---


### Lab 6 — Build a /daily-brief Skill

Learning outcome: turn a routine you have already done into a reusable Agent Skill, and update it.

Goal: Labs 4 and 5 showed what the connectors can do — but you had to describe the whole routine each time. Now you capture it once. The reliable way to build a skill is the Do / Verify / Save pattern: do the task with Claude once, refine until the output is right, then use the /skill-creator skill to save it. You have already done the doing — this lab turns it into a command, then updates it.

**What you'll build**

A daily-brief Agent Skill you can run by name each morning, updated once.   (Tools: Claude Cowork, Agent Skills, /skill-creator, Google Drive connector, Gmail connector.)

**The prompt**

Copy the block below into Claude exactly as it is.

```text
Step 1 — DO. Run my morning finance briefing for Meridian Capital
Partners, once, so we can get the format right together:

- What changed in the Meridian Finance folder on Google Drive since
  yesterday?
- Which desks are behind their quarterly target right now?
- What finance emails do I need to respond to today?

If a section has nothing in it, say so plainly — "No new files since
yesterday" — rather than padding it out. End with one line on what most
needs my attention, or "Nothing urgent — have a good day" if there is
nothing. All money in Singapore dollars. Draft only — never send email.

Step 2 — SAVE. Once I confirm the output is right, use the
/skill-creator skill to turn exactly this routine into a skill called
daily-brief that I can run every morning.
```

> **Note:** Do it once, check the output, then save it — that order is what makes the skill reliable.

**Step-by-step**

1. Make sure the Drive and Gmail connectors from Labs 4 and 5 are still enabled.  —  The skill drives those connectors, so it can only work if they are on.
2. DO — paste Step 1 of the lab prompt and let Claude run the routine once.  —  You are not writing instructions yet; you are doing the task together so Claude sees what good looks like.
3. VERIFY — read the briefing and ask for changes until the format is right.  —  Reorder a section, tighten the wording, fix a heading. Whatever you settle on here is what the skill will reproduce.
4. Check the fallback wording on any empty section.  —  The fallbacks are what stop the routine inventing filler on a quiet morning — get them right before you save.
5. Confirm it drafted and did not send anything.  —  A routine you will run unattended must not be able to send mail on its own.
6. SAVE — run Step 2 so /skill-creator turns the routine into a daily-brief skill.  —  The skill-creator skill writes the SKILL.md for you, from the run you just verified.
7. Read the SKILL.md it produces, especially the description line.  —  The description is how Claude decides whether to load the skill for a future task — make it specific.
8. Run the skill by name, then run it again.  —  The same structure both times is the payoff: one command instead of re-describing the routine every morning.
9. UPDATE — ask for one change, such as putting the emails section first.  —  A skill is not written once. You keep refining it as you learn what you actually want each morning.
10. Save the change under the same skill name and confirm the replace prompt.  —  Claude warns that a skill with this name already exists and that replacing it cannot be undone — read that prompt before you accept it.
11. Run the skill once more to confirm the change took effect.  —  Always re-run after an update; that is how you know the new version is the one being loaded.

**Test it**

Running the daily-brief skill by name produces a briefing with all three sections — Drive changes, desks behind target, emails needing a reply — using the plain fallback wording where a section is empty, ending with a single attention line, with all money in SGD and no email sent. After the update, the revised section order appears on the next run — and Claude warned you before replacing the existing skill.

> **Note:** Full commands and screenshots are in labs/lab-06-*.md. Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.

---


## Topic 03 — Claude Projects

Bringing it together · project knowledge · reusable workspace for the team

**Key concepts**

- ('A Claude Project', 'A dedicated place for ongoing work, where context builds over time instead of resetting each chat.')
- ('Backed by a folder', 'In Cowork the files and instructions live in a real folder on your computer — you can still open them yourself.')
- ('Three ways to start', 'Start from scratch, import a project you made in Chat, or point Claude at a folder you already work from.')
- ('Project instructions', 'Standing rules for this body of work — house style, SGD formatting, check before sending.')
- ('Everything in one place', 'The finance data, the brand rules, your daily-brief skill and the dashboard, together.')
- ('Share the folder', 'A colleague opens the same project and inherits the data, rules and tools you set up.')


### Lab 7 — Build the Meridian Claude Project

Learning outcome: assemble the data, instructions, skill and dashboard into one reusable Project.

Goal: Everything you have built so far lives in separate places — a dashboard in your sidebar, files in Drive, a skill, and rules you have been restating by hand. In this final lab you gather them into one Cowork Project: a dedicated folder on your computer where context builds over time, and which a colleague can open and be immediately productive in.

**What you'll build**

A Meridian Finance Reporting project holding the data, instructions, skill and dashboard.   (Tools: Claude Cowork, Projects, Agent Skills, Live Artefacts, Google Drive connector.)

**The prompt**

Copy the block below into Claude exactly as it is.

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

**Step-by-step**

1. In Cowork, choose New project, then Start from scratch.  —  The other two routes on that screen are Import a project (bring one over from Chat) and Use an existing folder (point Claude at a folder you already work from).
2. In the Start a new project dialog, type the Name: Meridian Finance Reporting.  —  The dialog has four fields — Name, Instructions, Add files and Choose project location.
3. Paste the lab prompt's rules into the Instructions box.  —  These are the standing rules — house style, SGD formatting and the approval habit — applied to every chat in the project.
4. Under Add files, drop in the Meridian finance data and the brand guidelines.  —  Adding them once means no chat in this project has to re-attach them.
5. Set Choose project location to where you want the folder to live, then click Create.  —  A Cowork project is backed by a real folder on your computer — you can open the files yourself at any time.
6. Add the daily-brief skill from Lab 6 to the project.  —  The routine now travels with the project, so anyone working in it can run it.
7. Open the project folder on your computer and confirm the files are really there.  —  This is what distinguishes a Cowork project — the instructions and files are a folder you own, not something locked inside the app.
8. Save the FY2025 dashboard into the project so it sits with the data it reports on.  —  The artefact, its data and its rules finally live in one place.
9. Start a fresh chat in the project and ask for a one-paragraph Q4 summary.  —  Test the payoff: no files attached, no rules restated, and the output already follows the house style.
10. Confirm the folder holds the data, instructions, skill and dashboard, ready to share.  —  Handing a colleague this folder hands them the whole working setup.

**Test it**

A Meridian Finance Reporting project exists, backed by a folder containing the finance data and brand guidelines, with project instructions set, the daily-brief skill available and the dashboard saved. A brand-new chat in the project produces a Q4 summary in SGD with the correct header and footer without you attaching a file or restating a single rule.

> **Note:** Full commands and screenshots are in labs/lab-07-*.md. Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.

---


## Wrap-Up

Across seven labs you took one finance scenario from a blank workspace to a branded, connected, reusable dashboard.

**What you built**

- A Live Artefact sales dashboard for Meridian Capital, saved and downloaded.
- A Google Drive connection that feeds the dashboard from the firm's finance data.
- An approved Gmail summary of the quarter, sent to a test recipient.
- A daily-brief Agent Skill that runs the whole morning routine on one command.
- A Meridian Finance Reporting Project holding the data, instructions, skill and dashboard.

**The habit to keep**

- Describe the outcome, let Claude build it, then check the figures yourself.
- Scope every connector to the one folder or mailbox the task needs.
- Approve every outgoing message against the source data before it is sent.
- Write a routine down once as a skill instead of retyping it every time.
- Keep the work in a Project so context builds instead of resetting each chat.

---


## Next Steps

- First pass: complete every lab yourself, following the steps in each lab file.
- Second pass: redo the labs from memory until the workflow is automatic.
- Apply the techniques to a real process or project in your own organisation.
- Review each lab's detailed steps in this guide and re-run the labs on your own.


## Glossary

- **Agent Skill** — A folder containing a SKILL.md of instructions that Claude loads on demand when the task matches its description.
- **Artefact** — A self-contained output Claude builds — a document, dashboard or tool — shown beside the chat rather than inside it.
- **Claude Cowork** — The desktop agent for non-developers that works on your files, folders and connected apps.
- **Connector** — An integration that lets Claude reach an outside service such as Google Drive, Gmail or Calendar.
- **Live Artefact** — An artefact that persists in your workspace, keeps its state, and refreshes its data when reopened.
- **MCP** — Model Context Protocol — the open standard connectors use to expose tools and data to Claude.
- **SKILL.md** — The Markdown file at the heart of an Agent Skill: name, description and instructions.
