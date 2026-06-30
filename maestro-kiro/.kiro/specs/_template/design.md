# Design — <feature-name>

> Grounded in the real codebase and `.kiro/steering/` (tech.md, structure.md). Reference existing
> code/utilities to reuse — don't reinvent.

## Overview

<the approach in a paragraph: what we build and the shape of the solution>

## Architecture

<how the pieces fit; a small diagram or bullet flow. BE layers + FE components touched.>

## Backend (Spring Boot)

- **Endpoints / contracts:** <method + path + request/response DTOs>
- **Domain / entities:** <entities, relationships, new fields>
- **Persistence:** <repositories, queries, migration>
- **Validation & errors:** <rules + error responses, matching the project's shape>

## Frontend (React)

- **Components:** <new/changed components, where they live, shared ones reused>
- **State & data:** <store/hook/query changes>
- **UI:** <library primitives + styling approach>

## Data model / schema changes

<tables/columns/DTOs; migration plan>

## Trade-offs & alternatives

- <decision> — chosen because <reason>; alternative <X> rejected because <reason>

## Testing strategy

- <unit/integration/e2e to add; what proves each requirement>

## Risks

- <risk> → <mitigation>
