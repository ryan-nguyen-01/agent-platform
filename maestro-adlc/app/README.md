# app/

The host application — the deployable shell that serves and exposes the agents: API, UI, runtime,
integrations. Organize the internal layout as the project needs (frontend, backend, workers); register
each component in `.maestro/registry/components.yaml`.

This is the application code that hosts the agents. The agents themselves — mission, tools, prompts,
memory, knowledge — live in `agents/`, and their behavior eval suites live in `evals/`.
