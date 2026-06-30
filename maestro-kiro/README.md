<div align="center">

# Maestro Kiro

**You ask. Kiro does it — and writes down what it did.**

A lean, [Kiro](https://kiro.dev)-native workspace for shipping **full-stack web** features fast —
**Java/Spring Boot · Node.js · Next.js · ReactJS** — no task tickets, no approval pipeline. Just
*Understand → Do → Log*.

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
[![Made for Kiro](https://img.shields.io/badge/made%20for-Kiro-5A31F4.svg)](https://kiro.dev)
[![Stack](https://img.shields.io/badge/stack-Spring%20Boot%20%C2%B7%20Node%20%C2%B7%20Next%20%C2%B7%20React-success.svg)](.kiro/steering/tech.md)
[![Skills](https://img.shields.io/badge/skills-57-blue.svg)](.kiro/skills/CATALOG.md)

</div>

---

## Why

Most agent setups make you babysit a process: write a ticket, get it analyzed, approve a plan, hand off
to a coder, run QC. Great for ceremony, slow for real work.

**Kiro flips it.** Ask in plain language → Kiro reads the relevant code, matches your conventions, makes
the change, and appends one honest entry to `WORKLOG.md`. It only stops to ask before something it
can't undo (delete, deploy, push, secrets). That's it.

It's tuned for a focused full-stack lane so it's actually good at it: **Spring Boot or Node.js
backends, React or Next.js frontends, the UI libraries, ORMs, and auth you already use** — 57 curated
skills, zero bloat.

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
Understand   detect the stack/layer (Spring · Node · React · Next · DB/UI),
             match conventions in .kiro/steering/structure.md, load the right skill
Do           implement directly — no ticket, no gate, no hand-off; reuse what exists
Verify       build/typecheck/test the changed area; no dead code, one code path
Log          append one entry to WORKLOG.md (asked · did · files · notes)
Report       quick summary + any assumption
```

For a **large or fuzzy feature**, Kiro switches to **spec mode** (`requirements → design → tasks`,
see below). Small, clear changes stay on the direct flow above.

Kiro confirms first only for irreversible / outward actions: deleting data, deploying, `git push`,
writing secrets, or a real two-way-door decision.

## What's inside

```text
.kiro/
├── steering/        project knowledge Kiro loads every session
│   ├── kiro.md          the operating contract (Ask → Do → Log)
│   ├── product.md       what you're building
│   ├── tech.md          stack: Spring Boot · Node.js · Next.js · React + UI/ORM/auth libs
│   └── structure.md     your conventions (BE layering, FE hooks/shared components/style)
├── skills/          57 curated how-to skills + CATALOG.md (pick by domain)
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

57 skills across **Backend — Java/Spring Boot** (`java-spring-development`, `spring-boot-engineer`, …),
**Backend — Node.js** (`nodejs-backend-patterns`, `nestjs-clean-typescript`, `fastify-typescript`,
`graphql`, …), **Frontend — React** (`react`, `react-query`, `redux-toolkit`, `zustand`, …),
**Frontend — Next.js** (`next-best-practices`, `next-cache-components`, `native-data-fetching`,
`deploy-to-vercel`, …), **UI libraries** (shadcn, MUI, Tailwind, styled-components, framer-motion, …),
**Data & ORM** (Postgres, MySQL, Redis, Supabase, Neon, Prisma, Drizzle, TypeORM), **Auth**
(`better-auth-best-practices`), and **cross-cutting** (debugging, testing, code comprehension). Browse
[`.kiro/skills/CATALOG.md`](.kiro/skills/CATALOG.md).

## Using it with Claude Code (optional)

This repo is built for **Kiro IDE**, which reads `.kiro/steering/` automatically. To use the same
contract in **Claude Code**, add a one-line `CLAUDE.md`:

```text
@.kiro/steering/kiro.md
```

## License

[MIT](LICENSE).
