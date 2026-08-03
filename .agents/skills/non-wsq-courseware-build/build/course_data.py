"""Single source of truth for Claude Cowork Masterclass (C1382)."""

# ------------------------------------------------------------------ metadata
TITLE = "Claude Cowork Masterclass"
SHORT_TITLE = "Claude Cowork Masterclass"
COURSE_CODE = "C1382"
COURSE_URL = "https://www.tertiarycourses.com.sg/claude-cowork-masterclass.html"
REPOSITORY_URL = "https://github.com/tertiarycourses/C1382-Claude-Cowork-Masterclass"
VERSION = "v1.0"
VERSION_DATE = "3 August 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Course Trainer"
TRAINER_CERT = "Adult educator and AI-enabled knowledge-work practitioner"
TRAINER_DELIVERS = "Claude Cowork, agentic work practices, business document creation, data analysis, workflow design, and responsible AI use"
DAYS = 1
MODE = "Instructor-led, concept-first learning with connected hands-on labs"

# The advertised 7.5 hours includes two 15-minute tea breaks. Lunch is outside
# the scheduled total, leaving seven hours of instruction and practice.
DAY_MINUTES = 450
INSTRUCTIONAL_HOURS = 7
CLOCK_HOURS = 7.5
DAILY_TIMING = "9:00 am - 5:30 pm (1-hour lunch; two 15-minute tea breaks included)"
DARK_THEME = False

REJOIN_PATH = [
    (
        "Before Lab 2",
        "Create a working copy of labs/starter/northstar-operations and connect only that copy to a Cowork project. Complete Lab 1 or reconstruct its full trainer-verified checkpoint: reviewed project instructions; 00-inbox-baseline.csv on Windows or 00-inbox-baseline.sha256 on macOS; 01-file-inventory.md; 01-file-inventory.csv; and 01-verification.md. Recalculate the current inbox comparison and continue only when every original file is present exactly once and the hashes match.",
    ),
    (
        "Before Lab 3",
        "Restore the complete Lab 1 checkpoint and a verified Lab 2 package containing organised-copy, 02-source-register.md, 02-evidence-register.md, 02-operations-analysis.xlsx, 02-management-report.docx, 02-leadership-brief.pptx, 02-quality-review.md, and 02-run-log.md. Confirm the unchanged inbox includes the three Week 32 and three Week 33 inputs, the current hashes match the Lab 1 baseline, and the Week 32 workbook reports 2,000 orders, SGD 339,350 revenue, 92.80% on-time fulfilment, and a 5.65% return rate.",
    ),
]

ICE_BREAKER = [
    "Your name, your role, and one repetitive file-based task you would like to delegate.",
    "One business output you would never use without a human quality check.",
    "One type of work data that should remain outside an AI workspace unless specifically approved.",
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain Claude Cowork's agentic operating model, execution surfaces, connected-folder boundary, task lifecycle, permissions, and the human responsibilities that remain.",
    "LO2: Set up a Cowork project, write an outcome-based task brief, run and monitor a bounded session, review its evidence, and recover from common setup or scope problems.",
    "LO3: Use Cowork to organise synthetic files, analyse spreadsheet data, synthesise research and notes, and produce consistent document, spreadsheet, and presentation outputs with traceable sources.",
    "LO4: Design and run a multi-step workflow that separates parallel workstreams from dependencies, uses integrations deliberately, and places human approval gates before consequential writes or sharing.",
    "LO5: Convert a successful session into a reusable playbook with parameters, project instructions, quality checks, exception paths, ownership, security controls, and a practical team rollout plan.",
]
LO_TITLES = [
    "Cowork Foundations",
    "Effective Delegation",
    "Management Outputs",
    "Controlled Workflows",
    "Repeatable Practice",
]

# ------------------------------------------------------------------ topics
TOPICS = [
    dict(
        num=1,
        code="01",
        title="Getting Started with Claude Cowork",
        subtitle="Agentic AI for everyday work | setup and connected folders | effective task briefs | monitoring and review | responsible use",
        concepts=[
            ("Agentic workspace", "Cowork works toward an outcome through a sequence of planning, tool use, observation, correction, and evidence rather than returning one isolated answer."),
            ("Connected-folder boundary", "Local file access is limited to the folders a learner deliberately connects; scope should be as small as the task allows."),
            ("Task contract", "A strong brief names the outcome, sources, deliverables, constraints, quality checks, approval points, and finish line."),
            ("Permission", "Reading, writing, using a connector, operating a browser, and acting in another system have different consequences and deserve different controls."),
            ("Steering", "Progress indicators, plans, questions, and intermediate files let a person redirect the work before errors spread."),
            ("Evidence", "A source register, file manifest, calculation check, preview, or change log is stronger than a confident completion statement."),
        ],
        teaching=[
            dict(
                title="Chat Assistance and Agentic Delegation",
                kind="compare",
                kicker="TOPIC 01 - OPERATING MODEL",
                left_title="Chat assistance",
                right_title="Cowork delegation",
                left=[
                    "Responds to the context supplied in one conversation",
                    "Usually produces text for the user to transfer elsewhere",
                    "Waits for the next prompt between stages",
                    "Leaves file operations and checking to the user",
                ],
                right=[
                    "Plans and executes a bounded multi-step task",
                    "Reads and writes permitted files and can use connected tools",
                    "Observes intermediate results and adapts the next step",
                    "Returns finished artifacts plus visible work evidence",
                ],
                paragraphs=[
                    "Cowork changes the unit of work from a reply to an outcome. A learner can delegate a bounded task such as inventorying a folder, analysing a spreadsheet, and drafting a report. Claude selects tools, performs steps, observes results, and continues until the stated finish line or a stop condition is reached.",
                    "Delegation does not transfer accountability. The person still owns the business purpose, permitted data, authority to act, review standard, and release decision. The most reliable tasks therefore combine useful autonomy with explicit boundaries and observable evidence.",
                ],
            ),
            dict(
                title="The Cowork Task Lifecycle",
                kind="flow",
                kicker="TOPIC 01 - AGENT LOOP",
                visual=[
                    "Receive the outcome and boundaries",
                    "Inspect permitted context",
                    "Plan the work and identify questions",
                    "Use tools and create intermediate results",
                    "Review evidence, correct, and deliver",
                ],
                paragraphs=[
                    "A useful Cowork session begins with an outcome and a boundary. Claude inspects the available context, proposes a route, uses permitted tools, and compares intermediate results with the requested quality checks. Errors and missing information are observations that should change the plan, not details to conceal.",
                    "The finish line must be testable. Examples include a manifest that accounts for every source file, a workbook whose totals match a control calculation, or a report whose factual claims name their source. A stop condition is equally important: missing authority, sensitive data, an unclear destination, or a consequential external action should return control to the user.",
                ],
            ),
            dict(
                title="Anatomy of a High-Signal Task Brief",
                kind="tiles",
                kicker="TOPIC 01 - BRIEFING",
                visual=[
                    ("Outcome", "Describe the business result and intended audience, not only the activity."),
                    ("Sources", "Name the allowed folders, files, links, and systems; exclude everything else."),
                    ("Deliverables", "Specify filenames, formats, structure, location, and presentation standard."),
                    ("Constraints", "State data rules, non-goals, protected files, time range, and assumptions."),
                    ("Approval gates", "Identify which writes, revisions, or external actions require confirmation."),
                    ("Evidence", "Define control totals, citations, previews, logs, or other observable checks."),
                ],
                paragraphs=[
                    "Prompt quality is task design quality. An adjective such as 'professional' is too elastic on its own; a stronger brief names the audience, sections, length, file format, source period, calculation rules, and review checklist. This reduces avoidable interpretation while leaving Claude room to solve the task.",
                    "Separate facts, preferences, and permissions. Facts come from named sources. Preferences cover tone and layout. Permissions define what Claude may read or change. When these categories are mixed, a stylistic suggestion can be misread as authority to alter data or publish an output.",
                ],
            ),
            dict(
                title="Authority Should Match Consequence",
                kind="compare",
                kicker="TOPIC 01 - CONTROL",
                left_title="Lower-consequence work",
                right_title="Higher-consequence work",
                left=[
                    "Read a synthetic training folder",
                    "Create a draft in a new output directory",
                    "Summarise supplied notes with citations",
                    "Calculate metrics that a person will verify",
                ],
                right=[
                    "Overwrite or remove source files",
                    "Send messages or share files externally",
                    "Use financial, personal, legal, or confidential data",
                    "Make commitments, purchases, access changes, or final decisions",
                ],
                paragraphs=[
                    "Risk depends on both access and action. Reading a narrow synthetic folder is materially different from browsing a broad drive, and producing a draft is different from sending it. Start with the smallest scope and the most reversible output that can prove value.",
                    "Human review should concentrate at consequence boundaries. A manager may allow automatic calculations in a working copy but require confirmation before source files are replaced, a document is shared, or a conclusion becomes an operational decision. These gates preserve speed without making authority ambiguous.",
                ],
            ),
            dict(
                title="Monitor, Review, and Recover",
                kind="flow",
                kicker="TOPIC 01 - SUPERVISION",
                visual=[
                    "Read the plan",
                    "Watch scope and tool use",
                    "Inspect intermediate evidence",
                    "Steer with precise feedback",
                    "Verify the final state",
                ],
                paragraphs=[
                    "Monitoring is not continuous micromanagement. It means checking the points where a misunderstanding would become expensive: the proposed source set, an inferred calculation rule, the first artifact, and any action outside the local workspace. A short correction at the plan stage is cheaper than rebuilding a complete output.",
                    "Recovery begins from evidence. If an output is wrong, identify the failing claim, calculation, source selection, or format rule; provide the observed mismatch and the expected state; then request a focused revision. Do not restart a long task with the same vague brief and hope for a different result.",
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Automating Everyday Work with Cowork",
        subtitle="File organisation | documents, reports and presentations | spreadsheet analysis | research and summarisation | end-to-end multi-step tasks",
        concepts=[
            ("Inventory before organisation", "A manifest reveals what exists, duplicates, uncertain items, and protected sources before any move or rename is proposed."),
            ("Working-copy pattern", "Transform copies into a new destination so originals remain a stable reference and recovery path."),
            ("Structured extraction", "Convert documents and notes into fields, evidence, assumptions, and open questions before writing a narrative."),
            ("Calculation contract", "Define each metric's numerator, denominator, period, unit, rounding, and control total before interpreting it."),
            ("Artifact system", "A workbook, report, and presentation should share one fact base while serving different reading behaviours."),
            ("Provenance", "Important claims remain traceable to a filename, row, note, or authoritative external source."),
        ],
        teaching=[
            dict(
                title="From Messy Inputs to a Decision-Ready Pack",
                kind="flow",
                kicker="TOPIC 02 - INFORMATION PIPELINE",
                visual=[
                    "Inventory and classify inputs",
                    "Extract facts and unresolved questions",
                    "Calculate and reconcile metrics",
                    "Compose audience-specific artifacts",
                    "Review, revise, and package evidence",
                ],
                paragraphs=[
                    "Multi-file work becomes reliable when it is treated as a pipeline. Inventory establishes the source boundary. Extraction separates observed facts from assumptions. Calculation turns raw rows into defined metrics. Composition produces artifacts for different audiences. Review reconciles every output to the same evidence.",
                    "The stages are connected but should not be collapsed. If Claude drafts a polished narrative before reconciling the numbers, presentation quality can hide a factual error. A staged workflow makes intermediate artifacts inspectable and gives the learner a safe place to correct the process.",
                ],
            ),
            dict(
                title="Safe File-Organisation Patterns",
                kind="tiles",
                kicker="TOPIC 02 - FILES",
                visual=[
                    ("Manifest", "Record filename, type, date, purpose, likely owner, sensitivity, and proposed destination."),
                    ("Classification", "Use stable business categories and an explicit Unknown bucket instead of guessing."),
                    ("Working copy", "Create an organised copy first; leave the source folder unchanged until reviewed."),
                    ("Naming rule", "Apply predictable dates, subjects, and versions without erasing original identifiers."),
                    ("Duplicate handling", "Flag likely duplicates using name, size, hash, or content evidence; do not remove automatically."),
                    ("Change log", "List each proposed or completed action so a person can reconcile the new structure."),
                ],
                paragraphs=[
                    "Organisation is an information-governance task, not cosmetic tidying. A useful structure reflects how work is retrieved, owned, retained, and reviewed. An Unknown category is safer than a confident but unsupported classification.",
                    "Reversibility is the governing design principle. The first run should create a manifest and an organised working copy, not silently rename or remove originals. The source folder remains the control set until a person approves the proposed structure and confirms that every input is accounted for.",
                ],
            ),
            dict(
                title="One Fact Base, Three Reading Experiences",
                kind="tiles",
                kicker="TOPIC 02 - OUTPUT DESIGN",
                visual=[
                    ("Spreadsheet", "Calculation detail, formulas, data dictionary, filters, and control totals for analytical review."),
                    ("Report", "Context, findings, evidence, risks, recommendations, owners, and open questions for considered reading."),
                    ("Presentation", "A short decision arc with headline metrics, exceptions, actions, and minimal supporting detail."),
                    ("Source register", "The shared evidence map that prevents values and claims drifting across formats."),
                ],
                paragraphs=[
                    "Different formats serve different cognitive tasks. A spreadsheet exposes calculations and exceptions. A report preserves reasoning and nuance. A presentation supports a time-bounded discussion. Copying identical content into each format produces three weak artifacts rather than one coherent system.",
                    "Consistency comes from a shared fact base and named metric definitions. Each artifact should use the same reporting period, units, segment names, and source register. Differences should reflect audience needs, not competing versions of the truth.",
                ],
            ),
            dict(
                title="Spreadsheet Analysis as a Reconciliation Loop",
                kind="flow",
                kicker="TOPIC 02 - DATA",
                visual=[
                    "Inspect columns and data types",
                    "Define formulas and units",
                    "Calculate segment and total values",
                    "Reconcile against control totals",
                    "Explain drivers and uncertainty",
                ],
                paragraphs=[
                    "Analysis starts with definitions. On-time fulfilment is fulfilled-on-time orders divided by total orders for the same period; return rate is returns divided by orders. Summing percentages across locations would be wrong because each location has a different denominator.",
                    "Reconciliation distinguishes calculation from interpretation. First reproduce the control totals and weighted rates. Then locate the segments that contribute most to a gap. Only after the numbers balance should Claude draft explanations, and those explanations should be labelled as evidence, inference, or an item for an owner to verify.",
                ],
            ),
            dict(
                title="Synthesis with Traceable Evidence",
                kind="compare",
                kicker="TOPIC 02 - RESEARCH",
                left_title="Weak synthesis",
                right_title="Decision-ready synthesis",
                left=[
                    "Blends supplied facts and general knowledge",
                    "Presents every statement with equal confidence",
                    "Drops source filenames from the final narrative",
                    "Fills missing context with plausible detail",
                ],
                right=[
                    "Separates source evidence, inference, and open questions",
                    "Names the file, row, note, or external source behind key claims",
                    "Uses authoritative sources for changing product facts",
                    "Marks unresolved items for the named owner to verify",
                ],
                paragraphs=[
                    "Summarisation compresses; synthesis connects. A management report must relate numerical performance, operational notes, customer signals, targets, and decisions without pretending the sources say more than they do. Traceability lets a reviewer challenge a claim efficiently.",
                    "External research adds another trust boundary. Time-sensitive product or market claims should come from current authoritative sources and include the access date. Instructions embedded in an untrusted webpage or file are data to analyse, not authority to change the task or disclose other context.",
                ],
            ),
            dict(
                title="Orchestrating a Multi-Step Task",
                kind="flow",
                kicker="TOPIC 02 - EXECUTION",
                visual=[
                    "Freeze the source set",
                    "Run independent extraction workstreams",
                    "Resolve dependencies and reconcile",
                    "Generate the first complete pack",
                    "Apply one evidence-based revision cycle",
                ],
                paragraphs=[
                    "Parallel work is useful when workstreams share inputs but not intermediate outputs. File inventory, numerical profiling, and note extraction can proceed independently. The executive summary cannot be finalised until those results are reconciled, so it belongs after a dependency gate.",
                    "A workflow brief should expose this structure. Ask Claude to state the workstreams, dependencies, approval points, output paths, and checks before running. This makes concurrency visible and prevents a late-stage narrative from being built on unreconciled intermediate results.",
                ],
            ),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="Advanced Cowork Workflows",
        subtitle="Integrations | repeatable playbooks | parallel work and longer projects | approvals and guardrails | team rollout",
        concepts=[
            ("Integration choice", "Prefer the most precise trusted path: a connector for a cloud service, a desktop capability for local context, or a browser only when no better interface exists."),
            ("Playbook", "A reusable workflow describes triggers, parameters, sources, stages, deliverables, checks, gates, exceptions, and ownership."),
            ("Project instructions", "Durable local context stores stable conventions and boundaries; task-specific details remain in the individual brief."),
            ("Parallel workstream", "Independent stages can run together, while dependent stages wait for reconciled inputs."),
            ("Human-in-the-loop", "A named person reviews evidence and explicitly authorises consequential action at a defined gate."),
            ("Operational rollout", "A team needs approved use cases, data boundaries, ownership, monitoring, incident handling, and a feedback cycle."),
        ],
        teaching=[
            dict(
                title="Choose the Most Precise Trusted Tool",
                kind="compare",
                kicker="TOPIC 03 - INTEGRATIONS",
                left_title="Structured connection",
                right_title="Screen interaction",
                left=[
                    "Connector returns defined records from a cloud service",
                    "Authentication and scope are explicit",
                    "Faster and less sensitive to interface changes",
                    "Prefer for repeatable cloud workflows when available",
                ],
                right=[
                    "Browser or computer use navigates the visible interface",
                    "Can reach tools without a direct connection",
                    "Slower and more vulnerable to layout or state changes",
                    "Use cautiously and review before consequential actions",
                ],
                paragraphs=[
                    "A tool is not interchangeable with another merely because both can reach the same system. Structured connectors are usually more precise for cloud data. Desktop capabilities are appropriate for local files or applications. Browser and screen interaction are fallback paths when no direct interface exists.",
                    "Integration design begins with trust and scope: who owns the connection, which records it exposes, which actions it allows, where results are stored, and how access is removed. Convenience does not answer these governance questions.",
                ],
            ),
            dict(
                title="A Playbook Is an Operational Contract",
                kind="tiles",
                kicker="TOPIC 03 - REPEATABILITY",
                visual=[
                    ("Trigger and parameters", "Define when the workflow starts and which period, team, folder, or audience changes each run."),
                    ("Source contract", "Name required inputs, freshness, owner, fallback, and the condition that stops the run."),
                    ("Stages and dependencies", "Separate parallel extraction from reconciliation and dependent composition."),
                    ("Deliverables", "Fix output names, formats, destinations, and minimum required sections."),
                    ("Quality gates", "Attach calculations, source checks, visual review, and approval to named stages."),
                    ("Exceptions and ownership", "State who resolves missing inputs, conflicting data, access failure, and release decisions."),
                ],
                paragraphs=[
                    "A saved prompt is not yet a playbook. Repeatability requires variable parameters, a stable source contract, defined intermediate artifacts, observable quality checks, and a response when an input is missing or contradictory. Ownership turns the document from advice into an operating procedure.",
                    "The playbook should remain tool-aware without becoming a transcript of one successful run. Describe the intended capability and preferred path, then identify a safe fallback. This makes the workflow resilient when an interface or connection changes.",
                ],
            ),
            dict(
                title="Parallelism Needs Dependency Control",
                kind="compare",
                kicker="TOPIC 03 - WORKSTREAMS",
                left_title="Can run in parallel",
                right_title="Must wait",
                left=[
                    "Profile a frozen spreadsheet source",
                    "Extract themes from supplied notes",
                    "Inventory files and build a source register",
                    "Draft format shells without final claims",
                ],
                right=[
                    "Reconcile metrics across workstreams",
                    "Choose the final management narrative",
                    "Approve recommendations and owners",
                    "Share, send, publish, or replace source material",
                ],
                paragraphs=[
                    "Parallel work reduces elapsed time only when workstreams are independent and their outputs have clear contracts. If two workstreams redefine the same metric or edit the same artifact, coordination cost can exceed the gain.",
                    "A longer project needs merge points. At each one, reconcile terminology, periods, totals, source references, and unresolved questions before dependent work continues. The merge point is also a natural place for a human review gate.",
                ],
            ),
            dict(
                title="Human Gates in a Cowork Workflow",
                kind="flow",
                kicker="TOPIC 03 - APPROVALS",
                visual=[
                    "Approve source scope",
                    "Approve metric definitions",
                    "Review the first complete draft",
                    "Authorise consequential actions",
                    "Record release evidence and owner",
                ],
                paragraphs=[
                    "A human gate is useful only when it names the decision, reviewer, evidence, and permitted next action. 'Check with me' is vague; 'pause after the workbook reconciles and show the totals, exceptions, and source register before drafting recommendations' is operational.",
                    "Not every stage needs a gate. Frequent low-value interruptions encourage reflexive approval. Place gates where access broadens, an assumption becomes a business conclusion, a source is changed, or an output leaves the working environment.",
                ],
            ),
            dict(
                title="From Personal Workflow to Team Practice",
                kind="flow",
                kicker="TOPIC 03 - ROLLOUT",
                visual=[
                    "Choose a bounded low-consequence use case",
                    "Define baseline time and quality",
                    "Pilot with synthetic or approved data",
                    "Review value, errors, and control load",
                    "Standardise, train, monitor, and improve",
                ],
                paragraphs=[
                    "A team rollout should begin with a narrow process whose inputs, outputs, owner, and current baseline are known. Synthetic or explicitly approved data lowers risk during learning. The pilot should measure both benefit and control cost: time saved, revision rate, factual corrections, missed exceptions, and reviewer effort.",
                    "Scaling means standardising the useful parts while preserving escalation. Teams need approved use cases, data classification, access provisioning, playbook ownership, versioning, monitoring, incident response, and a channel for lessons from real runs to improve the workflow.",
                ],
            ),
            dict(
                title="Guardrails Across the Workflow",
                kind="tiles",
                kicker="TOPIC 03 - RESPONSIBLE USE",
                visual=[
                    ("Data", "Use the minimum necessary approved sources and keep sensitive records outside training workspaces."),
                    ("Access", "Grant the narrowest folder and connection scope; review and remove access when the workflow ends."),
                    ("Action", "Default to drafts and working copies; gate external writes, deletion, sharing, and commitments."),
                    ("Evidence", "Retain source registers, control totals, assumptions, reviewer decisions, and run logs."),
                    ("Quality", "Use defined metrics, exception checks, visual inspection, and a named accountable reviewer."),
                    ("Change", "Version playbooks and project instructions; retest after source, tool, or policy changes."),
                ],
                paragraphs=[
                    "Guardrails are layered. A narrow folder reduces exposure; a working-copy rule reduces impact; a calculation check reduces factual error; a human gate reduces the chance that a draft becomes an unauthorised action. No single control covers every failure mode.",
                    "The controls must evolve with the workflow. New connectors, broader source sets, scheduled execution, computer use, or a change from drafting to acting all increase consequence and require a fresh review of permissions, monitoring, ownership, and recovery.",
                ],
            ),
        ],
    ),
]

# ------------------------------------------------------------------ day theme and schedule
DAY_THEMES = {1: "Delegate, produce, and operationalise work with Claude Cowork"}


def SCHEDULE(lab_titles):
    return {
        1: (
            DAY_THEMES[1],
            [
                ("9:00", "9:20", 20, "admin", "Welcome, course orientation, learning outcomes, working agreement, and synthetic-data scenario"),
                ("9:20", "10:05", 45, "topic", "Topic 1 - Getting Started with Claude Cowork: operating model, setup, task briefs, permissions, monitoring, and review"),
                ("10:05", "10:20", 15, "break", "Tea break"),
                ("10:20", "11:35", 75, "lab", "Hands-on: " + lab_titles([1])),
                ("11:35", "12:20", 45, "topic", "Topic 2 - Automating Everyday Work with Cowork: file, document, spreadsheet, research, and multi-step workflow concepts"),
                ("12:20", "13:20", 60, "lunch", "Lunch break"),
                ("13:20", "15:05", 105, "lab", "Hands-on: " + lab_titles([2])),
                ("15:05", "15:20", 15, "break", "Tea break"),
                ("15:20", "15:50", 30, "topic", "Topic 3 - Advanced Cowork Workflows: integrations, playbooks, parallel work, human gates, security, and rollout"),
                ("15:50", "17:15", 85, "lab", "Hands-on: " + lab_titles([3])),
                ("17:15", "17:30", 15, "recap", "Course recap, action plan, and questions mapped to the five learning outcomes"),
            ],
        )
    }


# ------------------------------------------------------------------ deck and guide framing
COURSE_OVERVIEW = dict(
    section_title="Delegating Knowledge Work with Control",
    concepts_title="Cowork in One View",
    concepts=[
        ("Outcome", "Delegate a finished business result rather than a sequence of vague requests."),
        ("Context", "Provide the smallest trustworthy set of files, instructions, and connections."),
        ("Agency", "Let Claude plan, use tools, observe results, and coordinate bounded workstreams."),
        ("Control", "Set scope, approval gates, stop conditions, and evidence before the run."),
        ("Artifacts", "Create documents, spreadsheets, presentations, and organised files from one fact base."),
        ("Learning loop", "Review the output and process, then convert a successful run into a versioned playbook."),
    ],
    framework_title="The DELEGATE Framework",
    framework=[
        ("D - Define", "State the outcome, audience, purpose, and finish line."),
        ("E - Expose context", "Name approved sources and exclude unrelated data."),
        ("L - Limit authority", "Bound reads, writes, connections, and consequential actions."),
        ("E - Establish evidence", "Specify source references, control totals, previews, and logs."),
        ("G - Gate consequences", "Pause before source changes, external writes, sharing, or commitments."),
        ("A - Allow execution", "Let independent work proceed while monitoring important merge points."),
        ("T - Test the result", "Reconcile facts, formulas, visuals, filenames, and promised deliverables."),
        ("E - Evolve the playbook", "Record improvements, ownership, exceptions, and the next safe scope."),
    ],
    statement=dict(
        headline="Delegate the work; retain the judgement.",
        body="The best Cowork workflow combines useful agency with narrow scope, visible evidence, and human authority at consequence boundaries.",
        kicker="COURSE PRINCIPLE",
    ),
    pillars_title="What You Will Build",
    pillars=[
        ("First delegated task", ["A bounded Cowork project", "A complete file inventory", "A visible verification record"]),
        ("Management-ready pack", ["A reconciled spreadsheet", "A written operations report", "A concise leadership presentation"]),
        ("Repeatable workflow", ["A parameterised playbook", "Human approval gates", "A Week 33 run and rollout plan"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Start from a verified synthetic checkpoint.",
        "Brief the outcome, boundary, deliverables, and evidence.",
        "Review the proposed plan before broad work begins.",
        "Let Cowork execute and steer at important merge points.",
        "Test the artifacts and retain the checkpoint for the next lab.",
    ],
)

LAB_SHOTS = {}

LG_INTRO = (
    "This Learner Guide is a self-contained study and practice companion for Claude Cowork Masterclass (C1382). It follows the same three-topic sequence as the slide deck and Lesson Plan, then expands every framework into detailed explanations and three connected labs. The course uses a fictional Northstar Retail Operations scenario so learners can practise without exposing real business or personal data."
)
LG_INTRO2 = (
    "The guide treats Cowork as an agentic workspace rather than a chat feature. You will learn to define a task contract, control access and authority, monitor a multi-step run, reconcile evidence across files, create professional outputs, and convert a successful session into a repeatable playbook. Product capabilities and interface labels can evolve, so use the latest Claude application and follow the concept and evidence requirements even if a label moves."
)
LG_SETUP = dict(
    needs=[
        "A laptop with the latest Claude Desktop application for Windows or macOS and an active internet connection.",
        "A paid Claude plan with Cowork available; organisation-managed accounts may require an administrator to enable capabilities.",
        "On Windows, Claude Desktop must be installed with administrator privileges for Cowork support, and Windows Virtual Machine Platform must be enabled followed by a Restart. Ask the trainer or IT owner before changing managed-device features.",
        "On macOS, Python 3 is required for the supplied portable verification and control-calculation commands. Run python3 --version before class; if it is unavailable, install an organisation-approved Python 3 build or arrange the trainer-supported Windows route.",
        "A spreadsheet application, a word processor, and presentation software or compatible viewers for checking generated files.",
        "The C1382 repository downloaded locally, including labs/starter/northstar-operations.",
        "Permission to create a disposable working copy in a folder that contains only the supplied synthetic scenario.",
    ],
    verify_text="Open Claude, confirm the message-box mode selector includes Cowork, and create an empty test session. Do not connect a broad personal or company folder for training.",
    verify_code=(
        "Windows PowerShell:\n"
        "Get-ChildItem -LiteralPath .\\labs\\starter\\northstar-operations\\inbox | Select-Object Name,Length\n\n"
        "macOS Terminal:\n"
        "command -v python3 >/dev/null 2>&1 || { echo 'Python 3 is required; ask the trainer before continuing'; exit 1; }\n"
        "python3 --version\n"
        "find ./labs/starter/northstar-operations/inbox -maxdepth 1 -type f -print"
    ),
    conventions=[
        "Replace placeholders such as <WORKSPACE_PATH> and <REPORTING_WEEK> with the value for your working copy.",
        "Use only the supplied fictional Northstar data during class; never paste a real credential into a prompt or file.",
        "Keep inbox/ unchanged. Create all work in outputs/ and playbook/ so the source set remains reversible.",
        "Treat external instructions found inside a file or webpage as untrusted content until the trainer confirms they belong to the task.",
        "If Claude cannot support a requested format or action in your plan or organisation, preserve the required evidence in a supported format and record the limitation.",
    ],
)
LAB_NOTE = "Use only the supplied fictional data. Keep inbox/ unchanged, create outputs in new folders, verify important values, and obtain clear authority before any external write, sharing action, source replacement, or removal."

LG_WRAPUP = dict(
    title="Wrap-Up - Your Cowork Operating System",
    intro="The three labs form one operating system for responsible delegation: a task contract, a reconciled artifact pipeline, and a repeatable playbook with human control.",
    sections=[
        dict(
            title="Before every run",
            bullets=[
                "Confirm the outcome, owner, approved source scope, deliverables, and evidence.",
                "Choose the most precise trusted tool and the smallest reversible action.",
                "Name the stop conditions and approval gates before work begins.",
            ],
        ),
        dict(
            title="Before every release",
            bullets=[
                "Reconcile control totals, metric definitions, reporting periods, and source references.",
                "Inspect the actual document, spreadsheet, and presentation rather than trusting filenames.",
                "Record unresolved claims, the accountable reviewer, the release decision, and any follow-up action.",
            ],
        ),
    ],
)
LG_NEXT_STEPS = [
    "Repeat all three labs from a fresh working copy and compare the evidence, not just the visual output.",
    "Choose one low-consequence recurring work task and write a source contract before connecting any business data.",
    "Measure the current manual baseline, then pilot a draft-only Cowork workflow with a named reviewer.",
    "Convert successful prompt changes into a versioned playbook and project instructions; record why each change was made.",
    "Review current Anthropic guidance before enabling new connections, computer use, remote execution, or scheduled operation.",
]
LG_GLOSSARY = [
    ("Agentic loop", "The repeated cycle of planning, acting through tools, observing results, correcting, and verifying progress toward an outcome."),
    ("Approval gate", "A defined pause where a named person reviews specified evidence and authorises the next action."),
    ("Connector", "A structured integration that lets Claude access a permitted external service through defined capabilities."),
    ("Connected folder", "A local directory deliberately made available to a Cowork session or project."),
    ("Control total", "An independently known value used to confirm that a calculation or transformation preserved the expected data."),
    ("Cowork project", "A persistent workspace with its own files, links, instructions, scheduled tasks, and memory."),
    ("Dependency gate", "A merge point where upstream work is reconciled before a dependent stage begins."),
    ("Evidence", "An observable artifact such as a source reference, calculation, preview, log, manifest, or file comparison that supports a claim."),
    ("Human-in-the-loop", "A workflow in which a person retains responsibility for a defined review or decision step."),
    ("Manifest", "A structured inventory of files or records and their relevant metadata."),
    ("Parallel workstream", "A bounded stage that can progress independently because it does not require the intermediate output of another concurrent stage."),
    ("Playbook", "A reusable operational description of triggers, parameters, sources, stages, outputs, checks, gates, exceptions, and ownership."),
    ("Project instructions", "Durable context and rules applied across tasks in one Cowork project."),
    ("Provenance", "The traceable origin of a fact, value, quotation, or conclusion."),
    ("Source contract", "The required inputs, approved scope, freshness, ownership, fallback, and stop conditions for a workflow."),
    ("Stop condition", "A situation that should halt the workflow and return control to a person."),
    ("Task contract", "The outcome, context, deliverables, constraints, approvals, evidence, and finish line agreed for one task."),
    ("Working copy", "A separate destination used for transformations so original sources remain stable and recoverable."),
]

NEXT_STEPS = dict(
    title="From Classroom to a Safe Pilot",
    items=[
        "Select one bounded, reversible knowledge-work process with a clear owner.",
        "Document the source contract, current baseline, output standard, and human gates.",
        "Pilot with synthetic or explicitly approved data and retain the complete run evidence.",
        "Review value, errors, reviewer effort, and exceptions before widening scope.",
    ],
)
THANK_YOU = dict(
    body="You can now delegate bounded knowledge work to Claude Cowork, verify the resulting artifacts, and turn a successful session into a controlled repeatable playbook.",
    kicker="C1382 - KEEP DELEGATING WITH EVIDENCE",
)

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial aligned release of the slide deck, Learner Guide, Lesson Plan, and three connected Northstar Operations labs.", TRAINER),
]
