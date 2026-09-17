# Lab 07 prompt — Do the routine, then save it as a skill

This lab has **three blocks**, sent at different times.

Blocks 1 and 2 are typed into the **chat composer**. Send block 1 first; only
after you have read the output and are happy with the format do you send block 2.

Block 3 is different: it is pasted into the **Instructions field of the
Create scheduled task dialog**, not into the chat.

## Block 1 — DO

Send this first, on its own:

```text
Run my morning finance briefing for Meridian Capital Partners, once,
so we can get the format right together:

- What changed in the Meridian Finance folder on Google Drive since
  yesterday?
- Which desks are behind their quarterly target right now?
- What finance emails do I need to respond to today?

If a section has nothing in it, say so plainly — "No new files since
yesterday" — rather than padding it out. End with one line on what most
needs my attention, or "Nothing urgent — have a good day" if there is
nothing. All money in Singapore dollars. Draft only — never send email.
```

**Stop here.** Read the briefing and ask for changes until the format is right.
Whatever you settle on is exactly what the skill will reproduce every morning.

## Block 2 — SAVE

Type `/skill-creator` into the composer. It appears in the slash-command list as
you type — select it, then add the description after it:

```text
/skill-creator Save the morning finance briefing routine we just ran as
a skill called daily-brief. Keep the three sections in the order we
settled on, the plain fallback wording for empty sections, the single
closing attention line, all money in Singapore dollars, and draft-only —
never send email.
```

## Block 3 — SCHEDULE

This block does not go in the chat composer. Open the **Create scheduled task**
dialog and paste it into the **Instructions** field:

```text
Run my daily-brief skill for Meridian Capital Partners.

Leave the briefing as a draft email to me in Gmail, with the subject
"Meridian daily brief" and today's date. Do not send it.

If a section has nothing in it, keep the plain fallback wording rather
than padding it out.
```

Notice it **names the skill** rather than restating the routine, and that it repeats
*Do not send it* even though the skill is already draft-only. A scheduled task is the
one place you state a safety rule twice.

> **Note:** Do it once, check the output, then save it — that order is what makes the skill reliable.
