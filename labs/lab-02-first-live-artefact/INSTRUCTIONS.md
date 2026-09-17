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
Two things, in order.

1. Look up today's mid-market exchange rates from SGD to USD, EUR
   and GBP, and tell me the rates and the date you found them.

2. Build me a Live Artefact: a currency converter for Meridian
   Capital Partners using exactly those rates.
   - Convert between SGD, USD, EUR and GBP.
   - One amount box, a from-currency and a to-currency selector,
     and a large result.
   - Under the result show the rate used, and a line saying
     "Rates as at <the date you looked them up>".
   - Clean, professional finance styling. Label it "Meridian
     Capital Partners".

Make it interactive so I can change the amount and see the result
update.

Then give me the same converter as a standalone HTML file I can
download, and in that version fetch the rates live from a free
no-key API when the page opens, with a Refresh button.
```

> **Note:** An artefact cannot call an external API — that is a sandbox rule, not a bug. Claude looks the rates up for you and builds them in; the downloadable HTML runs in your browser, so it can fetch live.

## Steps

1. **Start a new Cowork session — this lab needs no files.**
   Lab 1 gave Claude a folder to work in; here you are asking it to build something from nothing.
2. **Paste the lab prompt into the composer and send it.**
   Claude writes the code and renders the converter in the preview pane beside the chat.
3. **Try the converter: change the amount and switch the currencies.**
   This is what makes it an artefact rather than an answer — you can interact with it.
4. **Check the rate Claude found against a search for "1 USD to SGD".**
   Claude looked this up while building, so it should match today. The artefact itself cannot call an API — the sandbox blocks outbound requests — so the rate is baked in at build time.
5. **Open the downloaded HTML file in your browser and click Refresh.**
   Same converter, but running in your browser instead of the sandbox, so it CAN fetch live rates. This is the practical difference between an artefact and a file you own.
6. **Ask for one refinement in plain English, for example: Add a thousands separator to the result.**
   Refining by conversation is the normal way to work — you never edit the code yourself.
7. **Save the artefact so it appears in your sidebar.**
   A saved artefact persists as a reusable tool; an unsaved one scrolls away with the chat.
8. **Download a copy of the artefact to your lab folder.**
   Downloading gives you a file you can keep, attach or hand to someone without Claude.

## Check your work

The artefact converts S$10,000 to USD using the rate Claude looked up, and shows a "Rates as at …" line with today's date. The downloaded HTML file opens in your browser, fetches rates itself and updates them when you click Refresh. The artefact appears in your sidebar after saving and still works when reopened.

## Further viewing

- [CLAUDE COWORK FULL COURSE 3 HOURS For Beginners (2026)](https://www.youtube.com/watch?v=0UFSZ_5OSIk)

Optional background, not needed to complete the lab.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
