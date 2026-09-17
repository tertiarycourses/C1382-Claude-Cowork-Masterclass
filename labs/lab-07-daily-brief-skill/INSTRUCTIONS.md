# Lab 07 — Build a /daily-brief Skill

**Topic 02 · Tools and Skills**

> Meridian Capital Partners Pte Ltd — all data in this lab is synthetic and for training only.

## Goal

Labs 4 and 5 showed what the connectors can do, and Lab 6 showed a built-in skill doing the work for you. Now you write one yourself. The reliable way to build a skill is the Do / Verify / Save pattern: do the task with Claude once, refine until the output is right, then use `/skill-creator` to save it. You have already done the doing — this lab turns it into a command, then updates it. Finally you schedule it, so the briefing is waiting as a draft before you sit down rather than something you have to remember to ask for.

## You'll build

A daily-brief Agent Skill you can run by name each morning, updated once and scheduled to run itself at 9am.

**Tools:** Claude Cowork, Agent Skills, /skill-creator, Google Drive connector, Gmail connector, Scheduled tasks

## The prompt

This lab has **three blocks**, sent at different times. Blocks 1 and 2 are typed into the chat composer — block 1 does the work, and block 2 saves it once you are happy with the output. Block 3 schedules it. All three are also in [PROMPT.md](PROMPT.md).

### Block 1 — DO

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

**Now stop and read the output.** Ask for changes until the format is right — reorder a section, tighten a heading, fix the fallback wording. Whatever you settle on here is exactly what the skill will reproduce every morning. Do not continue until you are happy with it.

### Block 2 — SAVE

Only once the output is right, type `/skill-creator` into the composer. It appears in the slash-command list as you type — select it, then add your description after it:

```text
/skill-creator Save the morning finance briefing routine we just ran as
a skill called daily-brief. Keep the three sections in the order we
settled on, the plain fallback wording for empty sections, the single
closing attention line, all money in Singapore dollars, and draft-only —
never send email.
```

> **Note:** `/skill-creator` is a slash command **you** type, the same way you will later run `/daily-brief`. It is not something Claude invokes for you from inside a longer prompt.

### Block 3 — SCHEDULE

This one does not go in the chat. Open the **Create scheduled task** dialog and paste it into the **Instructions** field:

```text
Run my daily-brief skill for Meridian Capital Partners.

Leave the briefing as a draft email to me in Gmail, with the subject
"Meridian daily brief" and today's date. Do not send it.

If a section has nothing in it, keep the plain fallback wording rather
than padding it out.
```

Notice it **names the skill** rather than restating the routine — that is what saving the skill bought you. Notice too that it repeats *Do not send it* even though the skill is already draft-only. A scheduled task is the one place you state a safety rule twice: it runs unattended with Permissions set to *Automatically approve*, so both the instruction and the skill carry the constraint.

> **Note:** Do it once, check the output, then save it — that order is what makes the skill reliable.

## Steps

1. **Make sure the Drive and Gmail connectors from Labs 4 and 5 are still enabled.**
   The skill drives those connectors, so it can only work if they are on.
2. **DO — send block 1 on its own and let Claude run the routine once.**
   You are not writing instructions yet; you are doing the task together so Claude sees what good looks like.
3. **VERIFY — read the briefing and ask for changes until the format is right.**
   Reorder a section, tighten the wording, fix a heading. Whatever you settle on here is what the skill will reproduce.
4. **Check the fallback wording on any empty section.**
   The fallbacks are what stop the routine inventing filler on a quiet morning — get them right before you save.
5. **Confirm it drafted and did not send anything.**
   A routine you will run unattended must not be able to send mail on its own.
6. **SAVE — type `/skill-creator` in the composer, then send block 2.**
   You type the slash command yourself and pick it from the list; it then writes the SKILL.md for you, from the run you just verified.
7. **Read the SKILL.md it produces, especially the description line.**
   The description is how Claude decides whether to load the skill for a future task — make it specific.
8. **Run the skill by typing `/daily-brief`, then run it again.**
   The same structure both times is the payoff: one command instead of re-describing the routine every morning.
9. **UPDATE — ask for one change, such as putting the emails section first.**
   A skill is not written once. You keep refining it as you learn what you actually want each morning.
10. **Save the change under the same skill name and confirm the replace prompt.**
    Claude warns that a skill with this name already exists and that replacing it cannot be undone — read that prompt before you accept it.
11. **Run `/daily-brief` once more to confirm the change took effect.**
    Always re-run after an update; that is how you know the new version is the one being loaded.
12. **Open Scheduled tasks from the sidebar, choose New task, then Set up manually.**
    The other route, Create with Claude, fills the task in for you by asking questions; setting it up manually shows you every field it will set.
13. **Name the task "Daily briefing".**
    The skill captures WHAT to do; the schedule captures WHEN. Two different kinds of reuse, and this is the second one.
14. **Paste Block 3 into the Instructions field.**
    It names the skill you just built rather than re-describing the routine — that is what saving it bought you. It also repeats "Do not send it", because a scheduled task is the one place you state a safety rule twice.
15. **Point "Work in a project or folder" at the folder you have been working in.**
    The task needs the same working folder and connectors the skill expects.
16. **Set Frequency to run daily at 9:00am.**
    Before you sit down, so the briefing is waiting rather than something you go and fetch.
17. **Read the Permissions setting and understand what "Automatically approve" means.**
    The task will use your connectors unattended, without pausing to ask. This is exactly why the skill drafts and never sends — an unattended task that could send mail is how an unreviewed email reaches a real client.
18. **Decide whether to switch on "Require this computer".**
    On, it only runs while your computer is awake but can reach your local folders; off, it runs without them. Choose to match where the task's data actually lives.
19. **Save the task, then run it once manually to confirm it works.**
    Never leave a scheduled task untested — the first time it runs should not be the morning you are relying on it.
20. **Check Gmail for a draft titled "Meridian daily brief" and confirm nothing was sent.**
    A draft in your Drafts folder and an empty Sent folder is the proof the constraint held.

## Check your work

Running `/daily-brief` produces a briefing with all three sections — Drive changes, desks behind target, emails needing a reply — using the plain fallback wording where a section is empty, ending with a single attention line, with all money in SGD and no email sent. After the update, the revised section order appears on the next run — and Claude warned you before replacing the existing skill. A scheduled task named "Daily briefing" exists, set to run daily at 9:00am, and running it manually leaves a Gmail draft titled "Meridian daily brief" with today's date, while your Sent folder stays empty.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
