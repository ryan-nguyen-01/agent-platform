# Tech stack

This Kiro workspace is tuned for **Java/Spring Boot backends + ReactJS frontends + UI libraries**.
Kiro prefers the project's actual stack over these defaults — confirm against the real code and update
this file when you learn the specifics.

## Backend — Java / Spring Boot

- **Language/runtime:** Java <version> (build: Maven / Gradle — confirm)
- **Framework:** Spring Boot <version> (Web, Validation, Security, Data JPA as used)
- **Persistence:** <Postgres / MySQL> via Spring Data JPA / Hibernate; migrations: <Flyway / Liquibase>
- **Caching/queues:** <Redis / none>
- **API style:** REST (DTOs, `@ControllerAdvice` error handling, Bean Validation) — confirm shape
- **Testing:** JUnit 5 + Spring Boot Test (+ Testcontainers if present)

Skills: `java-spring-development`, `spring-boot-engineer`, `spring-framework`, `java-architect`,
`api-design-principles`, `postgresql-best-practices`, `redis-best-practices`.

## Frontend — ReactJS

- **Framework:** React <version> (Vite build — confirm), TypeScript
- **State:** <Redux Toolkit / Zustand / Context> — match what the repo uses
- **Data fetching:** <React Query / fetch / axios>
- **Routing:** <React Router / ...>
- **Testing:** <Vitest/Jest + Testing Library> + Playwright for e2e

Skills: `react`, `react-query`, `react-modernization`, `redux-toolkit`, `zustand-state-management`,
`vite`, `typescript-advanced-types`.

## UI libraries

- **Component lib:** <shadcn/ui / MUI> — reuse its primitives, don't hand-roll
- **Styling:** <Tailwind / styled-components / SCSS> — follow the existing approach
- **Motion:** <Framer Motion / GSAP> when needed; accessibility per WCAG

Skills: `shadcn`, `mui`, `tailwindcss`, `tailwind-design-system`, `tailwind-knowledge-patch`,
`styled-components-best-practices`, `scss-best-practices`, `postcss-best-practices`, `framer-motion`,
`gsap`, `accessibility-a11y`, `web-design-guidelines`.

> Pick skills by domain from [`.kiro/skills/CATALOG.md`](../skills/CATALOG.md). Load a skill before
> writing code in its area; use `legacy-code-comprehension` to read unfamiliar code first.
