# Maestro ADLC

Agent Development Lifecycle: building agentic products — agents with a mission, tools, memory, and a
planning loop — with a behavior eval gate before done.

A self-contained Maestro workspace with an agent-native folder tree: `agents/` for the agents you
build (one folder per agent: `agent.md` mission, `tools.yaml` contracts, `prompts/` versioned,
`memory.yaml`, `knowledge/`), `evals/` for behavior eval suites (the eval gate: task success,
trajectory, tool-call, safety), `app/` for the host application that serves the agents, and `tests/`.
Copy this folder anywhere, put your agents in `agents/` and the host app in `app/` (register paths in
`.maestro/registry/components.yaml`),
then run `claude` (or `codex`) in this folder and JUST DESCRIBE what you want in plain language
("xây cho tôi agent ...", "thêm tool cho agent X", "tình hình?") — no commands needed; the coordinator
maps intent to the right flow. Power-user shortcuts exist in COMMAND.md if you want them.

Entry points: `CLAUDE.md` (Claude) - `AGENTS.md` (Codex) - `COMMAND.md` (commands)
- `.maestro/INSTRUCTIONS.md` (workflow brain).

A self-contained workspace — edit it directly (see VARIANT.yaml). The folder tree is fit to developing
agents: agent definitions in `agents/`, behavior eval suites in `evals/`, host app in `app/`, product
docs in `docs/`.
