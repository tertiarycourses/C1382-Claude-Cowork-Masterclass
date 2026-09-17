# Lab 06 — Generate the Meridian Board Deck

**Topic 02 · Tools and Skills**

> Meridian Capital Partners Pte Ltd — all data in this lab is synthetic and for training only.

## Goal

The quarterly board pack is due. In Lab 5 you sent the head of finance a summary email — the board wants the same story as slides. Rather than building it by hand, you have Claude read the Meridian data from Drive and produce the PowerPoint itself.

This is your first look at a skill doing the work. You do not write anything or turn anything on: Claude has a built-in pptx skill for creating PowerPoint files, and it loads on demand because your request matches what the skill is for. You can watch it happen in the Context panel. It builds the charts too — real, editable PowerPoint charts, not screenshots. In Labs 7 and 8 you write your own skills; here you watch one work first.

## You'll build

A board-ready PowerPoint with charts and Q4 recommendations, built by Claude's built-in pptx skill.

**Tools:** Claude Cowork, Google Drive connector, the built-in pptx skill

## The prompt

Copy this into Claude (it is also in [PROMPT.md](PROMPT.md)):

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

## Steps

1. **Make sure the Google Drive connector from Lab 4 is still enabled.**
   Drive is where the finance data lives; the deck is built from what Claude reads there.
2. **Paste the lab prompt.**
   Claude reads the figures from Drive and writes the PowerPoint itself — you are not exporting data between tools by hand.
3. **Read the outline Claude proposes and correct it before it builds.**
   Structure is cheap to change now and expensive to change once six slides exist.
4. **Open the Context panel in the sidebar and find `pptx` under Skills.**
   It is there because your request matched what the skill is for — you never named it. The same panel shows your working folder and the connectors that are on: everything currently in Claude's context, in one place.
5. **Let Claude generate the .pptx and download it.**
   The file arrives as a download in the chat, the same way the HTML artefact did in Lab 2.
6. **Open the PowerPoint and read it end to end.**
   A deck you did not write is still a deck you are accountable for.
7. **Click a chart and confirm it is a real PowerPoint chart.**
   Selecting it should offer you the underlying data. A chart you can edit survives the first question from the board; a picture of a chart does not.
8. **Check every figure against the Lab 3 dashboard and the Lab 5 email.**
   FY2025 revenue should read S$24,850,000 and Q4 S$6,980,000 — the same numbers, or something has gone wrong.
9. **Confirm the Advisory recommendation names the target discrepancy rather than averaging it away.**
   The S$90,000 gap between the two files is the one thing the board must not be shown a tidy average of.

## Check your work

The PowerPoint downloads and opens with six slides. FY2025 revenue reads S$24,850,000 across 214 deals, Advisory is the best desk at S$8,420,000, and Q4 totals S$6,980,000 with each desk shown against its target. The revenue-by-desk and Q4-against-target charts are real PowerPoint charts with editable data, not images. One recommendation slide states the S$90,000 Q4 Advisory target discrepancy explicitly.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
