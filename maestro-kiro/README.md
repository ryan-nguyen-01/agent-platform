# Maestro Kiro

A direct build companion: **you ask, Kiro does it and writes down what it did** in `WORKLOG.md`. No
task tickets, no approval gates, no QC pipeline — just **Understand → Do → Log → Report**.

A self-contained workspace. Copy this folder onto (or beside) your project, run `claude` (or `codex`),
and just say what you want ("thêm nút X", "sửa API Y", "refactor component Z"). Kiro:

- scans the area first and **matches your existing FE/BE conventions** (component & hook patterns,
  shared components, folder layout, naming, state/data-fetching; backend layering, error shape,
  validation, DB access) — recorded in `.maestro/conventions.md`,
- makes the change directly (no task-first ceremony),
- appends one entry to `WORKLOG.md` (what was asked, what it did, files, notes),
- and only stops to ask before irreversible/outward actions (delete data, deploy, `git push`, secrets).

It ships the full Maestro skill library (237 skills, FE + BE + tooling) so it rarely lacks a skill; the
deeper Maestro engine is present as an optional reference library, never a mandatory flow.

Entry points: `CLAUDE.md` (Claude) · `AGENTS.md` (Codex) · `.maestro/INSTRUCTIONS.md` (operating model)
· `WORKLOG.md` (what Kiro did) · `.maestro/conventions.md` (your project's detected conventions).

Independent template — hand-maintained, edited directly (see VARIANT.yaml).
