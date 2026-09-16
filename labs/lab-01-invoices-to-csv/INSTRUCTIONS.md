# Lab 01 — Process a Folder of Invoices

**Topic 01 · Claude Cowork Fundamentals**

> Meridian Capital Partners Pte Ltd — all data in this lab is synthetic and for training only.

## Goal

Meridian's accountant needs the 2025 supplier invoices summarised and filed. You point Cowork at a folder of 126 PDFs — a full year of invoices, a few expense receipts, and the untidy filenames a real downloads folder collects — and have it read every document, build one CSV, and sort the files into month folders. This is work no dashboard can do: reading documents and acting on your file system. It is also far more than you would ever do by hand, which is the point.

## You'll build

An invoices_2025.csv summary plus the PDFs filed into YEAR-MONTH folders.

**Tools:** Claude Cowork, local files, PDF reading

## Mock data

The files for this lab are in `mock-data/`:

- `2025 Invoices`

Leave these files unchanged — let Claude write its output elsewhere.

## The prompt

Copy this into Claude (it is also in [PROMPT.md](PROMPT.md)):

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

## Steps

1. **Open the Claude desktop app, sign in, and choose Cowork in the sidebar.**
   Cowork is a desktop feature on a paid plan — the browser version cannot reach your files.
2. **Copy the lab's "2025 Invoices" folder somewhere you can work on it.**
   Always run a file-moving task against a copy the first time, so a mistake costs nothing.
3. **Open the folder yourself and skim it before you start — 126 files.**
   Two have machine-generated names and one looks like a duplicate. You cannot check 126 documents by hand, but you can check that the summary adds up.
4. **Start a Cowork session pointed at that folder, then paste the lab prompt.**
   Cowork needs access to the folder itself, not an attachment, because it must move files as well as read them.
5. **Let Claude work through the PDFs — this one takes a few minutes.**
   It is reading each document, not guessing from the filename, which is why the oddly-named files still land correctly.
6. **Open invoices_2025.csv and check the row count against the folder.**
   Expect 121 invoice rows — 117 in SGD and 4 in USD — with the receipts and the duplicate flagged rather than silently mixed in.
7. **Total the SGD column and compare it against S$777,954.81.**
   Spot-check a few rows against the PDFs too: a total that reconciles tells you the extraction held across all 126 files.
8. **Check the currency column — four invoices are in US dollars.**
   Never sum a mixed-currency column. This is exactly the kind of thing a human check is for.
9. **Confirm the PDFs now sit in 2025-01 … 2025-12 folders and nothing was deleted.**
   The file dates come from inside each document, so a file named Jan can still be filed by its real invoice date.
10. **Read Claude's list of flagged items and decide what to do about each.**
   Claude surfaces the exceptions; you make the call — that is the working relationship this course is teaching.

## Check your work

invoices_2025.csv lists every invoice with all seven fields plus the filename. The 117 SGD invoices total S$777,954.81; the four USD invoices are marked USD rather than added to that total. The duplicated invoice and the four expense receipts are flagged rather than counted as ordinary invoices. The PDFs now sit in 2025-01 … 2025-12 folders and all 126 files are still present.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
