# app/

The product shell — the deployable AI product: UI, APIs, and services. Organize the internal layout
as the project needs (frontend, backend, workers); register each component in
`.maestro/registry/components.yaml`.

This is the application code. The AI layer that makes this an AI product — versioned prompts, eval
suites, and datasets — lives separately under `ai/`.
