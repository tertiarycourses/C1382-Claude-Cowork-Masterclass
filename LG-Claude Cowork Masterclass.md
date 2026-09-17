# Claude Cowork Masterclass — Learner Guide

**Course Code:** C1382  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v4.1 · 18 September 2026**

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
  - [Lab 6 — Generate the Meridian Board Deck](#lab-6--generate-the-meridian-board-deck)
  - [Lab 7 — Build a /daily-brief Skill](#lab-7--build-a-daily-brief-skill)
  - [Lab 8 — Brand the Board Deck](#lab-8--brand-the-board-deck)
- [Topic 03 — Claude Projects and Plugins](#topic-03--claude-projects-and-plugins)
  - [Lab 9 — Build the Meridian Claude Project](#lab-9--build-the-meridian-claude-project)
  - [Lab 10 — Add the Productivity Plugin](#lab-10--add-the-productivity-plugin)
- [Wrap-Up](#wrap-up)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

Claude Cowork is the desktop agent in the Claude family built for people who work with files and reports rather than code. This course teaches it through one continuous scenario: you are on the finance team at Meridian Capital Partners Pte Ltd, and over ten labs you process a year of invoices, build a live sales dashboard, connect it to the firm's data in Google Drive, deliver an approved summary by Gmail, have Claude generate the quarterly board deck with a built-in skill, wrap your morning routine and the firm's house style into reusable skills of your own, gather everything into one Claude Project your whole team can work from, and finish by installing a plugin — a toolkit somebody else packaged.

Meridian Capital Partners is a fictitious Singapore-based investment and advisory firm with four revenue desks — Advisory, Asset Management, Private Credit and Corporate Finance. All figures, clients, staff and documents in this course are synthetic and used for training only.


## Course Learning Outcomes

- LO1: Set up the Cowork desktop workspace and have Claude process a folder of documents into a structured summary.
- LO2: Build, save and download a Live Artefact, including an interactive sales dashboard from supplied data.
- LO3: Connect the Google Drive connector so Claude can read finance data held outside the chat.
- LO4: Refresh a Live Artefact from connected data and send an approved summary with the Gmail connector.
- LO5: Generate a board-ready deck with real charts from connected data, using a skill Claude loads on demand.
- LO6: Turn a verified routine into an Agent Skill with /skill-creator, update it, and explain a skill's three layers.
- LO7: Capture a documented house style as a reusable skill that brands any presentation on command.
- LO8: Assemble a Claude Project that holds the data, instructions, skills and dashboard as one reusable team workspace.
- LO9: Install a plugin and explain how a packaged bundle of skills differs from a skill you wrote yourself.


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

Goal: Now you have seen Cowork do a real piece of work, meet the other thing it makes: a Live Artefact. You build a small tool rather than ask a question, so you can see how an artefact differs from a chat answer — it persists, it is interactive, and you can save and download it. You also meet the sandbox: an artefact cannot call the internet, so you build one version with the rates baked in and a downloadable HTML version that fetches them live.

**What you'll build**

An FX converter as a saved artefact, plus a downloadable HTML version with live rates.   (Tools: Claude desktop app, Claude Cowork, Live Artefacts.)

**The prompt**

Copy the block below into Claude exactly as it is.

```text
I want a currency converter for Meridian Capital Partners, in three
steps. Artefacts cannot call the internet, so do NOT put any fetch,
API call or network request in the artefact — it will fail.

STEP 1 — You look up the rates.
Search the web for today's mid-market rates from SGD to USD, EUR and
GBP. Tell me the three rates and the date, in the chat.

STEP 2 — Build the artefact with those numbers HARD-CODED.
Write the three rates into the code as constants. No fetch anywhere.
   - Convert between SGD, USD, EUR and GBP.
   - One amount box, a from-currency and a to-currency selector,
     and a large result that updates as I type.
   - Under the result show the rate used, and the line
     "Rates as at <the date from Step 1> — fixed at build time".
   - Clean, professional finance styling, titled "Meridian Capital
     Partners".

STEP 3 — Now a SEPARATE downloadable HTML file.
Save a file called meridian-fx-live.html to my folder. Same design,
but this one DOES fetch rates from a free no-key API (such as
open.er-api.com or frankfurter.app) when it opens, with a Refresh
button and the fetch time shown. Tell me where you saved it.
Do not show this version as an artefact — it only works when I open
the file in my own browser.
```

> **Note:** The prompt tells Claude NOT to put a fetch in the artefact. If you leave that out, Claude writes one and the artefact shows "Live rate lookup failed" — the sandbox blocks it. Live data belongs in the downloadable HTML, which runs in your own browser.

**Step-by-step**

1. Start a new Cowork session — this lab needs no files.  —  Lab 1 gave Claude a folder to work in; here you are asking it to build something from nothing.
2. Paste the lab prompt into the composer and send it.  —  It asks for three things in order: look up the rates, build the artefact, then save a separate live HTML file.
3. Read the three rates Claude reports back in the chat.  —  Claude can search the web; the artefact cannot. This is why the lookup happens here, in the conversation, and not inside the tool.
4. Try the artefact: change the amount and switch the currencies.  —  It works instantly because the rates are constants in the code — no network call to fail.
5. Check the artefact's rate against a search for "1 USD to SGD".  —  It should match today, because Claude looked it up minutes ago. The "fixed at build time" line is the honest caveat.
6. Open the downloaded meridian-fx-live.html in your browser and click Refresh.  —  Same design, but running outside the sandbox, so THIS one really does fetch live rates. That contrast is the lesson.
7. Ask for one refinement in plain English, for example: Add a thousands separator to the result.  —  Refining by conversation is the normal way to work — you never edit the code yourself.
8. Save the artefact so it appears in your sidebar.  —  A saved artefact persists as a reusable tool; an unsaved one scrolls away with the chat.

**Test it**

The artefact converts S$10,000 to USD with no error, shows the rate used and a "Rates as at … — fixed at build time" line, and the rate matches a live search. Separately, meridian-fx-live.html opens in your browser, fetches its own rates and updates them when you click Refresh. The artefact is saved in your sidebar.

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

Tools first — Google Drive and Gmail — then skills: a built-in skill that builds the board deck, and two of your own written with /skill-creator

**Key concepts**

- ('Connectors', 'Toggle Gmail, Calendar and Drive on from the + menu so Claude can reach data outside the chat.')
- ('Google Drive', 'Claude reads Sheets, Docs, Slides and PDFs from Drive, and can upload files back to a folder.')
- ('Scope the folder', 'Point Claude at one Drive folder for the task — not your whole Drive.')
- ('Gmail', 'Claude drafts, sends, replies and labels — sending asks for explicit approval by default.')
- ('Agent Skills', 'A folder of instructions Claude loads on demand, so a task runs the same way every time.')
- ('Built-in skills', 'Some ship with Claude — pptx builds PowerPoint files. It loads when your request matches.')
- ('Where to see them', 'Your own skills appear in + → Skills. Built-in ones do not — look in the Context panel.')
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
4. Approve the permissions Google asks for — grant FULL READ access.  —  Approve only what you are willing to let Claude reach. But if you decline the read scopes here, Claude connects yet cannot open anything.
5. If Claude reports an "insufficient scope" error, reconnect the connector.  —  Settings → Connectors → Google Drive → Reconnect, and accept the read permissions. A connector can show "Connected" while still missing the drive.readonly scope it needs to search and read files.
6. Paste the lab prompt so Claude reads the Meridian Finance folder.  —  Naming the folder scopes the task; Claude does not need access to your whole Drive.
7. Compare Claude's file summary against what you actually uploaded.  —  Confirm it found every file and read the right periods before you rely on it.
8. Note any inconsistency Claude reports between the files.  —  The Q4 Advisory target deliberately disagrees between two files — a real check.

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


### Lab 6 — Generate the Meridian Board Deck

Learning outcome: have Claude build a board-ready deck with real charts using a skill it loads on demand.

Goal: The quarterly board pack is due. In Lab 5 you sent the head of finance a summary email — the board wants the same story as slides. Rather than building it by hand, you have Claude read the Meridian data from Drive and produce the PowerPoint itself.

This is your first look at a skill doing the work. You do not write anything or turn anything on: Claude has a built-in pptx skill for creating PowerPoint files, and it loads on demand because your request matches what the skill is for. You can watch it happen in the Context panel. It builds the charts too — real, editable PowerPoint charts, not screenshots. In Labs 7 and 8 you write your own skills; here you watch one work first.

**What you'll build**

A board-ready PowerPoint with charts and Q4 recommendations, built by Claude's built-in pptx skill.   (Tools: Claude Cowork, Google Drive connector, the built-in pptx skill.)

**The prompt**

Copy the block below into Claude exactly as it is.

```text
Using the Meridian Finance folder in Google Drive, build me a PowerPoint
called "Meridian Capital Partners — FY2025 Board Review".

Slides:
1. Title slide with the company name and "FY2025 Board Review".
2. FY2025 summary — total revenue, total deals, average deal size and
   the best-performing desk.
3. Revenue by desk — a bar chart of FY2025 revenue for the four desks,
   with the figures labelled.
4. Q4 desk performance — a grouped bar chart of each desk's Q4 actual
   against its target, plus a line on what the gaps mean.
5. Recommendation — how to close the Q4 Advisory shortfall.
6. Recommendation — where to invest next year, based on the strongest
   and weakest desks.

Use real PowerPoint charts, not pictures of charts, so the numbers stay
editable. All money in Singapore dollars with thousands separators.

Show me the outline before you build it. When the deck is ready, post the
.pptx in the chat so I can download it.
```

> **Note:** Ask for the outline first. It is far cheaper to fix the structure before the slides exist than after.

**Step-by-step**

1. Make sure the Google Drive connector from Lab 4 is still enabled.  —  Drive is where the finance data lives; the deck is built from what Claude reads there.
2. Paste the lab prompt.  —  Claude reads the figures from Drive and writes the PowerPoint itself — you are not exporting data between tools by hand.
3. Read the outline Claude proposes and correct it before it builds.  —  Structure is cheap to change now and expensive to change once six slides exist.
4. Open the Context panel in the sidebar and find `pptx` under Skills.  —  It is there because your request matched what the skill is for — you never named it. The same panel shows your working folder and the connectors that are on: everything currently in Claude's context, in one place.
5. Let Claude generate the .pptx and download it.  —  The file arrives as a download in the chat, the same way the HTML artefact did in Lab 2.
6. Open the PowerPoint and read it end to end.  —  A deck you did not write is still a deck you are accountable for.
7. Click a chart and confirm it is a real PowerPoint chart.  —  Selecting it should offer you the underlying data. A chart you can edit survives the first question from the board; a picture of a chart does not.
8. Check every figure against the Lab 3 dashboard and the Lab 5 email.  —  FY2025 revenue should read S$24,850,000 and Q4 S$6,980,000 — the same numbers, or something has gone wrong.
9. Confirm the Advisory recommendation names the target discrepancy rather than averaging it away.  —  The S$90,000 gap between the two files is the one thing the board must not be shown a tidy average of.

**Test it**

The PowerPoint downloads and opens with six slides. FY2025 revenue reads S$24,850,000 across 214 deals, Advisory is the best desk at S$8,420,000, and Q4 totals S$6,980,000 with each desk shown against its target. The revenue-by-desk and Q4-against-target charts are real PowerPoint charts with editable data, not images. One recommendation slide states the S$90,000 Q4 Advisory target discrepancy explicitly.

> **Note:** Full commands and screenshots are in labs/lab-06-*.md. Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.

---


### Lab 7 — Build a /daily-brief Skill

Learning outcome: turn a routine you have already done into a reusable Agent Skill, update it, and schedule it to run itself.

Goal: Labs 4 and 5 showed what the connectors can do, and Lab 6 showed a built-in skill doing the work for you. Now you write one yourself. The reliable way to build a skill is the Do / Verify / Save pattern: do the task with Claude once, refine until the output is right, then use `/skill-creator` to save it. You have already done the doing — this lab turns it into a command, then updates it. Finally you schedule it, so the briefing is waiting as a draft before you sit down rather than something you have to remember to ask for.

**What you'll build**

A daily-brief Agent Skill you can run by name each morning, updated once and scheduled to run itself at 9am.   (Tools: Claude Cowork, Agent Skills, /skill-creator, Google Drive connector, Gmail connector, Scheduled tasks.)

**The prompt**

This lab has three blocks, sent at different times. Blocks 1 and 2 are typed into the chat composer, with a verify step between them. Block 3 goes into the Instructions field of the Create scheduled task dialog rather than into the chat.

Block 1 — DO

```text
Run my morning finance briefing for Meridian Capital Partners, once,
so we can get the format right together:

- What changed in the Meridian Finance folder on Google Drive since
  yesterday?
- Which desks are behind their quarterly target right now?
- What finance emails do I need to respond to today?

If a section has nothing in it, say so plainly — "No new files since
yesterday" — rather than padding it out. End with one line on what most
needs my attention, or "Nothing urgent — have a good day" if there is
nothing. All money in Singapore dollars. Draft only — never send email.
```

Now stop and read the output. Ask for changes until the format is right — reorder a section, tighten a heading, fix the fallback wording. Whatever you settle on here is exactly what the skill will reproduce every morning. Do not continue until you are happy with it.

Block 2 — SAVE — type /skill-creator into the composer yourself, select it from the slash-command list, then add this description after it

```text
/skill-creator Save the morning finance briefing routine we just ran as
a skill called daily-brief. Keep the three sections in the order we
settled on, the plain fallback wording for empty sections, the single
closing attention line, all money in Singapore dollars, and draft-only —
never send email.
```

Block 3 — SCHEDULE — this block is pasted into the Instructions field of the Create scheduled task dialog, not typed into the chat

```text
Run my daily-brief skill for Meridian Capital Partners.

Leave the briefing as a draft email to me in Gmail, with the subject
"Meridian daily brief" and today's date. Do not send it.

If a section has nothing in it, keep the plain fallback wording rather
than padding it out.
```

Notice it names the skill rather than restating the routine — that is what saving the skill bought you. Notice too that it repeats *Do not send it* even though the skill is already draft-only. A scheduled task is the one place you state a safety rule twice: it runs unattended with Permissions set to *Automatically approve*, so both the instruction and the skill carry the constraint.

> **Note:** Do it once, check the output, then save it — that order is what makes the skill reliable.

**Step-by-step**

1. Make sure the Drive and Gmail connectors from Labs 4 and 5 are still enabled.  —  The skill drives those connectors, so it can only work if they are on.
2. DO — send block 1 on its own and let Claude run the routine once.  —  You are not writing instructions yet; you are doing the task together so Claude sees what good looks like.
3. VERIFY — read the briefing and ask for changes until the format is right.  —  Reorder a section, tighten the wording, fix a heading. Whatever you settle on here is what the skill will reproduce.
4. Check the fallback wording on any empty section.  —  The fallbacks are what stop the routine inventing filler on a quiet morning — get them right before you save.
5. Confirm it drafted and did not send anything.  —  A routine you will run unattended must not be able to send mail on its own.
6. SAVE — type `/skill-creator` in the composer, then send block 2.  —  You type the slash command yourself and pick it from the list; it then writes the SKILL.md for you, from the run you just verified.
7. Read the SKILL.md it produces, especially the description line.  —  The description is how Claude decides whether to load the skill for a future task — make it specific.
8. Run the skill by typing `/daily-brief`, then run it again.  —  The same structure both times is the payoff: one command instead of re-describing the routine every morning.
9. UPDATE — ask for one change, such as putting the emails section first.  —  A skill is not written once. You keep refining it as you learn what you actually want each morning.
10. Save the change under the same skill name and confirm the replace prompt.  —  Claude warns that a skill with this name already exists and that replacing it cannot be undone — read that prompt before you accept it.
11. Run `/daily-brief` once more to confirm the change took effect.  —  Always re-run after an update; that is how you know the new version is the one being loaded.
12. Open Scheduled tasks from the sidebar, choose New task, then Set up manually.  —  The other route, Create with Claude, fills the task in for you by asking questions; setting it up manually shows you every field it will set.
13. Name the task "Daily briefing".  —  The skill captures WHAT to do; the schedule captures WHEN. Two different kinds of reuse, and this is the second one.
14. Paste Block 3 into the Instructions field.  —  It names the skill you just built rather than re-describing the routine — that is what saving it bought you. It also repeats "Do not send it", because a scheduled task is the one place you state a safety rule twice.
15. Point "Work in a project or folder" at the folder you have been working in.  —  The task needs the same working folder and connectors the skill expects.
16. Set Frequency to run daily at 9:00am.  —  Before you sit down, so the briefing is waiting rather than something you go and fetch.
17. Read the Permissions setting and understand what "Automatically approve" means.  —  The task will use your connectors unattended, without pausing to ask. This is exactly why the skill drafts and never sends — an unattended task that could send mail is how an unreviewed email reaches a real client.
18. Decide whether to switch on "Require this computer".  —  On, it only runs while your computer is awake but can reach your local folders; off, it runs without them. Choose to match where the task's data actually lives.
19. Save the task, then run it once manually to confirm it works.  —  Never leave a scheduled task untested — the first time it runs should not be the morning you are relying on it.
20. Check Gmail for a draft titled "Meridian daily brief" and confirm nothing was sent.  —  A draft in your Drafts folder and an empty Sent folder is the proof the constraint held.

**Test it**

Running `/daily-brief` produces a briefing with all three sections — Drive changes, desks behind target, emails needing a reply — using the plain fallback wording where a section is empty, ending with a single attention line, with all money in SGD and no email sent. After the update, the revised section order appears on the next run — and Claude warned you before replacing the existing skill. A scheduled task named "Daily briefing" exists, set to run daily at 9:00am, and running it manually leaves a Gmail draft titled "Meridian daily brief" with today's date, while your Sent folder stays empty.

> **Note:** Full commands and screenshots are in labs/lab-07-*.md. Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.

---


### Lab 8 — Brand the Board Deck

Learning outcome: teach Claude a house style from an example deck and save it as a reusable skill.

Goal: The board deck from Lab 6 has the right numbers and the wrong clothes — it looks like a default template. Meridian has a branded template every deck is supposed to follow; the problem is that applying it by hand, every time, is what nobody does.

So you do not describe the house style to Claude — you hand it the template and let it work the style out for itself. That is how branding actually reaches people in a firm: somebody sends you the template, not a list of hex values. You apply it once, check the result, then save it as a skill so any future deck can be branded by name — the same way you saved `/daily-brief` in Lab 7.

**What you'll build**

A brand-deck Agent Skill that applies the Meridian house style to any presentation.   (Tools: Claude Cowork, Agent Skills, /skill-creator.)

**The prompt**

This lab is sent in two separate messages, not one. Attach both the template and the Lab 6 deck, send block 1, and only send block 2 once the restyled deck looks right.

Block 1 — DO

```text
I have attached two files.

The first, meridian-brand-template.pptx, is our house template. Study
it and work out the style it uses: the colours, the fonts for headings
and body text, how the title slide is treated, the rule under each
slide title, and what goes in the footer.

The second is the "Meridian Capital Partners — FY2025 Board Review"
deck I built in the last lab. Apply the template's style to it so the
two look like the work of the same firm.

Tell me what style rules you took from the template before you apply
them, so I can check you read it correctly.

This is a restyle only — do not change any figure or any wording.
Give me the restyled .pptx to download when you are done.
```

Now stop and look at the deck. Open the restyled deck beside the template and check the title slide and one content slide — they should read as the same firm's work. Ask for changes until it looks right. Whatever you settle on here is what the skill will reproduce.

Block 2 — SAVE — type /skill-creator into the composer yourself, select it from the slash-command list, then add this description after it

```text
/skill-creator Save what we just did as a skill called brand-deck that
applies the Meridian house style to any presentation. Write the actual
colours, fonts, title treatment and footer you took from the template
into the skill, so it works on a deck later without me attaching the
template again. Never change figures or wording — restyle only.
```

The skill records the style values Claude read off the template. That is the point of saving it: from now on the house style travels with the skill, and nobody has to find the template first.

> **Note:** Restyle only. A branding skill that is allowed to touch the numbers is a branding skill that will eventually change one.

**Step-by-step**

1. Attach the template from `mock-data/` and the PowerPoint you downloaded in Lab 6.  —  Claude learns the style from the template and applies it to the deck, so it needs both files in front of it.
2. DO — send block 1 on its own and let Claude study the template.  —  You are not describing the house style; you are handing over an example and letting Claude read it — which is how a template reaches anyone in a real firm.
3. Read the style rules Claude says it took from the template before it applies them.  —  If it misread the template, you find out now rather than in the finished deck.
4. Open the restyled deck beside the template and compare the title slides.  —  Same background, same wordmark treatment, same rule. They should read as the work of one firm.
5. Check a content slide against the template's content slide.  —  Heading colour and typeface, the rule under the title, the body font, and the footer lockup with the slide number.
6. Confirm no figure and no wording changed.  —  Compare against the Lab 6 check: S$24,850,000, 214 deals, Q4 S$6,980,000, and the S$90,000 Advisory discrepancy still stated.
7. VERIFY — ask for changes until the look is right.  —  Whatever you settle on now is what every future deck will inherit.
8. SAVE — type `/skill-creator` in the composer, then send block 2.  —  You type the slash command yourself and pick it from the list; it writes the SKILL.md from the restyle you just verified.
9. Read the SKILL.md it produces and check it recorded the actual style values.  —  A skill that says "match the template" needs the template. A skill that names the colours and fonts works on its own — that is what saving it is for.
10. Attach another deck, type `/brand-deck`, and run it — without attaching the template.  —  The same house style landing on a deck the skill has never seen, with no template in the chat, is the whole point.

**Test it**

The restyled deck downloads and matches the template's look — the same background colours, heading and body typefaces, title treatment, rule under each title and footer lockup with the internal-use line and slide number. Every FY2025 and Q4 figure is unchanged from Lab 6, including the S$90,000 Advisory discrepancy. Running `/brand-deck` on a different presentation, with no template attached, applies the same house style.

> **Note:** Full commands and screenshots are in labs/lab-08-*.md. Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.

---


## Topic 03 — Claude Projects and Plugins

Bringing it together · project knowledge · a reusable workspace for the team · installing a packaged toolkit

**Key concepts**

- ('A Claude Project', 'A dedicated place for ongoing work, where context builds over time instead of resetting each chat.')
- ('Backed by a folder', 'In Cowork the files and instructions live in a real folder on your computer — you can still open them yourself.')
- ('Ways to start', 'Create a new one from scratch, recreate one you run in Chat, or point it at a folder you already work from.')
- ('Project instructions', 'Standing rules for this body of work — house style, SGD formatting, check before sending.')
- ('Context vs Folder', 'Context is what Claude reads and never edits. Folder is where it actually works — reading data and writing output.')
- ('Everything in one place', 'The finance data, the brand rules, your daily-brief and brand-deck skills and the dashboard, together.')
- ('Share the folder', 'A colleague opens the same project and inherits the data, rules and tools you set up.')
- ('Plugins', 'A bundle somebody else packaged — several skills plus the tools they need, installed in one click from Discover.')
- ('Namespaced commands', "A plugin's commands carry its name: /productivity:start. That prefix is how you tell a bundle's command from one you wrote.")


### Lab 9 — Build the Meridian Claude Project

Learning outcome: assemble the data, instructions, skills and dashboard into one reusable Project.

Goal: Everything you have built so far lives in separate places — a dashboard in your sidebar, files in Drive, two skills, a scheduled task, and rules you have been restating by hand. In this final lab you gather them into one Cowork Project: a dedicated folder on your computer where context builds over time, and which a colleague can open and be immediately productive in.

The project page has four panels — Instructions, Context, Folder and Scheduled — and you fill each in turn. The one worth pausing on is the difference between Context and Folder: Context holds documents Claude reads and never edits, while Folder is where it actually works.

**What you'll build**

A Meridian Finance Reporting project holding the data, instructions, skills and dashboard.   (Tools: Claude Cowork, Projects, Agent Skills, Live Artefacts, Google Drive connector.)

**The prompt**

This lab has two blocks. Block 1 is pasted into the Create a project dialog as the project is created; block 2 sets the project's standing instructions once it exists.

Block 1 — CREATE — paste this into the "What are you trying to achieve?" box of the Create a project dialog

```text
Quarterly finance reporting for Meridian Capital Partners Pte Ltd — a
Singapore investment firm with four desks: Advisory, Asset Management,
Private Credit and Corporate Finance. I produce revenue dashboards,
board decks and a daily briefing from the firm's finance data, all in
Singapore dollars and in the Meridian house style.
```

This is the standing context every chat in the project inherits, so you stop re-explaining who Meridian is.

Block 2 — INSTRUCTIONS — send this in the project once it exists, to set its standing instructions

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

1. In Cowork, start a new project to open the Create a project dialog.  —  The dialog asks two questions and offers a folder — it is deliberately short, because the detail is set once the project exists.
2. Under "What are you working on?", enter: Meridian Finance Reporting.  —  This is the project's name — it is how you will find it in the sidebar later.
3. Under "What are you trying to achieve?", paste Block 1.  —  This is the standing context every chat in the project inherits, so you stop re-explaining who Meridian is.
4. Click Create project.  —  The project now exists but is empty. Everything else is added from the project page, which has four panels down the right: Instructions, Context, Folder and Scheduled. You fill them in that order.
5. INSTRUCTIONS — open the panel and set the standing rules with Block 2.  —  These are the house style, the SGD formatting and the approval habit, applied to every chat in the project. You stop restating them.
6. CONTEXT — add the brand guidelines, the reporting calendar and the desk profiles.  —  Context holds documents Claude READS. It never edits them — they are reference material, which is why the brand rules and the calendar belong here rather than in the working folder.
7. FOLDER — point the panel at the working/ folder from this lab's mock data.  —  Folder is where Claude WORKS: it reads the revenue CSV there and writes its output into working/reports/. That read-versus-write split is the difference between the two panels, and it is the part people get wrong.
8. SCHEDULED — add the 9am daily-brief task you built in Lab 7 to the project.  —  Same feature as Lab 7, now scoped to the project: the task belongs to this body of work rather than floating loose in your account.
9. Add the daily-brief skill from Lab 7 and the brand-deck skill from Lab 8 to the project.  —  Both routines now travel with the project, so anyone working in it can run them. Type / in the composer to see them listed.
10. Open the project folder on your computer and confirm the files are really there.  —  This is what distinguishes a Cowork project — the instructions and files are a folder you own, not something locked inside the app.
11. Save the FY2025 dashboard into the project so it sits with the data it reports on.  —  The artefact, its data and its rules finally live in one place.
12. Start a fresh chat in the project and ask for a one-paragraph Q4 summary.  —  Test the payoff: no files attached, no rules restated, and the output already follows the house style.
13. Confirm all four panels are populated and the folder is ready to share.  —  Handing a colleague this folder hands them the whole working setup.

**Test it**

A Meridian Finance Reporting project exists with all four panels populated: Instructions carries the house rules, Context holds the brand guidelines, reporting calendar and desk profiles, Folder points at the working folder with the FY2025 revenue data, and Scheduled carries the 9am daily-brief task. Both the daily-brief and brand-deck skills are available and the dashboard is saved. A brand-new chat in the project produces a Q4 summary in SGD with the correct header and footer without you attaching a file or restating a single rule.

> **Note:** Full commands and screenshots are in labs/lab-09-*.md. Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.

---


### Lab 10 — Add the Productivity Plugin

Learning outcome: install a plugin and tell a packaged bundle apart from a skill you wrote yourself.

Goal: Lab 9 packaged your own setup so a colleague could open it and be productive. This lab runs the same idea in the opposite direction: you install a toolkit somebody else packaged.

That is the difference between a skill and a plugin. A skill is one routine you wrote — `/daily-brief` in Lab 7, `/brand-deck` in Lab 8. A plugin is the whole setup: several skills plus the tools they need, installed together in one click. You use Anthropic's Productivity plugin to track the follow-ups this course has actually generated, inside the Meridian project you just built.

**What you'll build**

The Productivity plugin installed, with a TASKS.md tracking your Meridian follow-ups.   (Tools: Claude Cowork, Plugins, the Productivity plugin.)

**The prompt**

Copy the block below into Claude exactly as it is.

```text
/productivity:start
```

> **Note:** This lab has no long prompt to paste — it is driven by the plugin's own commands. Note the `productivity:` prefix: that is how you tell a plugin's command from a skill you wrote.

**Step-by-step**

1. Open the Plugins panel and switch to the Discover tab.  —  The search box covers "skills and plugins" — both live in the same place, which is the first hint that a plugin is a container for skills.
2. Find the Productivity plugin from Anthropic and click Add.  —  It is described as "Tasks, planning and follow-ups — the everyday toolkit." The card shows the publisher and the install count.
3. Check Your plugins to confirm it installed.  —  The two tabs separate what you have from what is available — the same split as a package manager.
4. Type `/` in the composer and find the new `/productivity:` commands.  —  Note the prefix. These came from a bundle, unlike `/daily-brief` which you wrote yourself. That prefix is how you tell at a glance where a command came from.
5. Open the Meridian project from Lab 9 and run `/productivity:start` there.  —  The plugin works on the project you already built, so the tasks it tracks are real work rather than invented ones.
6. Answer whatever it asks and let it create the task list.  —  It sets up its task and memory systems for this project the first time you run it.
7. Open `TASKS.md` in the project folder and read the sections.  —  Active, Waiting On, Someday and Done. Like the project itself, it is a real file you own — not state hidden inside the app.
8. Add the follow-ups this course actually produced.  —  Chase the S$90,000 Q4 Advisory target discrepancy with Finance; review the FY2025 board deck before it goes to the board; confirm tomorrow's daily brief arrived as a draft. Genuine loose ends from Labs 4-8, which is why this lab can close the course honestly.
9. Run `/productivity:update` and see it triage.  —  It syncs from any connected source and flags what has gone stale — the maintenance half of a task system, which is the half people skip.
10. Note what the plugin could also connect to.  —  Asana, Linear, Jira, Monday, ClickUp, Notion, Slack and Microsoft 365. A plugin is how a whole team adopts the same toolkit at once, rather than each person writing their own version of it.

**Test it**

The Productivity plugin appears under Your plugins, and typing `/` lists its `/productivity:` commands alongside the `/daily-brief` and `/brand-deck` skills you wrote. A `TASKS.md` file exists in the Meridian project folder with Active, Waiting On, Someday and Done sections, and it holds at least the three Meridian follow-ups: the Q4 Advisory target discrepancy, the board deck review, and the daily-brief draft check.

> **Note:** Full commands and screenshots are in labs/lab-10-*.md. Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.

---


## Wrap-Up

Across ten labs you took one finance scenario from a blank workspace to a branded, connected, reusable set of finance tools.

**What you built**

- A Live Artefact sales dashboard for Meridian Capital, saved and downloaded.
- A Google Drive connection that feeds the dashboard from the firm's finance data.
- An approved Gmail summary of the quarter, sent to a test recipient.
- A board-ready PowerPoint with real charts, generated by Claude's built-in pptx skill.
- A daily-brief Agent Skill that runs the whole morning routine on one command.
- A brand-deck Agent Skill that applies the Meridian house style to any presentation.
- A Meridian Finance Reporting Project holding the data, instructions, skills and dashboard.
- The Productivity plugin installed, tracking the follow-ups this course produced.

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
