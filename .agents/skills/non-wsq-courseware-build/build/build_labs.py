#!/usr/bin/env python3
"""
Generate labs/lab-NN-*.md and labs/README.md from the SAME single source
(course_data.py + data_domainN.py) that drives the PPT, LP and LG — so the
lab files can never drift out of alignment with the other artifacts.
"""
import os, re, sys, glob, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C

def find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(start))

REPO = find_repo(HERE)
LABS = os.path.join(REPO, "labs")
os.makedirs(LABS, exist_ok=True)

# ---- collect labs from every data_domainN.py, in domain order
labs = []
for path in sorted(glob.glob(os.path.join(HERE, "data_domain[0-9]*.py"))):
    mod = importlib.import_module(os.path.basename(path)[:-3])
    for name in dir(mod):
        if re.fullmatch(r"DOMAIN\d+", name):
            labs.extend(getattr(mod, name))
labs.sort(key=lambda l: l["num"])

TOPICS = {t["num"]: t for t in C.TOPICS}

def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")

# Fail fast before writing any files: contiguous numbering and complete lab
# records are alignment invariants for the PPT, LP, LG, and lab set.
expected_nums = list(range(1, len(labs) + 1))
actual_nums = [lab.get("num") for lab in labs]
assert actual_nums == expected_nums, f"Lab numbers must be contiguous 1..N; got {actual_nums}"
assert len({slug(lab.get("title", "")) for lab in labs}) == len(labs), "Lab filenames would not be unique"
required_fields = {"num", "topic", "title", "objective", "duration", "desc", "build", "services", "steps", "test"}
for lab in labs:
    missing = required_fields - set(lab)
    assert not missing, f"Lab {lab.get('num')} missing required fields: {sorted(missing)}"
    assert lab["topic"] in TOPICS, f"Lab {lab['num']} uses unknown topic {lab['topic']}"
    assert lab["steps"] and all(isinstance(step, tuple) and len(step) == 2 for step in lab["steps"]), f"Lab {lab['num']} has invalid steps"
    assert re.fullmatch(r"\d+ minutes", lab["duration"]), f"Lab {lab['num']} has invalid duration {lab['duration']!r}"

def fence(cmd):
    """Prompts contain no backticks; render them as a plain fenced block."""
    return "```text\n" + cmd.strip() + "\n```"

written = []
for lab in labs:
    n = lab["num"]
    topic = TOPICS.get(lab["topic"], {})
    fname = f"lab-{n:02d}-{slug(lab['title'])}.md"
    written.append((n, fname, lab, topic))

    L = []
    L.append(f"# Lab {n} — {lab['title']}\n")
    L.append(f"- **Course:** {C.TITLE}")
    L.append(f"- **Version:** {C.VERSION} ({C.VERSION_DATE})")
    L.append(f"- **Topic {lab['topic']}:** {topic.get('title','')}")
    L.append(f"- **Maps to:** {lab['objective']}")
    L.append(f"- **Tools:** {lab['services']}\n")
    L.append(f"**Duration:** {lab.get('duration','Refer to the Lesson Plan')}\n")
    L.append("---\n")
    L.append("## What You Will Do\n")
    L.append(lab["desc"] + "\n")
    L.append("## What You Will Build\n")
    L.append(lab["build"] + "\n")
    if lab.get("prerequisites"):
        L.append("## Prerequisites\n")
        for item in lab["prerequisites"]:
            L.append(f"- {item}")
        L.append("")
    if n > 1:
        L.append("> **Rejoin path.** If a prerequisite artifact is missing, use the Rejoin Path in [the labs index](README.md), reconstruct the named checkpoint, and verify it before continuing.\n")
    L.append(f"> **Data note.** {C.LAB_NOTE}\n")
    L.append("## Steps\n")
    for i, (instr, cmd) in enumerate(lab["steps"], 1):
        L.append(f"**{i}. {instr}**\n")
        if cmd.strip():
            L.append(fence(cmd) + "\n")
    L.append("## Test It\n")
    L.append(lab["test"] + "\n")
    if lab.get("checkpoint"):
        L.append("## Checkpoint for the Next Lab\n")
        L.append(lab["checkpoint"] + "\n")
    if lab.get("troubleshooting"):
        L.append("## Troubleshooting\n")
        for issue, fix in lab["troubleshooting"]:
            L.append(f"- **{issue}:** {fix}")
        L.append("")
    if lab.get("challenge"):
        L.append("## Challenge\n")
        L.append(lab["challenge"] + "\n")
    if lab.get("reflection"):
        L.append("## Reflection\n")
        L.append(lab["reflection"] + "\n")
    L.append("---\n")
    prev = f"[← Lab {n-1}](lab-{n-1:02d}-{slug(labs[n-2]['title'])}.md)" if n > 1 else "[← Labs index](README.md)"
    nxt  = f"[Lab {n+1} →](lab-{n+1:02d}-{slug(labs[n]['title'])}.md)" if n < len(labs) else "[Labs index →](README.md)"
    L.append(f"{prev} · {nxt}\n")

    with open(os.path.join(LABS, fname), "w", encoding="utf-8") as f:
        f.write("\n".join(L))

# ---- labs/README.md index
lab_minutes = sum(int(re.match(r"\d+", lab["duration"]).group()) for lab in labs)
lab_time = f"{lab_minutes // 60} h {lab_minutes % 60:02d} min" if lab_minutes % 60 else f"{lab_minutes // 60} h"
R = [f"# {C.TITLE} — Hands-On Labs\n",
     f"{len(labs)} labs across {len(C.TOPICS)} topics · {C.DAYS} {'day' if C.DAYS == 1 else 'days'} · "
     f"{C.INSTRUCTIONAL_HOURS:g} instructional hours · {C.CLOCK_HOURS:g} clock hours including tea breaks · {lab_minutes/60:g} hands-on lab hours\n",
     "Work through the labs in order — each one builds on the artifacts you produced "
     "in the labs before it.\n"]
R[1] = R[1].replace(f"{lab_minutes/60:g} hands-on lab hours", f"{lab_time} hands-on lab time")
R.append("\n## Rejoin Path\n")
R.append("If you join after Lab 1 or resume after a gap, do not skip the connected inputs. Reconstruct and verify the smallest baseline below before starting the target lab. The supplied starter files reduce setup time but do not replace the required checks.\n")
R.append("| Rejoin point | Minimum verified baseline |")
R.append("|---|---|")
for point, baseline in C.REJOIN_PATH:
    R.append(f"| {point} | {baseline} |")
for t in C.TOPICS:
    R.append(f"\n## Topic {t['num']} — {t['title']}\n")
    R.append("| # | Lab | Tools | You Build |")
    R.append("|---|-----|-------|-----------|")
    for n, fname, lab, _tp in written:
        if lab["topic"] == t["num"]:
            R.append(f"| {n} | [{lab['title']}]({fname}) | {lab['services']} | {lab['build']} |")
R.append(f"\n---\n\n> {C.LAB_NOTE}\n")
R.append(f"\n_{C.ORG} · {C.COURSE_CODE} · {C.VERSION} ({C.VERSION_DATE})_\n")

with open(os.path.join(LABS, "README.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(R))

print(f"Saved {len(labs)} lab files + README.md to {LABS}")
