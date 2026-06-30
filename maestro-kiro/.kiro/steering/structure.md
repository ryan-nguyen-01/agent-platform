# Structure & conventions

How this codebase is organized and the patterns Kiro must follow so generated code fits in seamlessly.
**Scan the area before editing and keep this file current** — it is the project's living style guide.
Match what exists; never impose a different style. Fill in the sections for the stacks the project
actually uses; delete the rest.

## Backend — Java / Spring Boot

```text
- Layering:          controller → service → repository?  package-by-feature or package-by-layer?
- DTO & mapping:     MapStruct / manual; entities never leak out of the service layer
- Error handling:    @ControllerAdvice + error response shape
- Validation:        Bean Validation @Valid / custom
- Persistence:       Spring Data repositories / query style; transactions on the service layer
- Config & secrets:  application.yml profiles / env; never hard-code secrets
- Logging:           SLF4J pattern, levels
- Naming:            Controller/Service/RepositoryImpl suffixes, package names
- Tests:             where, naming, JUnit/Testcontainers patterns
```

## Backend — Node.js / TypeScript

```text
- Framework:         NestJS / Fastify / Koa / Express — match the repo
- Layering:          module/controller/service/repository (Nest) or routes/handlers/services
- Validation:        Zod / class-validator / DTOs
- ORM:               Prisma / Drizzle / TypeORM — schema location, migration command
- Error handling:    central error middleware / exception filter + response shape
- Async/config:      async/await everywhere; config via env (dotenv / Nest config); no hard-coded secrets
- Logging:           pino / winston / Nest logger
- Naming & layout:   feature folders, file naming, barrel exports?
- Tests:             Vitest / Jest + supertest; where they live
```

## Frontend — React / Next.js

```text
- App type:          React SPA (Vite) or Next.js (App Router / Pages)? RSC vs client components
- Folder layout:     feature folders / app router segments / by-type
- Components:        function components, PascalCase; one per file?; server vs client ("use client")
- Shared/common:     WHERE shared components live and how to import them — reuse, don't recreate
- Hooks:             custom hooks location + patterns (use*, single responsibility)
- State:             Redux Toolkit / Zustand / Context / server state (React Query) — the project's choice
- Data fetching:     React Query keys / Next server actions / route handlers / fetch in RSC
- Styling:           Tailwind / shadcn / MUI / styled-components — the existing approach only
- Imports/aliases:   @/ alias, import ordering
- Tests:             Vitest/RTL + Playwright e2e conventions
```

## Shared

```text
- Lint/format:       ESLint/Prettier, Checkstyle/Spotless
- Branch/commit:     convention
- Build/run:         commands to build, run, test each part (BE and FE)
- Gotchas:           anything surprising future-you should know
```
