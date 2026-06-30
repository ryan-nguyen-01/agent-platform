# Tech stack

This Kiro workspace is tuned for **full-stack web**: backends in **Java/Spring Boot** *or* **Node.js**
(NestJS / Fastify / Koa), frontends in **ReactJS** and **Next.js**, with a full set of UI libraries,
ORMs, auth, and data tools. Kiro prefers the project's ACTUAL stack over these defaults — confirm
against the real code and keep this file current.

Most projects use one backend and one frontend flavor. Detect which from the repo (build files, deps)
and follow that; the others are listed so Kiro is ready for whatever the project picks. Replace each
`…` with the project's real choice.

## Backend

### Java / Spring Boot

- Java …, build Maven / Gradle; Spring Boot … (Web, Validation, Security, Data JPA as used)
- Persistence: Postgres / MySQL via Spring Data JPA / Hibernate; migrations Flyway / Liquibase
- REST DTOs, `@ControllerAdvice` errors, Bean Validation; tests JUnit 5 + Spring Boot Test
- Skills: `java-spring-development`, `spring-boot-engineer`, `spring-framework`, `java-architect`, `api-design-principles`

### Node.js / TypeScript

- Node … + TypeScript; framework NestJS / Fastify / Koa / Express
- API style REST and/or GraphQL; realtime via WebSocket when needed
- Skills: `nodejs-backend-patterns`, `nestjs-clean-typescript`, `fastify-typescript`, `koa-typescript`, `graphql`, `websocket-development`, `api-design-principles`

## Frontend

### React (SPA / Vite)

- React … + TypeScript, Vite build; state Redux Toolkit / Zustand / Context; data React Query
- Skills: `react`, `react-query`, `react-modernization`, `redux-toolkit`, `zustand-state-management`, `vite`, `typescript-advanced-types`

### Next.js (App Router / RSC)

- Next.js …, App Router, Server Components, server actions; deploy Vercel
- Skills: `next-best-practices`, `next-cache-components`, `native-data-fetching`, `vercel-react-best-practices`, `vercel-composition-patterns`, `deploy-to-vercel`

## UI libraries & styling

- Components shadcn/ui / MUI — reuse primitives, don't hand-roll. Styling Tailwind / styled-components / SCSS.
- Skills: `shadcn`, `mui`, `tailwindcss`, `tailwind-design-system`, `tailwind-knowledge-patch`, `styled-components-best-practices`, `scss-best-practices`, `postcss-best-practices`, `framer-motion`, `gsap`, `accessibility-a11y`, `web-design-guidelines`

## Data, ORM & auth

- SQL: Postgres / MySQL / Neon / Supabase; cache: Redis / Upstash
- ORM (Node): Prisma / Drizzle / TypeORM; (Java): Spring Data JPA
- Auth: Better Auth / Spring Security / Supabase Auth
- Skills: `postgresql-best-practices`, `mysql-best-practices`, `neon-postgres`, `supabase`, `supabase-postgres-best-practices`, `redis-best-practices`, `redis-js`, `upstash-redis-kv`, `prisma`, `prisma-development`, `prisma-knowledge-patch`, `drizzle-orm`, `drizzle-knowledge-patch`, `typeorm`, `better-auth-best-practices`

## Testing

- Unit/integration per stack (JUnit / Vitest / Jest), e2e Playwright.
- Skills: `test-driven-development`, `webapp-testing`, `playwright-best-practices`, `verification-before-completion`

> Pick skills by domain from [`.kiro/skills/CATALOG.md`](../skills/CATALOG.md). Load a skill before
> writing code in its area; use `legacy-code-comprehension` to read unfamiliar code first.
