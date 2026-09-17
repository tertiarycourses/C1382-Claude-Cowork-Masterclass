# Lab 08 — Brand the Board Deck

**Topic 02 · Tools and Skills**

> Meridian Capital Partners Pte Ltd — all data in this lab is synthetic and for training only.

## Goal

The board deck from Lab 6 has the right numbers and the wrong clothes — it looks like a default template. Meridian has a branded template every deck is supposed to follow; the problem is that applying it by hand, every time, is what nobody does.

So you do not describe the house style to Claude — you hand it the template and let it work the style out for itself. That is how branding actually reaches people in a firm: somebody sends you the template, not a list of hex values. You apply it once, check the result, then save it as a skill so any future deck can be branded by name — the same way you saved `/daily-brief` in Lab 7.

## You'll build

A brand-deck Agent Skill that applies the Meridian house style to any presentation.

**Tools:** Claude Cowork, Agent Skills, /skill-creator

## Mock data

The files for this lab are in `mock-data/`:

- `meridian-brand-template.pptx`

Leave these files unchanged — let Claude write its output elsewhere.

## The prompt

This lab is sent in **two separate messages**, not one. Block 1 does the work; block 2 saves it. Both are also in [PROMPT.md](PROMPT.md).

### Block 1 — DO

Attach both files — the template from `mock-data/` and the deck you downloaded in Lab 6 — then send this on its own:

```text
I have attached two files.

The first, meridian-brand-template.pptx, is our house template. Study
it and work out the style it uses: the colours, the fonts for headings
and body text, how the title slide is treated, the rule under each
slide title, and what goes in the footer.

The second is the "Meridian Capital Partners — FY2025 Board Review"
deck I built in the last lab. Apply the template's style to it so the
two look like the work of the same firm.

Tell me what style rules you took from the template before you apply
them, so I can check you read it correctly.

This is a restyle only — do not change any figure or any wording.
Give me the restyled .pptx to download when you are done.
```

**Now stop and look at the deck.** Open the restyled deck beside the template and check the title slide and one content slide — they should read as the same firm's work. Ask for changes until it looks right. Whatever you settle on here is what the skill will reproduce.

### Block 2 — SAVE

Only once the deck looks right, type `/skill-creator` into the composer. It appears in the slash-command list as you type — select it, then add your description after it:

```text
/skill-creator Save what we just did as a skill called brand-deck that
applies the Meridian house style to any presentation. Write the actual
colours, fonts, title treatment and footer you took from the template
into the skill, so it works on a deck later without me attaching the
template again. Never change figures or wording — restyle only.
```

The skill records the style values Claude read off the template. That is the point of saving it: from now on the house style travels with the skill, and nobody has to find the template first.

> **Note:** `/skill-creator` is a slash command **you** type, the same way you ran `/daily-brief` in Lab 7. It is not something Claude invokes for you from inside a longer prompt.

> **Note:** Restyle only. A branding skill that is allowed to touch the numbers is a branding skill that will eventually change one.

## Steps

1. **Attach the template from `mock-data/` and the PowerPoint you downloaded in Lab 6.**
   Claude learns the style from the template and applies it to the deck, so it needs both files in front of it.
2. **DO — send block 1 on its own and let Claude study the template.**
   You are not describing the house style; you are handing over an example and letting Claude read it — which is how a template reaches anyone in a real firm.
3. **Read the style rules Claude says it took from the template before it applies them.**
   If it misread the template, you find out now rather than in the finished deck.
4. **Open the restyled deck beside the template and compare the title slides.**
   Same background, same wordmark treatment, same rule. They should read as the work of one firm.
5. **Check a content slide against the template's content slide.**
   Heading colour and typeface, the rule under the title, the body font, and the footer lockup with the slide number.
6. **Confirm no figure and no wording changed.**
   Compare against the Lab 6 check: S$24,850,000, 214 deals, Q4 S$6,980,000, and the S$90,000 Advisory discrepancy still stated.
7. **VERIFY — ask for changes until the look is right.**
   Whatever you settle on now is what every future deck will inherit.
8. **SAVE — type `/skill-creator` in the composer, then send block 2.**
   You type the slash command yourself and pick it from the list; it writes the SKILL.md from the restyle you just verified.
9. **Read the SKILL.md it produces and check it recorded the actual style values.**
   A skill that says "match the template" needs the template. A skill that names the colours and fonts works on its own — that is what saving it is for.
10. **Attach another deck, type `/brand-deck`, and run it — without attaching the template.**
    The same house style landing on a deck the skill has never seen, with no template in the chat, is the whole point.

## Check your work

The restyled deck downloads and matches the template's look — the same background colours, heading and body typefaces, title treatment, rule under each title and footer lockup with the internal-use line and slide number. Every FY2025 and Q4 figure is unchanged from Lab 6, including the S$90,000 Advisory discrepancy. Running `/brand-deck` on a different presentation, with no template attached, applies the same house style.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
