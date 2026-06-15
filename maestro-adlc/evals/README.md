# evals/

The EVAL GATE — how agent behavior is proven before DONE. Agents are non-deterministic, so quality
claims need eval evidence, not demos (eval-driven-ai methodology, R-019-10). A failing suite blocks
DONE for that agent/capability.

```text
evals/
  <agent-or-capability>/
    dataset/         task scenarios + golden trajectories + real failure cases
    graders/         code graders and/or LLM-judge (with a calibration plan)
    thresholds.yaml  pass-rate thresholds + non-determinism policy (pin model/params, or n>=3 rates)
  datasets/          shared eval datasets reused across suites
```

What agent suites measure beyond single-turn correctness:

- **Task success** — did the agent achieve the goal end-to-end?
- **Trajectory** — did it take a valid path (no needless steps, no loops past the cap)?
- **Tool-call correctness** — right tool, right arguments, handled tool errors, no forbidden tools.
- **Safety** — prompt injection / exfiltration resistance; destructive tools still require human confirm (R-011-07).
- **Cost/latency** — within the per-agent budget recorded in the blueprint.

Design suites with `agent-eval-suite.template.yaml` / `agent-behavior-eval.template.yaml`
(eval-engineer advises; qc-runner executes via `/evals`). Run results are recorded under
`.maestro/observability/evals/<run-id>/` — never summarized from memory (R-024-04). Failures become
permanent regression cases; shrinking datasets or raising thresholds to pass is fabrication (R-019-QC4).
