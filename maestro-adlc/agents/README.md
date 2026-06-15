# agents/

The agents you build — one folder per agent. This is the heart of the Agent Development Lifecycle:
each agent is a first-class product with a mission, tools, memory, prompts, and a behavior contract.

```text
agents/
  <agent-name>/
    agent.md         mission, role, goals, non-goals, owner, autonomy level
    tools.yaml       tool contracts: each tool's typed inputs/outputs, side effects, auth, limits
    prompts/         versioned prompts (system / task / few-shot) — prompts are code
    memory.yaml      memory scope & bounds (what it remembers, retention, redaction)
    knowledge/       RAG / grounding sources this agent uses at runtime (synthetic or licensed, R-013)
    README.md
```

Author each agent from the engine templates (`.maestro/engine/templates/`):

- `agent-mission.template.md`           → `agent.md` mission/goals/non-goals/termination
- `agent-definition.template.md`        → persona, skills, tools, knowledge, memory bounds, model routing
- `agent-behavior-contract.template.md` → typed I/O, refusal, escalation, forbidden tools, tone, SLA
- `agent-autonomy-policy.template.md`   → reactive / proactive / autonomous boundaries + loop caps
- `agent-eval-suite.template.yaml` / `agent-behavior-eval.template.yaml` → the behavior eval gate (see `evals/`)

Register each agent in `.maestro/registry/components.yaml`. The host application that serves/exposes
the agent (API, UI, runtime) lives in `app/`; behavior eval suites live in `evals/`.
