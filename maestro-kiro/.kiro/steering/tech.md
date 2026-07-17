# Tech stack

**File này là MẶC ĐỊNH CHUNG toàn workspace.** `source/` có nhiều service — stack THẬT của từng
service ghi trong hồ sơ `svc-<tên>.md` (thắng file này khi làm trong service đó).

**File này GHI LẠI stack thật của dự án — không quy định stack.** Bộ skills bên dưới phủ một mảng
full-stack (Java/Spring Boot hoặc Node.js; React hoặc Next.js; thư viện UI/ORM/auth) để Kiro sẵn sàng
cho bất cứ thứ gì dự án dùng — nhưng **lựa chọn thật của dự án luôn thắng**. Hãy dò từ repo (file build,
deps, code có sẵn), theo đúng đó, và giữ file này khớp. Dự án dùng thứ không có trong đây → cứ theo dự
án và bổ sung. Thay mỗi `…` bằng lựa chọn thật; xoá phần không dùng.

## Backend

### Java / Spring Boot

- Java …, build Maven / Gradle; Spring Boot … (Web, Validation, Security, Data JPA tuỳ dùng)
- Lưu trữ: Postgres / MySQL qua Spring Data JPA / Hibernate; migration Flyway / Liquibase
- REST DTO, lỗi qua `@ControllerAdvice`, Bean Validation; test JUnit 5 + Spring Boot Test
- Skills: `java-spring-development`, `spring-boot-engineer`, `spring-framework`, `java-architect`, `api-design-principles`

### Node.js / TypeScript

- Node … + TypeScript; framework NestJS / Fastify / Koa / Express
- API kiểu REST và/hoặc GraphQL; realtime qua WebSocket khi cần
- Skills: `nodejs-backend-patterns`, `nestjs-clean-typescript`, `fastify-typescript`, `koa-typescript`, `graphql`, `websocket-development`, `api-design-principles`

## Frontend

### React (SPA / Vite)

- React … + TypeScript, build Vite; state Redux Toolkit / Zustand / Context; data React Query
- Skills: `react`, `react-query`, `react-modernization`, `redux-toolkit`, `zustand-state-management`, `vite`, `typescript-advanced-types`

### Next.js (App Router / RSC)

- Next.js …, App Router, Server Components, server actions; deploy Vercel
- Skills: `next-best-practices`, `next-cache-components`, `native-data-fetching`, `vercel-react-best-practices`, `vercel-composition-patterns`, `deploy-to-vercel`

## Thư viện UI & styling

- Component shadcn/ui / MUI — tái dùng primitive, đừng tự chế. Styling Tailwind / styled-components / SCSS.
- Skills: `shadcn`, `mui`, `tailwindcss`, `tailwind-design-system`, `tailwind-knowledge-patch`, `styled-components-best-practices`, `scss-best-practices`, `postcss-best-practices`, `framer-motion`, `gsap`, `accessibility-a11y`, `web-design-guidelines`

## Data, ORM & auth

- SQL: Postgres / MySQL / Neon / Supabase; cache: Redis / Upstash
- ORM (Node): Prisma / Drizzle / TypeORM; (Java): Spring Data JPA
- Auth: Better Auth / Spring Security / Supabase Auth
- Skills: `postgresql-best-practices`, `mysql-best-practices`, `neon-postgres`, `supabase`, `supabase-postgres-best-practices`, `redis-best-practices`, `redis-js`, `upstash-redis-kv`, `prisma`, `prisma-development`, `prisma-knowledge-patch`, `drizzle-orm`, `drizzle-knowledge-patch`, `typeorm`, `better-auth-best-practices`

## Testing

- Unit/integration theo stack (JUnit / Vitest / Jest), e2e Playwright.
- Skills: `test-driven-development`, `webapp-testing`, `playwright-best-practices`, `verification-before-completion`

> Tra skill theo mảng ở [`.kiro/skills/CATALOG.md`](../skills/CATALOG.md). Nạp skill trước khi viết code
> trong mảng đó; dùng `legacy-code-comprehension` để đọc code lạ trước.
