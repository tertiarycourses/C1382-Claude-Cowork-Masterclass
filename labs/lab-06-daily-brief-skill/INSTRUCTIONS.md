# Lab 06 — Build a /daily-brief Skill

**Topic 02 · Tools and Skills**

> Meridian Capital Partners Pte Ltd — all data in this lab is synthetic and for training only.

## Goal

Labs 4 and 5 showed what the connectors can do — but you had to describe the whole routine each time. Now you capture it once. The reliable way to build a skill is the Do / Verify / Save pattern: do the task with Claude once, refine until the output is right, then use the /skill-creator skill to save it. You have already done the doing — this lab turns it into a command, then updates it.

## You'll build

A daily-brief Agent Skill you can run by name each morning, updated once.

**Tools:** Claude Cowork, Agent Skills, /skill-creator, Google Drive connector, Gmail connector

## The prompt

Copy this into Claude (it is also in [PROMPT.md](PROMPT.md)):

```text
Step 1 — DO. Run my morning finance briefing for Meridian Capital
Partners, once, so we can get the format right together:

- What changed in the Meridian Finance folder on Google Drive since
  yesterday?
- Which desks are behind their quarterly target right now?
- What finance emails do I need to respond to today?

If a section has nothing in it, say so plainly — "No new files since
yesterday" — rather than padding it out. End with one line on what most
needs my attention, or "Nothing urgent — have a good day" if there is
nothing. All money in Singapore dollars. Draft only — never send email.

Step 2 — SAVE. Once I confirm the output is right, use the
/skill-creator skill to turn exactly this routine into a skill called
daily-brief that I can run every morning.
```

> **Note:** Do it once, check the output, then save it — that order is what makes the skill reliable.

## Steps

1. **Make sure the Drive and Gmail connectors from Labs 4 and 5 are still enabled.**
   The skill drives those connectors, so it can only work if they are on.
2. **DO — paste Step 1 of the lab prompt and let Claude run the routine once.**
   You are not writing instructions yet; you are doing the task together so Claude sees what good looks like.
3. **VERIFY — read the briefing and ask for changes until the format is right.**
   Reorder a section, tighten the wording, fix a heading. Whatever you settle on here is what the skill will reproduce.
4. **Check the fallback wording on any empty section.**
   The fallbacks are what stop the routine inventing filler on a quiet morning — get them right before you save.
5. **Confirm it drafted and did not send anything.**
   A routine you will run unattended must not be able to send mail on its own.
6. **SAVE — run Step 2 so /skill-creator turns the routine into a daily-brief skill.**
   The skill-creator skill writes the SKILL.md for you, from the run you just verified.
7. **Read the SKILL.md it produces, especially the description line.**
   The description is how Claude decides whether to load the skill for a future task — make it specific.
8. **Run the skill by name, then run it again.**
   The same structure both times is the payoff: one command instead of re-describing the routine every morning.
9. **UPDATE — ask for one change, such as putting the emails section first.**
   A skill is not written once. You keep refining it as you learn what you actually want each morning.
10. **Save the change under the same skill name and confirm the replace prompt.**
   Claude warns that a skill with this name already exists and that replacing it cannot be undone — read that prompt before you accept it.
11. **Run the skill once more to confirm the change took effect.**
   Always re-run after an update; that is how you know the new version is the one being loaded.

## Check your work

Running the daily-brief skill by name produces a briefing with all three sections — Drive changes, desks behind target, emails needing a reply — using the plain fallback wording where a section is empty, ending with a single attention line, with all money in SGD and no email sent. After the update, the revised section order appears on the next run — and Claude warned you before replacing the existing skill.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
