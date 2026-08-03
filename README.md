<div align="center">

# Claude Cowork Masterclass

[![Course](https://img.shields.io/badge/Course-C1382-1f6feb?style=for-the-badge)](https://www.tertiarycourses.com.sg/claude-cowork-masterclass.html)
[![Claude Cowork](https://img.shields.io/badge/Built_for-Claude_Cowork-D97757?style=for-the-badge)](https://claude.com/product/cowork)
[![Format](https://img.shields.io/badge/Format-1_Day_Hands--On-14b8a6?style=for-the-badge)](#lab-activities)
[![Artifacts](https://img.shields.io/badge/Artifacts-PPTX_DOCX_XLSX-f59e0b?style=for-the-badge)](#what-youll-build)
[![License](https://img.shields.io/badge/License-Educational-fbbf24?style=for-the-badge)](#license)

**Delegate real knowledge work to Claude while retaining control of scope, evidence, quality, and consequential actions.**

[📘 Course Page](https://www.tertiarycourses.com.sg/claude-cowork-masterclass.html) · [📖 Learner Guide](LG-Claude%20Cowork%20Masterclass.md) · [🧪 Labs](labs/README.md) · [🐛 Report Bug](https://github.com/tertiarycourses/C1382-Claude-Cowork-Masterclass/issues) · [💡 Request Feature](https://github.com/tertiarycourses/C1382-Claude-Cowork-Masterclass/issues)

</div>

> [!NOTE]
> **These are the official courseware and hands-on materials for Claude Cowork Masterclass.**
> **Course Code:** `C1382` · **Duration:** one day, 7.5 hours · by Tertiary Courses / Tertiary Infotech
> **Course page:** https://www.tertiarycourses.com.sg/claude-cowork-masterclass.html

---

## Lab Activities

The three labs use one fictional Northstar Retail Operations workspace. Each verified checkpoint becomes the starting point for the next activity.

**Lab 1 — Delegate Your First Task to Claude Cowork** · Create a narrowly scoped Cowork project, write durable project instructions, brief a read-only file-inventory task, monitor its execution, and prove the protected inbox did not change.

**Lab 2 — Turn a Messy Folder into a Management-Ready Report** · Run parallel file, data, and evidence workstreams; reconcile the numbers at a human gate; then produce a consistent spreadsheet, written report, and leadership presentation.

**Lab 3 — Build a Repeatable Cowork Workflow for Your Own Work** · Convert the successful run into a parameterised playbook, choose the right integration path, rerun it for a new reporting week, and define a bounded team pilot.

---

## About

This repository contains the complete learning package for **Claude Cowork Masterclass** (`C1382`) by Tertiary Courses / Tertiary Infotech: an aligned slide deck, Learner Guide, Lesson Plan, and three connected labs.

The course treats Cowork as an agentic workspace for knowledge work. Learners practise giving Claude a clear outcome, narrowing its file and tool scope, monitoring multi-step work, reconciling evidence, producing professional business artifacts, and turning a successful session into a controlled repeatable playbook.

### What you'll learn

| Topic | Coverage | Hands-on outcome |
|---|---|---|
| **1. Getting Started with Claude Cowork** | Agentic operating model, setup, connected folders, task briefs, permissions, monitoring, and responsible use | A verified first delegated task |
| **2. Automating Everyday Work with Cowork** | File organisation, documents, reports, presentations, spreadsheet analysis, research synthesis, and end-to-end task design | A reconciled management pack |
| **3. Advanced Cowork Workflows** | Integrations, projects, repeatable playbooks, parallel workstreams, human gates, security, and team rollout | A reusable workflow proven on a new reporting week |

> 📖 **Full walkthrough:** start with the [Learner Guide](LG-Claude%20Cowork%20Masterclass.md). Generated slides and documents are in [`courseware/`](courseware/), while standalone activity instructions and the rejoin path are in [`labs/`](labs/).

---

## What You'll Build

| Stage | Artifacts | Evidence |
|---|---|---|
| **First delegation** | Cowork project instructions and a complete file inventory | Filename reconciliation and source hashes |
| **Management pack** | Analysis workbook, written operations report, and leadership presentation | Independent control totals, source register, visual review, and cross-artifact check |
| **Repeatable practice** | Parameterised playbook, integration decision, Week 33 pack, and rollout plan | Two human gates, new-period reconciliation, run log, and unchanged-source proof |

All supplied data is fictional. The labs use a working-copy pattern and keep `inbox/` read-only.

---

## Operating Model

```text
DEFINE
  Outcome + audience + source boundary + deliverables + stop conditions
      │
      ▼
PLAN
  Read set + write set + parallel workstreams + dependencies + human gates
      │
      ▼
EXECUTE
  Inventory ──┐
  Data work ──┼──▶ Reconcile evidence ──▶ Build artifacts
  Note work ──┘
      │                                  │
      ▼                                  ▼
CONTROL                              REVIEW
  Narrow permissions                  Totals + sources + visuals
  Working copies                      Cross-artifact consistency
  Consequential-action gates          Owner questions + release decision
      │                                  │
      └──────────────▶ EVOLVE THE PLAYBOOK ◀──────────────┘
```

---

## Tech Stack

| Category | Technology |
|---|---|
| **Agentic workspace** | [Claude Cowork](https://claude.com/product/cowork) on Claude Desktop |
| **Local context** | Narrow connected folder and Cowork project instructions |
| **Business outputs** | Excel-compatible `.xlsx`, Word-compatible `.docx`, PowerPoint-compatible `.pptx`, Markdown, and CSV |
| **Workflow controls** | Source contracts, working copies, control totals, source registers, human gates, run logs, and versioned playbooks |
| **Courseware** | PowerPoint slides generated with `python-pptx`; Learner Guide and Lesson Plan generated with `python-docx` |

---

## Project Structure

```text
C1382-Claude-Cowork-Masterclass/
├── README.md
├── LG-Claude Cowork Masterclass.md       # Full self-study guide
├── courseware/
│   ├── Claude Cowork Masterclass-v1.0.pptx
│   ├── Claude Cowork Masterclass-v1.0.pdf
│   ├── LG-Claude Cowork Masterclass.docx
│   ├── LG-Claude Cowork Masterclass.pdf
│   ├── LP-Claude Cowork Masterclass.docx
│   └── LP-Claude Cowork Masterclass.pdf
├── labs/
│   ├── README.md                         # Lab index and rejoin path
│   ├── lab-01-delegate-your-first-task-to-claude-cowork.md
│   ├── lab-02-turn-a-messy-folder-into-a-management-ready-report.md
│   ├── lab-03-build-a-repeatable-cowork-workflow-for-your-own-work.md
│   └── starter/northstar-operations/     # Fictional connected scenario
└── .agents/                              # Local courseware build source
```

---

## Getting Started

### Prerequisites

- A paid Claude plan with Cowork available.
- The latest Claude Desktop application for Windows or macOS.
- A spreadsheet application, word processor, and presentation application or compatible viewers.
- Git if you want to clone the repository; no coding is required for the labs.

### 1. Clone the repository

```bash
git clone https://github.com/tertiarycourses/C1382-Claude-Cowork-Masterclass.git
cd C1382-Claude-Cowork-Masterclass
```

### 2. Read the guide and lab index

1. Open [LG-Claude Cowork Masterclass.md](LG-Claude%20Cowork%20Masterclass.md).
2. Review [labs/README.md](labs/README.md) and the rejoin path.
3. Read `labs/starter/northstar-operations/00_READ_ME_FIRST.md` before connecting a folder.

### 3. Create a disposable working copy

Do not connect the whole course repository. Lab 1 gives Windows and macOS steps that copy only the fictional Northstar starter into a separate `C1382-northstar-workspace` folder.

### 4. Work through the labs in order

Each lab ends with a concrete **Test It** section, troubleshooting, a challenge, a reflection, and a verified checkpoint for the next lab.

---

## Responsible Use

- Use the minimum necessary approved context.
- Prefer read-only sources and new output folders.
- Separate source evidence, inference, and unresolved questions.
- Verify calculations, provenance, and visual artifacts before use.
- Require clear human authority before external writes, sharing, source replacement, removal, or commitments.
- Review current Anthropic guidance before enabling a new connection, computer use, remote execution path, or scheduled task.

---

## Contributing

Contributions, fixes, and improvements are welcome:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/my-improvement`.
3. Commit your changes: `git commit -m "Add my improvement"`.
4. Push the branch and open a pull request.

Found a bug or have an idea? Open an [issue](https://github.com/tertiarycourses/C1382-Claude-Cowork-Masterclass/issues).

---

## License

This material is provided for educational use as part of **Claude Cowork Masterclass (`C1382`)**. © Tertiary Infotech Academy Pte Ltd. All rights reserved.

---

## Developed By

**Tertiary Infotech Academy Pte Ltd** — [Tertiary Courses](https://www.tertiarycourses.com.sg/)

Course: [Claude Cowork Masterclass (C1382)](https://www.tertiarycourses.com.sg/claude-cowork-masterclass.html)

## Acknowledgements

- [Anthropic](https://www.anthropic.com/) — Claude and Claude Cowork.
- Course trainers and learners who refine the activities through practice and feedback.

---

<div align="center">

⭐ **If these materials help you delegate work with better evidence and control, star the repository.**

Powered by [Tertiary Infotech Academy Pte Ltd](https://www.tertiaryinfotech.com/)

[📘 Course Page](https://www.tertiarycourses.com.sg/claude-cowork-masterclass.html) · [📖 Learner Guide](LG-Claude%20Cowork%20Masterclass.md) · [🧪 Labs](labs/README.md)

</div>
