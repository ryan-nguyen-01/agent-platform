<div align="center">

# Maestro Kiro

**You ask. Kiro does it — and writes down what it did.**

A lean, [Kiro](https://kiro.dev)-native workspace for shipping **Java/Spring Boot + ReactJS** features
fast — no task tickets, no approval pipeline. Just *Understand → Do → Log*.

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
[![Made for Kiro](https://img.shields.io/badge/made%20for-Kiro-5A31F4.svg)](https://kiro.dev)
[![Stack](https://img.shields.io/badge/stack-Spring%20Boot%20%2B%20React-success.svg)](.kiro/steering/tech.md)

</div>

---

## Why

Most agent setups make you babysit a process: write a ticket, get it analyzed, approve a plan, hand off
to a coder, run QC. Great for ceremony, slow for real work.

**Kiro flips it.** Ask in plain language → Kiro reads the relevant code, matches your conventions, makes
the change, and appends one honest entry to `WORKLOG.md`. It only stops to ask before something it
can't undo (delete, deploy, push, secrets). That's it.

It's tuned for one stack so it's actually good at it: **Spring Boot backends, React frontends, and the
UI libraries you already use** — 32 curated skills, zero bloat.

## Quickstart

```bash
# 1. Drop .kiro/ (and WORKLOG.md) into your project — or start here and add your code.
cp -R maestro-kiro/.kiro  your-project/
cp    maestro-kiro/WORKLOG.md  your-project/

# 2. Open the project in Kiro (kiro.dev). Steering loads automatically from .kiro/steering/.

# 3. Just talk:
#    "add a GET /users/{id} endpoint returning UserDto"
#    "build a Settings page with the shared <Card> and our form hook"
```

First run, tell Kiro about your project: fill `.kiro/steering/product.md` and let it scan to complete
`tech.md` / `structure.md` (or run the **refresh-steering** hook). After that it knows your stack and
conventions and stops rescanning.

## How it works

```text
You ask
   │
   ▼
Understand   read just enough; match conventions in .kiro/steering/structure.md
Do           implement directly — no ticket, no gate, no hand-off
Log          append one entry to WORKLOG.md (asked · did · files · notes)
Report       quick summary + any assumption
```

Kiro confirms first only for irreversible / outward actions: deleting data, deploying, `git push`,
writing secrets, or a real two-way-door decision.

## What's inside

```text
.kiro/
├── steering/        project knowledge Kiro loads every session
│   ├── kiro.md          the operating contract (Ask → Do → Log)
│   ├── product.md       what you're building
│   ├── tech.md          stack: Spring Boot + React + UI libs
│   └── structure.md     your conventions (BE layering, FE hooks/shared components/style)
├── skills/          32 curated how-to skills + CATALOG.md (pick by domain)
├── specs/           OPTIONAL spec mode for big features (requirements → design → tasks)
├── hooks.yaml       agent hooks (auto-worklog, convention self-checks)
└── settings.json    permissions + Kiro config
WORKLOG.md           the running record of what Kiro did
```

## Spec mode (optional)

For a large or fuzzy feature, ask Kiro to "spec it out" and it switches to the Kiro spec workflow —
`requirements.md → design.md → tasks.md` under `.kiro/specs/<feature>/`, approved in order, then built
task by task. Everyday changes skip this and go straight to Understand → Do → Log. See
[`.kiro/specs/README.md`](.kiro/specs/README.md).

## Skills

32 skills across **Backend (Java/Spring Boot)**, **Data (Postgres/Redis)**, **Frontend (React)**,
**UI libraries (shadcn, MUI, Tailwind, styled-components, …)**, and **cross-cutting** (debugging,
testing, code comprehension). Browse [`.kiro/skills/CATALOG.md`](.kiro/skills/CATALOG.md).

## Using it with Claude Code (optional)

This repo is built for **Kiro IDE**, which reads `.kiro/steering/` automatically. To use the same
contract in **Claude Code**, add a one-line `CLAUDE.md`:

```text
@.kiro/steering/kiro.md
```

## License

[MIT](LICENSE).
