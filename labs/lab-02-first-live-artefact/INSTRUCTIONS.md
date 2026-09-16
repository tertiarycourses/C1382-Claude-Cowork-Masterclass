# Lab 02 — Your First Live Artefact

**Topic 01 · Claude Cowork Fundamentals**

> Meridian Capital Partners Pte Ltd — all data in this lab is synthetic and for training only.

## Goal

Now you have seen Cowork do a real piece of work, meet the other thing it makes: a Live Artefact. You build a small tool rather than ask a question, so you can see how an artefact differs from a chat answer — it persists, it is interactive, and you can save and download it.

## You'll build

A saved, downloaded Live Artefact — a working Meridian FX converter.

**Tools:** Claude desktop app, Claude Cowork, Live Artefacts

## The prompt

Copy this into Claude (it is also in [PROMPT.md](PROMPT.md)):

```text
Build me a Live Artefact: a currency converter for Meridian Capital Partners.

Requirements:
- Convert between SGD, USD, EUR and GBP.
- Use these fixed demo rates from SGD: USD 0.74, EUR 0.68, GBP 0.58.
- One amount box, a from-currency and a to-currency selector, and a large result.
- Show the rate used underneath the result.
- Clean, professional finance styling. Label it "Meridian Capital Partners".

Make it interactive so I can change the amount and see the result update.
```

> **Note:** Rates are fixed demo values so the lab gives the same answer for everyone.

## Steps

1. **Start a new Cowork session — this lab needs no files.**
   Lab 1 gave Claude a folder to work in; here you are asking it to build something from nothing.
2. **Paste the lab prompt into the composer and send it.**
   Claude writes the code and renders the converter in the preview pane beside the chat.
3. **Try the converter: change the amount and switch the currencies.**
   This is what makes it an artefact rather than an answer — you can interact with it.
4. **Ask for one refinement in plain English, for example: Add a thousands separator to the result.**
   Refining by conversation is the normal way to work — you never edit the code yourself.
5. **Save the artefact so it appears in your sidebar.**
   A saved artefact persists as a reusable tool; an unsaved one scrolls away with the chat.
6. **Download a copy of the artefact to your lab folder.**
   Downloading gives you a file you can keep, attach or hand to someone without Claude.

## Check your work

Converting S$10,000 to USD shows US$7,400. The artefact appears in your sidebar after saving, still works when you reopen it, and a downloaded copy is in your lab folder.

## Further viewing

- [CLAUDE COWORK FULL COURSE 3 HOURS For Beginners (2026)](https://www.youtube.com/watch?v=0UFSZ_5OSIk)

Optional background, not needed to complete the lab.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
