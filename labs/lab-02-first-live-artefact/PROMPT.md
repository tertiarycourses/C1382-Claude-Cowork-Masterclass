# Lab 02 prompt — Build your first Live Artefact

Copy everything in the block below into Claude.

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
