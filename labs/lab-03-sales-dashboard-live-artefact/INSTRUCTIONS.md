# Lab 03 — The Meridian Sales Dashboard

**Topic 01 · Claude Cowork Fundamentals**

> Meridian Capital Partners Pte Ltd — all data in this lab is synthetic and for training only.

## Goal

Meridian's head of finance wants to see how the four revenue desks performed this year without opening a spreadsheet. You take the supplied sales data and build it into a Live Artefact dashboard — KPI tiles, a trend chart and a desk breakdown — then save it. This dashboard is the artefact every later lab builds on.

## You'll build

A saved Live Artefact dashboard showing Meridian's FY2025 revenue by desk.

**Tools:** Claude Cowork, Live Artefacts, local files

## Mock data

The files for this lab are in `mock-data/`:

- `meridian-sales-fy2025.csv`

Leave these files unchanged — let Claude write its output elsewhere.

## The prompt

Copy this into Claude (it is also in [PROMPT.md](PROMPT.md)):

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

## Steps

1. **Open the lab folder and look at meridian-sales-fy2025.csv so you know what the data holds.**
   Always know your source before you ask Claude to summarise it — that is how you spot a wrong figure later.
2. **Start a Cowork session and attach the CSV, or point Claude at the lab folder.**
   Scope Claude to the one folder for this task rather than your whole drive.
3. **Paste the lab prompt and send it.**
   Claude reads the file, works out the totals and builds the dashboard in the preview pane.
4. **Check the KPI tiles against the CSV: total revenue should be S$24,850,000 across 214 deals.**
   This is the verification habit — read the artefact's numbers back against the source.
5. **Use the desk filter to view Advisory on its own, then return to all desks.**
   Interactivity is the point of a Live Artefact: the reader explores instead of asking you for another cut.
6. **Refine the layout in plain English, for example: Move the KPI tiles above the chart.**
   Keep refining by conversation until the dashboard reads the way you want it to.
7. **Save the dashboard to your sidebar with a clear name, then download a copy.**
   You will refresh this same artefact from connected data in Lab 5.

## Check your work

The dashboard shows total revenue S$24,850,000 and 214 deals, Advisory is the best desk at S$8,420,000, the desk filter changes the chart, and the artefact reopens from your sidebar after you close it.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
