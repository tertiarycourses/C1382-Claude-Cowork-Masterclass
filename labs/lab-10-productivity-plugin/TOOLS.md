# Lab 10 — tools

This lab uses the following, all within Topic 03 (Claude Projects and Plugins):

- **Claude Cowork**
- **Plugins**
- **the Productivity plugin**

## Skills and plugins live in the same place

Open the **Plugins** panel. It has two tabs — **Your plugins** and **Discover** —
with a search box reading "Search skills and plugins", plus Filter and Sort
controls. Cards in Discover show the publisher and how many people installed it.

## A skill versus a plugin

A skill is ONE routine you wrote. A plugin is the whole setup — hand a colleague
the plugin and they get every skill, tool and agent it contains.

The clearest tell is the command name. Your own skills run as `/daily-brief`. A
plugin's run as `/productivity:start` — the `plugin:command` prefix shows at a
glance that it came from a bundle rather than a folder you wrote yourself.

## What the Productivity plugin does

It ships two commands. `/productivity:start` sets up the task and memory systems;
`/productivity:update` syncs tasks from external sources and triages stale items.
Tasks live in a `TASKS.md` file with Active, Waiting On, Someday and Done
sections — a real file in your folder, not state hidden inside the app.

It can also connect to Asana, Linear, Jira, Monday, ClickUp, Notion, Slack and
Microsoft 365. Those need connecting separately and this lab does not use them —
but they are why a plugin is how a whole team adopts one toolkit at once.

## No connector needed

This lab uses no connector and no mock data. The tasks you track are the real
loose ends the earlier labs produced.
