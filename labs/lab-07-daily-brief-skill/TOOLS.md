# Lab 07 — tools

This lab uses the following, all within Topic 02 (Tools and Skills):

- **Claude Cowork**
- **Agent Skills**
- **/skill-creator**
- **Google Drive connector**
- **Gmail connector**
- **Scheduled tasks**

## Turning connectors on

Click the **+** in the chat composer, hover **Connectors**, and toggle on only
what this lab needs. You can manage them later under **Customize → Connectors**.

## Running a slash command

`/skill-creator` is typed into the composer, not written inside a longer prompt.
Start typing `/` and it appears in the list — select it, then describe the skill
you want saved. The skill you create here is run the same way, as `/daily-brief`.

## Scheduled tasks

A scheduled task runs a prompt on a timetable without you. Open **Scheduled
tasks** from the sidebar and choose **New task**. *Create with Claude* fills the
task in for you by asking a few questions; *Set up manually* opens the dialog and
lets you set every field yourself. This lab sets it up manually.

The dialog asks for a **Name** and **Instructions**, lets you pick the project or
folder to work in and the **Default model**, and sets a **Frequency** — the default
is Manual, so you must change it to run daily.

Two settings deserve a moment. **Permissions** defaults to *Automatically approve*,
which means Claude uses your connectors unattended, without pausing to ask. That is
exactly why this skill drafts and never sends: an unattended task that could send
mail is how an unreviewed email reaches a real client. Because it drafts only, the
worst case is a draft nobody wanted.

**Require this computer** is off by default. On, the task only runs while your
computer is awake, but it can reach the folders you have allowed on it. Off, it
runs without them. Choose to match where the task's data actually lives.

## Keep it scoped

Point Claude at the one folder or mailbox the task needs — never your whole
Drive or inbox. Claude asks for approval before it sends mail or changes a file;
read the draft and check the figures before you approve.
