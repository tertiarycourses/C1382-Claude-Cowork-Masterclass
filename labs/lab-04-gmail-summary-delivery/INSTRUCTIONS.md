# Lab 04 — Refresh the Dashboard and Send the Summary

**Topic 02 · Tools and Skills**

> Meridian Capital Partners Pte Ltd — all data in this lab is synthetic and for training only.

## Goal

Quarter end has arrived. You refresh the dashboard you built in Lab 2 using the data Claude now reads from Drive, then have it draft a quarterly summary email to the head of finance. You read the draft against the figures and approve it before a single message leaves your outbox.

## You'll build

An updated dashboard plus an approved quarterly summary email sent to yourself.

**Tools:** Claude Cowork, Live Artefacts, Google Drive connector, Gmail connector

## The prompt

Copy this into Claude (it is also in [PROMPT.md](PROMPT.md)):

```text
Two tasks, in order.

1. Open my saved "Meridian Capital Partners — FY2026 Revenue"
   dashboard and update it from the Meridian Finance folder in Google
   Drive. Add a Q4 column to the desk breakdown and show each desk's
   actual against its target.

2. Then draft an email to <YOUR OWN ADDRESS> with the subject
   "Meridian FY2026 — Q4 revenue summary". In the body:
   - Total FY2026 revenue and the Q4 figure.
   - Each desk's Q4 actual against target, best and worst first.
   - Two sentences explaining the largest variance.
   - A closing line noting the Q4 Advisory target discrepancy.

Show me the draft. Do not send it until I approve it.
```

> **Note:** Replace <YOUR OWN ADDRESS> with your own email — never a real client's.

## Steps

1. **Reopen the dashboard you saved in Lab 2 from your sidebar.**
   You are extending the artefact you already built, not starting a new one.
2. **Enable the Gmail connector from the plus menu, alongside Google Drive.**
   Turn on only the connectors this task needs.
3. **Paste the lab prompt, replacing the placeholder with your own email address.**
   Class exercises always go to a test recipient — yourself.
4. **Watch Claude refresh the dashboard from Drive and add the Q4 target comparison.**
   The data comes from the connector now; you are not attaching files by hand.
5. **Check the refreshed dashboard: Q4 revenue should be S$6,980,000 across the four desks.**
   Verify the artefact before you let it feed an email to your head of finance.
6. **Read the drafted email in full and compare every figure against the dashboard.**
   Claude asks for explicit approval before sending — this is the moment to use it.
7. **Approve the send, then confirm the message arrived in your own inbox.**
   Approve only once the figures match; if anything is wrong, ask for a correction first.

## Check your work

The dashboard shows a Q4 column with actual against target per desk and Q4 revenue of S$6,980,000. The email arrives in your own inbox with the correct totals and a closing note about the Advisory target discrepancy.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
