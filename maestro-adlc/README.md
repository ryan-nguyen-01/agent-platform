# Maestro ADLC

AI development lifecycle: building AI products and agents (LLM features, RAG, agentic apps) with eval-driven quality gates.

A self-contained Maestro workspace with a purpose-fit folder tree: `app/` for the product shell
(UI, APIs, services), `ai/` for the AI layer (`ai/prompts` versioned, `ai/evals` for the eval gate,
`ai/datasets` for RAG/training sources), and `tests/`. Copy this folder anywhere, put your code in
`app/` + `ai/` (register paths in `.maestro/registry/components.yaml`),
then run `claude` (or `codex`) in this folder and JUST DESCRIBE what you want in plain language
("phân tích dự án này", "sửa bug X", "tình hình?") — no commands needed; the coordinator maps
intent to the right flow. Power-user shortcuts exist in COMMAND.md if you want them.

Entry points: `CLAUDE.md` (Claude) - `AGENTS.md` (Codex) - `COMMAND.md` (commands)
- `.maestro/INSTRUCTIONS.md` (workflow brain).

A self-contained workspace — edit it directly (see VARIANT.yaml). The folder tree is fit to building
AI products: code in `app/` + `ai/`, eval suites in `ai/evals/`, product docs in `docs/`.
