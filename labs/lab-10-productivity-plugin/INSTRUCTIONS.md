# Lab 10 — Add the Productivity Plugin

**Topic 03 · Claude Projects and Plugins**

> Meridian Capital Partners Pte Ltd — all data in this lab is synthetic and for training only.

## Goal

Lab 9 packaged your own setup so a colleague could open it and be productive. This lab runs the same idea in the opposite direction: you install a toolkit somebody else packaged.

That is the difference between a skill and a plugin. A skill is one routine you wrote — `/daily-brief` in Lab 7, `/brand-deck` in Lab 8. A plugin is the whole setup: several skills plus the tools they need, installed together in one click. You use Anthropic's Productivity plugin to track the follow-ups this course has actually generated, inside the Meridian project you just built.

## You'll build

The Productivity plugin installed, with a TASKS.md tracking your Meridian follow-ups.

**Tools:** Claude Cowork, Plugins, the Productivity plugin

## The prompt

Copy this into Claude (it is also in [PROMPT.md](PROMPT.md)):

```text
/productivity:start
```

> **Note:** This lab has no long prompt to paste — it is driven by the plugin's own commands. Note the `productivity:` prefix: that is how you tell a plugin's command from a skill you wrote.

## Steps

1. **Open the Plugins panel and switch to the Discover tab.**
   The search box covers "skills and plugins" — both live in the same place, which is the first hint that a plugin is a container for skills.
2. **Find the Productivity plugin from Anthropic and click Add.**
   It is described as "Tasks, planning and follow-ups — the everyday toolkit." The card shows the publisher and the install count.
3. **Check Your plugins to confirm it installed.**
   The two tabs separate what you have from what is available — the same split as a package manager.
4. **Type `/` in the composer and find the new `/productivity:` commands.**
   Note the prefix. These came from a bundle, unlike `/daily-brief` which you wrote yourself. That prefix is how you tell at a glance where a command came from.
5. **Open the Meridian project from Lab 9 and run `/productivity:start` there.**
   The plugin works on the project you already built, so the tasks it tracks are real work rather than invented ones.
6. **Answer whatever it asks and let it create the task list.**
   It sets up its task and memory systems for this project the first time you run it.
7. **Open `TASKS.md` in the project folder and read the sections.**
   Active, Waiting On, Someday and Done. Like the project itself, it is a real file you own — not state hidden inside the app.
8. **Add the follow-ups this course actually produced.**
   Chase the S$90,000 Q4 Advisory target discrepancy with Finance; review the FY2025 board deck before it goes to the board; confirm tomorrow's daily brief arrived as a draft. Genuine loose ends from Labs 4-8, which is why this lab can close the course honestly.
9. **Run `/productivity:update` and see it triage.**
   It syncs from any connected source and flags what has gone stale — the maintenance half of a task system, which is the half people skip.
10. **Note what the plugin could also connect to.**
    Asana, Linear, Jira, Monday, ClickUp, Notion, Slack and Microsoft 365. A plugin is how a whole team adopts the same toolkit at once, rather than each person writing their own version of it.

## Check your work

The Productivity plugin appears under Your plugins, and typing `/` lists its `/productivity:` commands alongside the `/daily-brief` and `/brand-deck` skills you wrote. A `TASKS.md` file exists in the Meridian project folder with Active, Waiting On, Someday and Done sections, and it holds at least the three Meridian follow-ups: the Q4 Advisory target discrepancy, the board deck review, and the daily-brief draft check.

## Before you move on

Use only the supplied mock data and your own test accounts. Never put real client, personal or confidential data into a training exercise, and send lab emails to yourself rather than to a real recipient.
