# Lab 02 — Your First Live Artefact

**Topic 01 · Claude Cowork Fundamentals**

> Meridian Capital Partners Pte Ltd — all data in this lab is synthetic and for training only.

## Goal

Now you have seen Cowork do a real piece of work, meet the other thing it makes: a Live Artefact. You build a small tool rather than ask a question, so you can see how an artefact differs from a chat answer — it persists, it is interactive, and you can save and download it. You also meet the sandbox: an artefact cannot call the internet, so you build one version with the rates baked in and a downloadable HTML version that fetches them live.

## You'll build

An FX converter as a saved artefact, plus a downloadable HTML version with live rates.

**Tools:** Claude desktop app, Claude Cowork, Live Artefacts

## The prompt

Copy this into Claude (it is also in [PROMPT.md](PROMPT.md)):

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

## Steps

1. **Start a new Cowork session — this lab needs no files.**
   Lab 1 gave Claude a folder to work in; here you are asking it to build something from nothing.
2. **Paste the lab prompt into the composer and send it.**
   It asks for three things in order: look up the rates, build the artefact, then save a separate live HTML file.
3. **Read the three rates Claude reports back in the chat.**
   Claude can search the web; the artefact cannot. This is why the lookup happens here, in the conversation, and not inside the tool.
4. **Try the artefact: change the amount and switch the currencies.**
   It works instantly because the rates are constants in the code — no network call to fail.
5. **Check the artefact's rate against a search for "1 USD to SGD".**
   It should match today, because Claude looked it up minutes ago. The "fixed at build time" line is the honest caveat.
6. **Open the downloaded meridian-fx-live.html in your browser and click Refresh.**
   Same design, but running outside the sandbox, so THIS one really does fetch live rates. That contrast is the lesson.
7. **Ask for one refinement in plain English, for example: Add a thousands separator to the result.**
   Refining by conversation is the normal way to work — you never edit the code yourself.
8. **Save the artefact so it appears in your sidebar.**
   A saved artefact persists as a reusable tool; an unsaved one scrolls away with the chat.

## Check your work

The artefact converts S$10,000 to USD with no error, shows the rate used and a "Rates as at … — fixed at build time" line, and the rate matches a live search. Separately, meridian-fx-live.html opens in your browser, fetches its own rates and updates them when you click Refresh. The artefact is saved in your sidebar.

## Further viewing

- [CLAUDE COWORK FULL COURSE 3 HOURS For Beginners (2026)](https://www.youtube.com/watch?v=0UFSZ_5OSIk)

Optional background, not needed to complete the lab.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
