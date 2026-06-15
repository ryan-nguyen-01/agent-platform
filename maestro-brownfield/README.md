# Maestro Brownfield

Maintain an EXISTING, running project: deep onboarding first, execute assigned tasks precisely, ask when unclear — never infer.

A self-contained Maestro workspace with a purpose-fit folder tree: `source/` for the existing
project's code (one folder per service/app/package) and `intake/` for raw material you drop in
(specs, bug reports, error logs, dumps). Copy this folder anywhere, move your project into `source/`,
drop any material into `intake/`,
then run `claude` (or `codex`) in this folder and JUST DESCRIBE what you want in plain language
("phân tích dự án này", "sửa bug X", "tình hình?") — no commands needed; the coordinator maps
intent to the right flow. Power-user shortcuts exist in COMMAND.md if you want them.

Entry points: `CLAUDE.md` (Claude) - `AGENTS.md` (Codex) - `COMMAND.md` (commands)
- `.maestro/INSTRUCTIONS.md` (workflow brain).

A self-contained workspace — edit it directly (see VARIANT.yaml). The folder tree is fit to
maintenance work: code in `source/`, raw user material in `intake/`.
