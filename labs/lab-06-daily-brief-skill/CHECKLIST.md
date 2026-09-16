# Lab 06 checklist — Build a /daily-brief Skill

- [ ] Make sure the Drive and Gmail connectors from Labs 4 and 5 are still enabled.
- [ ] DO — paste Step 1 of the lab prompt and let Claude run the routine once.
- [ ] VERIFY — read the briefing and ask for changes until the format is right.
- [ ] Check the fallback wording on any empty section.
- [ ] Confirm it drafted and did not send anything.
- [ ] SAVE — run Step 2 so /skill-creator turns the routine into a daily-brief skill.
- [ ] Read the SKILL.md it produces, especially the description line.
- [ ] Run the skill by name, then run it again.
- [ ] UPDATE — ask for one change, such as putting the emails section first.
- [ ] Save the change under the same skill name and confirm the replace prompt.
- [ ] Run the skill once more to confirm the change took effect.

## Done when

- [ ] Running the daily-brief skill by name produces a briefing with all three sections — Drive changes, desks behind target, emails needing a reply — using the plain fallback wording where a section is empty, ending with a single attention line, with all money in SGD and no email sent. After the update, the revised section order appears on the next run — and Claude warned you before replacing the existing skill.
