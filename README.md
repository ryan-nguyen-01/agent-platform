# Maestro

**Maestro** is a coordinator-driven multi-agent delivery framework. The `maestro-*` folders below are
**ready-to-copy workspaces**: copy one anywhere, put your source code inside, run `claude` (or `codex`)
in it — the agent follows that template's workflow, gates, and identity.

## Pick a template

| Folder | Use it when you want to… | Methodology | Skills |
| --- | --- | --- | --- |
| [`maestro-sdlc/`](maestro-sdlc/) | Build software end-to-end: BA → design → UI/UX prototype → code → real-user QC | spec-driven-development | 231 |
| [`maestro-adlc/`](maestro-adlc/) | **Agent** Development Lifecycle: build agents (`agents/` + `evals/`) with a behavior **eval gate** | eval-driven-ai | 164 |
| [`maestro-enterprise/`](maestro-enterprise/) | Operate governed/production agents: compliance, audit, accountability | enterprise-agent-governance | 166 |
| [`maestro-lite/`](maestro-lite/) | Ship a small tool/prototype fast, minimal ceremony (no specialist advisors) | risk-based-routing | 39 |
| [`maestro-brownfield/`](maestro-brownfield/) | Maintain an EXISTING project (`source/` + `intake/`): deep onboarding, precise tasks, **ask-don't-infer** | risk-based-routing | 225 |

## Use it

```bash
cp -R maestro/maestro-adlc ~/work/my-agent     # copy the template anywhere
cd ~/work/my-agent                              # agents in agents/, eval suites in evals/, host app in app/
claude                                          # /coord to start · /ship for autonomous build-to-done
```

Each template is self-contained and standardized: entry points (`CLAUDE.md`, `AGENTS.md`,
`COMMAND.md`), the `.maestro/` workflow brain, a purpose-fit agent/skill set, and folders for your
code and working artifacts. Ask the agent "who are you" — it answers as that Maestro variant
operating your project.

## Platform (framework source)

[`platform/`](platform/) holds the framework source and the generator. Maintain Maestro there:

```bash
cd platform && python3 scripts/build-variant.py --all   # rebuild the generated maestro-* templates
```

`build-variant.py --all` builds the three generated templates (sdlc, enterprise, lite).
`maestro-adlc/` (`agents/` + `evals/` + `app/`) and `maestro-brownfield/` (`source/` + `intake/`) are **independent
and hand-maintained** — each has its own purpose-fit tree and is edited directly, not generated.

Template manifests and the build contract: [platform/variants/README.md](platform/variants/README.md).

## License

MIT — see [LICENSE](LICENSE).
