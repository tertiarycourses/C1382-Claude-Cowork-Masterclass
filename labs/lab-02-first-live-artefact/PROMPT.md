# Lab 02 prompt — Build your first Live Artefact

Copy everything in the block below into Claude.

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
