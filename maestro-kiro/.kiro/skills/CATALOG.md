<!-- FILE SINH TỰ ĐỘNG từ frontmatter của skills — ĐỪNG SỬA TAY.
     Đổi metadata.category / metadata.summary trong SKILL.md rồi chạy:
     python3 scripts/build-skill-catalog.py -->

# Danh mục skills

60 skill how-to đã tuyển cho web full-stack: **Java/Spring Boot · Node.js · Next.js · ReactJS · thư
viện UI · database · QC/testing**. Mỗi skill là một thư mục có `SKILL.md` theo đúng format Agent
Skills của Kiro (frontmatter `name` + `description`; tài liệu phụ trong `references/`, code chạy được
trong `scripts/`, template trong `assets/`). Nạp skill liên quan trước khi viết code trong mảng đó;
bắt đầu bằng `legacy-code-comprehension` để đọc code lạ.

## Backend — Java / Spring Boot

| Skill | Dùng cho |
| --- | --- |
| `api-design-principles` | Thiết kế API REST/GraphQL (resource, versioning, lỗi) |
| `java-architect` | Kiến trúc & thiết kế Java enterprise (WebFlux, JPA, Security) |
| `java-spring-development` | Phát triển app Spring Boot end-to-end |
| `spring-boot-engineer` | Pattern service Spring Boot, starter, config |
| `spring-framework` | Spring lõi (DI, AOP, web, data) |

## Backend — Node.js

| Skill | Dùng cho |
| --- | --- |
| `fastify-typescript` | API hiệu năng cao với Fastify + TypeScript |
| `graphql` | GraphQL schema, resolver, tối ưu query |
| `koa-typescript` | API Koa.js middleware onion + TypeScript |
| `nestjs-clean-typescript` | NestJS + TypeScript sạch (module, DI, validation) |
| `nodejs-backend-patterns` | Pattern backend Node.js (layering, error, config) |
| `websocket-development` | Realtime WebSocket (thiết kế, reconnect, scale) |

## Frontend — ReactJS

| Skill | Dùng cho |
| --- | --- |
| `react` | Component, pattern, hiệu năng React |
| `react-modernization` | Hiện đại hoá/refactor code React cũ |
| `react-query` | Server-state với TanStack Query |
| `redux-toolkit` | Quản lý state Redux Toolkit |
| `typescript-advanced-types` | Kiểu TypeScript nâng cao cho code app |
| `vite` | Cấu hình build/dev Vite |
| `zustand-state-management` | Store Zustand |

## Frontend — Next.js

| Skill | Dùng cho |
| --- | --- |
| `deploy-to-vercel` | Deploy app Next.js/web lên Vercel |
| `native-data-fetching` | Data fetching phía server / pattern RSC |
| `next-best-practices` | Pattern & best practice App Router Next.js |
| `next-cache-components` | Caching & React Server Components trong Next.js |
| `vercel-composition-patterns` | Composition pattern cho React/Next |
| `vercel-react-best-practices` | Best practice hiệu năng React/Next của Vercel |

## Thư viện UI & styling

| Skill | Dùng cho |
| --- | --- |
| `accessibility-a11y` | Accessibility theo WCAG |
| `framer-motion` | Animation (Framer Motion) |
| `gsap` | Animation (GSAP) |
| `mui` | Component Material UI v7 (sx, theme) |
| `postcss-best-practices` | PostCSS |
| `scss-best-practices` | SCSS/Sass |
| `shadcn` | Component shadcn/ui |
| `styled-components-best-practices` | styled-components |
| `tailwind-design-system` | Design system trên Tailwind |
| `tailwind-knowledge-patch` | Thay đổi Tailwind gần đây |
| `tailwindcss` | Tailwind CSS |
| `web-design-guidelines` | Hướng dẫn thiết kế UI/UX |

## Data & ORM

| Skill | Dùng cho |
| --- | --- |
| `drizzle-knowledge-patch` | Thay đổi Drizzle gần đây |
| `drizzle-orm` | Drizzle ORM |
| `mysql-best-practices` | Schema & query MySQL |
| `neon-postgres` | Postgres serverless Neon |
| `postgresql-best-practices` | Schema, index, query PostgreSQL |
| `prisma` | Prisma ORM |
| `prisma-development` | Làm việc với Prisma |
| `prisma-knowledge-patch` | Thay đổi Prisma gần đây (v7) |
| `redis-best-practices` | Cache / cấu trúc dữ liệu Redis |
| `redis-js` | Redis từ Node.js |
| `supabase` | Supabase (DB, auth, storage) |
| `supabase-postgres-best-practices` | Pattern Postgres trên Supabase |
| `typeorm` | TypeORM |
| `upstash-redis-kv` | Redis/KV serverless Upstash |

## Auth

| Skill | Dùng cho |
| --- | --- |
| `better-auth-best-practices` | Auth (email/OAuth/plugin) với Better Auth |

## QC / Testing (luồng TEST — như tester thực thụ)

| Skill | Dùng cho |
| --- | --- |
| `playwright-best-practices` | Test e2e Playwright |
| `qa-test-case-design` | Thiết kế test case đầy đủ TỪ TÀI LIỆU: hồ sơ validation từng field (kiểu, min/max, ký tự cho phép), ma trận biên/rỗng/sai kiểu/độc hại, phủ mọi AC/endpoint/màn hình |
| `qa-test-execution` | Chạy test như tester thật: fail → bug → dev fix → retest; blocker → dừng case phụ thuộc, đợi fix OK mới chạy tiếp; done = 100% case + 0 bug mở |
| `test-driven-development` | Quy trình TDD khi viết code mới |
| `webapp-testing` | Chiến lược test web app |

## Xuyên suốt

| Skill | Dùng cho |
| --- | --- |
| `analyze-flow` | Trace luồng end-to-end FE→BE→DB→external theo từng tính năng + bản đồ phụ thuộc giữa tính năng — phục vụ fix bug & migration (monolith → microservices) |
| `legacy-code-comprehension` | Đọc & hiểu codebase lạ (quét trước khi sửa) |
| `systematic-debugging` | Debug có phương pháp — dò root cause khi fix bug |
| `verification-before-completion` | Xác minh thay đổi thật sự xong trước khi nói xong |
