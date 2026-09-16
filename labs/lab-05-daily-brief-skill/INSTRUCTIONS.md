# Lab 05 — Build a /daily-brief Skill

**Topic 02 · Tools and Skills**

> Meridian Capital Partners Pte Ltd — all data in this lab is synthetic and for training only.

## Goal

Labs 3 and 4 showed what the connectors can do — but you had to describe the whole routine each time. Now you capture it once as an Agent Skill. Every morning you type one command and Claude checks Drive and Gmail and briefs you on where Meridian's reporting stands, in the same format every day.

## You'll build

A daily-brief Agent Skill you can run by name each morning.

**Tools:** Claude Cowork, Agent Skills, Google Drive connector, Gmail connector

## The prompt

Copy this into Claude (it is also in [PROMPT.md](PROMPT.md)):

```text
I want to create an automation. I want this to be a daily briefing
automation for my finance work at Meridian Capital Partners.

The goal: every morning when I come into Claude, I type /daily-brief
and it runs the routine and catches me up on everything:

- What changed in the Meridian Finance folder on Google Drive since
  yesterday?
- Which desks are behind their quarterly target right now?
- What finance emails do I need to respond to today?

I want fallbacks. If there is nothing in a section, say so plainly —
"No new files since yesterday" — rather than padding it out.
End with one line on what most needs my attention, or "Nothing
urgent — have a good day" if there is nothing.

Keep all money in Singapore dollars with thousands separators.
Draft only — never send an email as part of this routine.

Save this as a skill I can reuse, and show me the finished SKILL.md.
```

> **Note:** The description line is what tells Claude when to load the skill — keep it specific.

## Steps

1. **Make sure the Drive and Gmail connectors from Labs 3 and 4 are still enabled.**
   The skill drives those connectors, so it can only work if they are on.
2. **Paste the lab prompt into Cowork.**
   You are describing the routine once; Claude writes it into the skill structure.
3. **Read the SKILL.md Claude produces, starting with the description line.**
   The description is how Claude decides whether to load the skill for a future task.
4. **Check each of the three sections is there, with its fallback wording.**
   The fallbacks are what stop the routine inventing filler on a quiet morning.
5. **Confirm the skill drafts only and never sends — ask for a correction if not.**
   A routine that runs unattended must not be able to send mail on its own.
6. **Save the skill, then run it by name to see the briefing.**
   This is the payoff: one command instead of re-describing the whole routine.
7. **Run it a second time and confirm the format is identical.**
   Consistency is the point of a skill — the same structure every single run.

## Check your work

Running the skill produces a briefing with all three sections — Drive changes, desks behind target, emails needing a reply — using the plain fallback wording where a section is empty, ending with a single attention line, with all money in SGD and no email sent.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
