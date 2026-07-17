<div align="center">

# Maestro Kiro

**Bạn hỏi. Kiro làm — và tự ghi lại việc đã làm.**

Một workspace [Kiro](https://kiro.dev) tự chứa để bảo trì & phát triển dự án **full-stack** —
**Java/Spring Boot · Node.js · Next.js · ReactJS** — theo kiểu [Maestro Brownfield](../maestro-brownfield):
code của dự án nằm trong `source/`, mọi tài liệu thô nằm trong `intake/`. Việc nhỏ: *Hiểu → Làm →
Kiểm → Ghi*, không nghi thức. Việc nhiều bước: **một Kiro đóng cả team** (điều phối · phân tích ·
dev · **QC tester thực thụ**) giao tiếp bằng **file bàn giao** — trạng thái luôn nằm trên đĩa.

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
[![Made for Kiro](https://img.shields.io/badge/made%20for-Kiro-5A31F4.svg)](https://kiro.dev)
[![Stack](https://img.shields.io/badge/stack-Spring%20Boot%20%C2%B7%20Node%20%C2%B7%20Next%20%C2%B7%20React-success.svg)](.kiro/steering/tech.md)
[![Skills](https://img.shields.io/badge/skills-60-blue.svg)](.kiro/skills/CATALOG.md)
[![CI](https://img.shields.io/badge/CI-validate-brightgreen.svg)](.github/workflows/validate.yml)

</div>

---

## Vì sao

Đa số setup agent bắt bạn trông chừng một quy trình: viết ticket, phân tích, duyệt kế hoạch, bàn giao
cho coder, chạy QC. Nhiều nghi thức, chậm việc thật.

**Kiro làm ngược lại.** Bạn nói bằng ngôn ngữ tự nhiên → Kiro đọc đúng chỗ (tài liệu trong `intake/`,
code trong `source/`, sổ tái dùng `inventory.md`), khớp convention của bạn, thực hiện thay đổi, và
thêm một mục trung thực vào `WORKLOG.md`. Nó chỉ dừng để hỏi trước những việc không thể hoàn tác
(xoá, deploy, push, secret) hoặc khi yêu cầu mơ hồ thật sự.

**Nó theo dự án của bạn, không áp khuôn.** Kiro đọc cách codebase của bạn thật sự được viết — layering,
đặt tên, thư viện, luồng — và khớp theo đó. Steering và skills là kiến thức khởi đầu; convention thật
của dự án luôn thắng.

## Bắt đầu nhanh

Workspace **tự chứa** — không cần cài đặt gì:

```bash
# 1. Copy nguyên thư mục này tới đâu tuỳ bạn
cp -R maestro-kiro ~/work/my-workspace && cd ~/work/my-workspace

# 2. Đưa code dự án vào source/ (mỗi service/app một thư mục — bao nhiêu con cũng được,
#    con cũ lẫn con mới, FE lẫn BE)
mv ~/old/legacy-api source/legacy-api
mv ~/old/new-api    source/new-api
mv ~/old/my-webapp  source/my-webapp

# 3. Thả tài liệu thô vào intake/ (SRS, spec, bug report, log, screenshot…)
cp ~/docs/srs-v2.pdf intake/

# 4. Mở trong Kiro và cứ nói:
#    "quét dự án đi"        → đăng ký từng service vào services.md + hồ sơ svc-<tên>.md riêng
#    "thêm endpoint GET /users/{id} trả UserDto"  → luồng DIRECT
#    "phân tích luồng nghiệp vụ API tạo đơn hàng" → luồng ANALYZE
#    "viết test case cho màn hình đăng ký theo tài liệu trong intake" → luồng TEST
```

## Nó hoạt động thế nào

```text
Bạn hỏi
   │
   ▼
Hiểu    đọc đúng nguồn: intake/INDEX.md → tài liệu · source/ → code thật · inventory.md → cái có sẵn
        nhận diện stack/tầng (Spring · Node · React · Next · DB/UI), nạp skill phù hợp
Làm     code trực tiếp trong source/ — không ticket, không cổng; TÁI DÙNG thay vì viết lại
Kiểm    build/typecheck/test vùng đã đổi; không dead code, một code path
Ghi     thêm một mục vào WORKLOG.md (yêu cầu · đã làm · files · ghi chú)
Báo     tóm tắt ngắn + assumption
```

Năm luồng, chọn theo việc (định nghĩa đầy đủ trong [`.kiro/steering/kiro.md`](.kiro/steering/kiro.md)):

| Luồng | Khi nào | Output |
| --- | --- | --- |
| **DIRECT** | thay đổi nhỏ/rõ | code trong `source/` + WORKLOG |
| **SPEC** | feature lớn/mơ hồ | `.kiro/specs/<feature>/` (requirements EARS + bảng validation → design → tasks) |
| **ANALYZE** | "phân tích luồng X", "trace FE sang BE", chuẩn bị migration | skill `analyze-flow`: mỗi tính năng một file `.kiro/analysis/<x>.md` (`file:line`, bảng hành vi theo case, migration notes) + `dependency-map.md` liên hệ giữa tính năng |
| **TEST** | "viết test case / test đi" | `.kiro/testing/<module>/<tinh-nang>/` + INDEX.md — xem dưới |
| **INTAKE** | vừa thả tài liệu vào `intake/` | phân loại + `intake/INDEX.md`; cờ secret; code lạc chỗ thì hỏi |

## Team — một Kiro, nhiều vai, bàn giao bằng file

Với việc nhiều bước/nhiều service, Kiro chạy **task pipeline** ([`team.md`](.kiro/steering/team.md)):
vai **COORDINATOR** chuẩn hoá yêu cầu thành `.kiro/team/tasks/<id>/task.md` (kèm yêu cầu nghiệp vụ +
Definition of Done) rồi giao lần lượt cho **ANALYST → DEV → TESTER** — mỗi vai chỉ nạp **bộ skill
riêng của vai + hồ sơ service nó phụ trách**. Vai xong phần mình **bắt buộc viết file bàn giao**;
vai nhận **echo-back** (tóm tắt mình hiểu gì) và được **hỏi–đáp qua lại ngay trong file** (tối đa 3
vòng) cho tới khi đủ input — thiếu thì `blocked`, không đoán. `board.md` là bảng công việc sống:
mở phiên mới đọc nó là resume đúng chỗ. Việc nhỏ đi fast lane, không dính nghi thức này.

## QC mode — test như một tester thực thụ

Hai skill chuyên trách biến Kiro thành tester:

1. **[`qa-test-case-design`](.kiro/skills/qa-test-case-design/SKILL.md)** — đọc tài liệu THẬT
   (requirements/AC, spec trong `intake/`, code trong `source/`) rồi lập **hồ sơ validation từng
   field**: kiểu dữ liệu (chỉ số hay cả chữ), bắt buộc, độ dài min/max, ký tự cho phép, format —
   và sinh test case theo ma trận **hợp lệ / biên (min−1, max+1) / rỗng / sai kiểu / ký tự đặc biệt /
   độc hại (SQL, XSS)**, phủ đủ mọi AC, mọi endpoint (2xx/400/401/403/404/409), mọi màn hình
   (empty/loading/error/success). Constraint không có trong tài liệu → dò code thật; vẫn không có →
   hỏi bạn, không bịa.
2. **[`qa-test-execution`](.kiro/skills/qa-test-execution/SKILL.md)** — chạy từng case với bằng chứng
   thật. **Fail → lập bug report → chuyển vai dev fix tận gốc → retest.** Gặp bug **blocker** →
   **DỪNG toàn bộ case phụ thuộc**, chỉ chạy tiếp khi dev báo OK và retest case blocker **pass**.
   Done = 100% case chạy + **0 bug còn mở**. Không pass giả định, không sửa expected, không hạ mức bug.

## Có gì bên trong

```text
source/              CODE dự án của bạn — mỗi service/app/package một thư mục
intake/              tài liệu thô bạn thả vào (SRS, spec, bug report, log, dump) + INDEX.md
.kiro/
├── steering/        kiến thức Kiro nạp mỗi phiên
│   ├── kiro.md          contract vận hành: bản đồ đọc/viết, 5 luồng, kỷ luật fix bug
│   ├── team.md          TEAM: vai COORDINATOR/ANALYST/DEV/TESTER, WIP=1, bàn giao bắt buộc
│   ├── product.md       bạn đang xây gì
│   ├── services.md      SỔ ĐĂNG KÝ service trong source/ (stack, DB, cũ/mới, ai gọi ai)
│   ├── svc-<tên>.md     hồ sơ TỪNG service — tự nạp khi đụng service đó (fileMatch)
│   ├── tech.md          mặc định chung (hồ sơ service thắng)
│   ├── structure.md     convention chung (hồ sơ service thắng)
│   ├── inventory.md     đồ dùng chung LIÊN-service — để TÁI DÙNG
│   └── git.md           git chỉ khi bạn ra tín hiệu, mỗi lần
├── skills/          60 Agent Skills chuẩn Kiro (tự kích hoạt theo task) + CATALOG.md (sinh tự động)
├── specs/           spec mode cho feature lớn (requirements → design → tasks)
├── analysis/        phân tích luồng — <module>/<tinh-nang>.md + INDEX.md + dependency-map.md
├── testing/         test case + bug report — <module>/<tinh-nang>/ + INDEX.md
├── team/            điều phối & BÀN GIAO: board.md + tasks/<id>/ (task.md, handoff-*.md)
├── hooks/           automation *.kiro.hook tuỳ chọn (mặc định tắt)
└── settings/mcp.json   MCP servers (mặc định rỗng)
WORKLOG.md           bản ghi việc Kiro làm (không commit)
```

**Trí nhớ tái dùng:** Kiro giữ `inventory.md` — sổ component, hook, helper dùng chung — và tra
trước khi viết cái mới, để tái dùng thay vì tạo trùng.

**Fix bug tận gốc:** tái hiện trước → dò root cause end-to-end (`file:line`) → sửa nơi lỗi *sinh ra*
chứ không phải nơi lỗi *lộ ra* → thêm test chống tái phát → kiểm cả các chỗ gọi chung.

**Càng làm càng khôn:** mỗi lỗi thật (user sửa lưng, bug do Kiro, assumption sai, loay hoay lặp)
bắt buộc đúc kết vào [`lessons.md`](.kiro/steering/lessons.md) — file bài học **luôn được nạp mỗi
phiên** nên lỗi hôm nay thành luật ngày mai; bug đóng phải kèm luật phòng ngừa; cuối mỗi task
pipeline có mini-retro. Seed sẵn 10 nguyên tắc vận hành cốt lõi đúc kết từ các agent trưởng thành.

## Skills

60 skill chuẩn **Kiro Agent Skills** (`.kiro/skills/<tên>/SKILL.md`, frontmatter `name` +
`description`; tài liệu phụ trong `references/`, code trong `scripts/`, template trong `assets/`) —
Kiro tự kích hoạt khi description khớp task ([docs](https://kiro.dev/docs/skills/)). Trải khắp
**Java/Spring Boot**, **Node.js** (NestJS, Fastify, Koa, GraphQL), **React** (react-query, redux,
zustand, vite), **Next.js** (best practices, cache, RSC, Vercel), **UI** (shadcn, MUI, Tailwind,
animation), **Data & ORM** (Postgres, MySQL, Redis, Supabase, Neon, Prisma, Drizzle, TypeORM),
**Auth**, **QC/Testing** (`qa-test-case-design`, `qa-test-execution`, Playwright, TDD) và
**xuyên suốt** (`analyze-flow` trace luồng FE→BE phục vụ fix bug & migration, debug, đọc-hiểu code lạ, verify trước khi nói xong).
Tra theo mảng ở [`.kiro/skills/CATALOG.md`](.kiro/skills/CATALOG.md).

## License

[MIT](LICENSE).
