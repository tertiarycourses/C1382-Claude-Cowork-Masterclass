# Lab 07 checklist — Build a /daily-brief Skill

- [ ] Make sure the Drive and Gmail connectors from Labs 4 and 5 are still enabled.
- [ ] DO — send block 1 on its own and let Claude run the routine once.
- [ ] VERIFY — read the briefing and ask for changes until the format is right.
- [ ] Check the fallback wording on any empty section.
- [ ] Confirm it drafted and did not send anything.
- [ ] SAVE — type `/skill-creator` in the composer, then send block 2.
- [ ] Read the SKILL.md it produces, especially the description line.
- [ ] Run the skill by typing `/daily-brief`, then run it again.
- [ ] UPDATE — ask for one change, such as putting the emails section first.
- [ ] Save the change under the same skill name and confirm the replace prompt.
- [ ] Run `/daily-brief` once more to confirm the change took effect.
- [ ] Open Scheduled tasks from the sidebar, choose New task, then Set up manually.
- [ ] Name the task "Daily briefing".
- [ ] Paste Block 3 into the Instructions field.
- [ ] Point "Work in a project or folder" at the folder you have been working in.
- [ ] Set Frequency to run daily at 9:00am.
- [ ] Read the Permissions setting and understand what "Automatically approve" means.
- [ ] Decide whether to switch on "Require this computer".
- [ ] Save the task, then run it once manually to confirm it works.
- [ ] Check Gmail for a draft titled "Meridian daily brief" and confirm nothing was sent.

## Done when

- [ ] Running `/daily-brief` produces a briefing with all three sections — Drive changes, desks behind target, emails needing a reply — using the plain fallback wording where a section is empty, ending with a single attention line, with all money in SGD and no email sent. After the update, the revised section order appears on the next run — and Claude warned you before replacing the existing skill. A scheduled task named "Daily briefing" exists, set to run daily at 9:00am, and running it manually leaves a Gmail draft titled "Meridian daily brief" with today's date, while your Sent folder stays empty.
