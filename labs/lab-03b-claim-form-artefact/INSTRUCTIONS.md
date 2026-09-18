# Lab 03b — Fill a Claim Form from an Artefact

**Topic 01 · Claude Cowork Fundamentals**

> Meridian Capital Partners Pte Ltd — all data in this lab is synthetic and for training only. Fill the form with invented details only; never a real person's NRIC, medical history or claim.

## Goal

Lab 3 used an artefact to *show* you data. This one uses an artefact to *collect* it. One of Meridian's staff has to submit a personal-accident claim, and the insurer's form is a 4-page PDF with 107 fields, most of them tiny boxed cells that are miserable to type into. You build a clean web form as a Live Artefact, fill it in once, click Submit — and Claude writes your answers into the real PDF.

The lesson underneath: an artefact runs in a sandbox and cannot write a file on your disk. So the artefact collects and validates, and Claude does the writing. That is the same split you met in Lab 2, where live rates had to live outside the artefact.

## You'll build

A claim-form artefact that collects the answers, plus a genuinely filled `claimants-statement-FILLED.pdf`.

**Tools:** Claude Cowork, Live Artefacts, local files

## Mock data

The files for this lab are in `mock-data/`:

- `claimants-statement-pa.pdf`

Leave these files unchanged — let Claude write its output to `outputs/`.

## The prompt

The prompt is in [PROMPT.md](PROMPT.md). It comes in two parts: one to build the artefact, and a follow-up that hands the collected answers back to Claude to write into the PDF.

> **Note:** Attach the PDF from your lab's mock-data folder before sending the prompt.

## Steps

1. **Open claimants-statement-pa.pdf and page through all four sections.**
   Note how much of it is boxed cells — one character per box. Knowing the shape of the source is what lets you judge the result.
2. **Start a Cowork session, attach the PDF, and send Part 1 of the prompt.**
   Claude lists the 107 fields and maps each visible label to its internal name. Read that table.
3. **Look at the field names Claude reports — several are wrong.**
   There are fields called `undefined`, and the one named `Gender M  F` is really the Occupation row. This is normal in forms built by hand, and it is why you never trust a field name without checking where it sits on the page.
4. **Send Part 2 and let Claude build the artefact.**
   You get one tidy scrolling form with date pickers, YES/NO radios and character counters, instead of 107 boxes.
5. **Fill it in with invented details, then click Submit.**
   The artefact validates the required fields and hands you a JSON block keyed by the PDF's internal field names. Nothing has touched the PDF yet.
6. **Copy the JSON, paste it back into the chat with the follow-up prompt.**
   This is the handover. The artefact collected; now Claude writes.
7. **Check the filled PDF that Claude saves to outputs/, page by page.**
   Open it and read each value against the printed label beside it. A value in the wrong row is the failure mode here — so this is the step that matters.
8. **Fix anything misplaced by telling Claude which label the value belongs next to.**
   For example: *The occupation went into the gender box — put it on the Occupation row.* Then have it render and check again.

## Check your work

The artefact shows the form grouped under sections 1, 2, 4, 5, 6, 7, 8 and 9, refuses to submit with a required field empty, and produces JSON on Submit rather than trying to build the PDF itself. `outputs/claimants-statement-FILLED.pdf` opens with your answers visible in the correct boxes — name on the Name row, NRIC on the NRIC row, occupation on the Occupation row, the accident date split across the Day / Month / Year cells — and the original in `mock-data/` is unchanged.

## Why the artefact can't just write the PDF

Worth being clear about, because it is the one thing learners try:

- An artefact is sandboxed. It cannot reach your filesystem and cannot reach the network, so it can neither open the source PDF nor save a new one.
- Claude in the Cowork session *can* read and write files in your folder. That is where the PDF work belongs.
- Two other traps sit in this particular form. Filled values are stored but invisible in some viewers unless `/NeedAppearances` is set; and the boxed comb fields take one character per cell, so a date must be written `14031981`, not `14/03/1981`.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise — a claim form is exactly the kind of document that invites it. Invent the claimant.
