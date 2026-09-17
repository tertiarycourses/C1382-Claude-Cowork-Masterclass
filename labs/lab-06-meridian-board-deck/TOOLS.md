# Lab 06 — tools

This lab uses the following, all within Topic 02 (Tools and Skills):

- **Claude Cowork**
- **Google Drive connector**
- **the built-in pptx skill**

## A skill you did not write

Claude ships with a **pptx** skill for creating PowerPoint files. You do not
enable it, install it or call it by name — its description matches "build me a
PowerPoint", so Claude loads it on demand. This is the same mechanism you will
use deliberately in Labs 7 and 8, where you write skills of your own with
`/skill-creator`. Lab 6 is where you see one work before you build one.

**You will not find pptx in the Skills panel**, and you do not need to add it.
That panel lists skills you manage — ones you added from Discover or wrote
yourself. Built-in skills are not listed there and cannot be switched off.

Where you *can* see it is the **Context** panel in the sidebar. Open it while the
task runs and it shows everything loaded for this job: the working folder, the
connectors that are on, and under **Skills**, `pptx`. That panel is the clearest
answer to "what is in Claude's context right now" — the same question the Context
Window slides ask. Look at it during this lab.

## Turning connectors on

Click the **+** in the chat composer, hover **Connectors**, and toggle on only
what this lab needs. You can manage them later under **Customize → Connectors**.

## Why no Microsoft 365 connector

The pptx skill builds the file and hands it to you as a download — no connector
is involved. The Microsoft 365 connector is read-only unless an administrator
enables its write tools, so it cannot save a new file into OneDrive on a standard
account. A skill that creates the file directly works on every plan, which is a
useful thing to know: not every job needs a connector.

## Keep it scoped

Point Claude at the one Drive folder the task needs — never your whole Drive.
Check the figures in the finished deck against the dashboard before you treat it
as done; a generated file is still your responsibility.
