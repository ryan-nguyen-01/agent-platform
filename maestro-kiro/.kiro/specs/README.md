# Specs (optional)

Spec mode is the **opt-in** path for a large or fuzzy feature. The default is Understand → Do → Log
(see `.kiro/steering/kiro.md`) — only reach for a spec when the change is too big to one-shot or the
user explicitly asks ("xây spec cho …", "let's spec this out").

A spec is one folder per feature with three files, written and approved in order:

```text
.kiro/specs/<feature-name>/
  requirements.md   WHAT & WHY — user stories + EARS acceptance criteria
  design.md         HOW — architecture, data model, APIs, components, trade-offs
  tasks.md          STEPS — an ordered, checkable implementation plan
```

## Workflow

1. **Requirements** — write `requirements.md` from `_template/`. Get the user's OK before designing.
2. **Design** — write `design.md` (grounded in the real codebase + `.kiro/steering/`). Get the user's OK.
3. **Tasks** — break design into small, ordered, verifiable tasks in `tasks.md`.
4. **Build** — work the tasks top to bottom, checking each `[ ] → [x]` as you finish it, and log
   completed tasks to `WORKLOG.md` like any other work. Confirm before irreversible/outward actions.

Keep specs in sync with reality: if the design changes mid-build, update `design.md`/`tasks.md` rather
than letting them drift. A finished feature's spec is the record of how it was built.

Start from the templates in [`_template/`](_template/).
