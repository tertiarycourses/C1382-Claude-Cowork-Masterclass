# Lab 03 — Connect Google Drive

**Topic 02 · Tools and Skills**

> Meridian Capital Partners Pte Ltd — all data in this lab is synthetic and for training only.

## Goal

Meridian's finance data does not live on your laptop — it sits in a shared Google Drive folder. You upload the firm's wider finance files to Drive, enable the Google Drive connector, and confirm Claude can read them without you attaching anything by hand.

## You'll build

A working Google Drive connection scoped to the Meridian finance folder.

**Tools:** Claude Cowork, Google Drive connector

## Mock data

The files for this lab are in `mock-data/`:

- `meridian-client-list.csv`
- `meridian-desk-targets-fy2026.csv`
- `meridian-quarterly-workbook-fy2026.csv`

Leave these files unchanged — let Claude write its output elsewhere.

## The prompt

Copy this into Claude (it is also in [PROMPT.md](PROMPT.md)):

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

## Steps

1. **Upload the lab's mock-data files to a new Google Drive folder named Meridian Finance.**
   The lab supplies the quarterly workbook, the desk targets and the client list as mock data.
2. **In Claude, click the plus sign in the composer and hover over Connectors.**
   This is where you turn individual connectors on and off for your account.
3. **Toggle Google Drive on and sign in to your Google account.**
   On a Team or Enterprise plan an owner must enable connectors for the organisation first.
4. **Approve the permissions Google asks for.**
   Approve only what you are willing to let Claude reach — you can revoke access later.
5. **Paste the lab prompt so Claude reads the Meridian Finance folder.**
   Naming the folder scopes the task; Claude does not need access to your whole Drive.
6. **Compare Claude's file summary against what you actually uploaded.**
   Confirm it found every file and read the right periods before you rely on it.
7. **Note any inconsistency Claude reports between the files.**
   The Q4 Advisory target deliberately disagrees between two files — a real check.

## Check your work

Claude lists all three Meridian Finance files with their periods, reports FY2026 revenue of S$24,850,000, and flags that the Q4 Advisory target disagrees between the two files — S$2,320,000 in the targets file against S$2,410,000 in the workbook. Nothing in Drive has been changed.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
