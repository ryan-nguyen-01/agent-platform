# Cấu trúc & convention

> Code nằm trong `source/`, NHIỀU service (xem `services.md`). File này chỉ ghi convention CHUNG;
> convention riêng từng service nằm trong `svc-<tên>.md` và THẮNG file này khi làm trong service đó.

**File này GHI LẠI convention thật của DỰ ÁN — đi dò, không quy định.** Quét codebase, ghi lại cách NÓ
đang được tổ chức, và theo đúng đó. Style hiện có của dự án luôn thắng placeholder bên dưới, thắng
pattern gợi ý của skills, và thắng "best practice" chung chung — code không khớp codebase thì ở đây là
sai. Giữ file này khớp code như một style guide sống. Điền phần cho stack dự án thật dùng; xoá phần còn lại.

Các gạch đầu dòng dưới là gợi ý *cần tìm & ghi lại gì* — không phải cấu trúc để áp đặt.

## Backend — Java / Spring Boot

```text
- Layering:          controller → service → repository?  package-by-feature hay package-by-layer?
- DTO & mapping:     MapStruct / thủ công; entity không lọt ra ngoài tầng service
- Xử lý lỗi:         @ControllerAdvice + shape response lỗi
- Validation:        Bean Validation @Valid / custom
- Lưu trữ:           Spring Data repository / kiểu query; transaction ở tầng service
- Config & secret:   application.yml theo profile / env; không hard-code secret
- Logging:           pattern SLF4J, mức log
- Đặt tên:           hậu tố Controller/Service/RepositoryImpl, tên package
- Test:              ở đâu, cách đặt tên, JUnit/Testcontainers
```

## Backend — Node.js / TypeScript

```text
- Framework:         NestJS / Fastify / Koa / Express — theo repo
- Layering:          module/controller/service/repository (Nest) hay routes/handlers/services
- Validation:        Zod / class-validator / DTO
- ORM:               Prisma / Drizzle / TypeORM — vị trí schema, lệnh migration
- Xử lý lỗi:         error middleware / exception filter tập trung + shape response
- Async/config:      async/await xuyên suốt; config qua env (dotenv / Nest config); không hard-code secret
- Logging:           pino / winston / Nest logger
- Đặt tên & bố cục:  feature folder, cách đặt tên file, có barrel export?
- Test:              Vitest / Jest + supertest; nằm ở đâu
```

## Frontend — React / Next.js

```text
- Loại app:          React SPA (Vite) hay Next.js (App Router / Pages)? RSC vs client component
- Bố cục thư mục:    feature folder / app router segment / theo loại
- Component:         function component, PascalCase; một file một component?; server vs client ("use client")
- Dùng chung:        component dùng chung NẰM ĐÂU và import thế nào — tái dùng, đừng tạo lại
- Hook:              vị trí & pattern custom hook (use*, một trách nhiệm)
- State:             Redux Toolkit / Zustand / Context / server state (React Query) — theo dự án
- Data fetching:     React Query keys / Next server actions / route handlers / fetch trong RSC
- Styling:           Tailwind / shadcn / MUI / styled-components — chỉ theo cách đang dùng
- Import/alias:      alias @/, thứ tự import
- Test:              Vitest/RTL + Playwright e2e
```

## Chung

```text
- Lint/format:       ESLint/Prettier, Checkstyle/Spotless
- Branch/commit:     convention
- Build/run:         lệnh build, run, test cho từng phần (BE và FE)
- Gotchas:           điều bất ngờ mà "bạn tương lai" cần biết
```
