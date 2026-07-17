---
inclusion: manual
---
<!-- TEMPLATE hồ sơ service — khi tạo cho service thật:
     1. Copy thành .kiro/steering/svc-<tên>.md
     2. Đổi frontmatter thành:
          inclusion: fileMatch
          fileMatchPattern: "source/<folder-service>/**"
        → Kiro CHỈ nạp hồ sơ này khi đụng file của service đó (tiết kiệm context, đúng "agent riêng
          cho từng service"). Nếu Kiro không nạp được fileMatch, tạm đổi inclusion: always.
     3. Điền từ CODE THẬT, mỗi mục kèm đường dẫn thật. Đăng ký service vào services.md. -->

# Hồ sơ service: <tên> (`source/<folder>/`)

> Trạng thái: active / legacy / new / migrating→<đích> · Loại: BE / FE / worker
> Vai trò một câu: <service này chịu trách nhiệm nghiệp vụ gì>

## Kiến trúc & bố cục

- **Stack:** <ngôn ngữ, framework + version thật từ file build/deps>
- **Kiểu kiến trúc:** <layered / hexagonal / MVC / feature-folder… — như code thật>
- **Bố cục thư mục:** <các folder chính và vai trò — vd `src/modules/<feature>/{controller,service,repo}`>
- **Entry points:** <main/bootstrap, route registration, cron/consumer> — `đường dẫn`

## Skills cho service này (bộ đồ nghề của vai DEV khi vào đây)

> Chọn từ `.kiro/skills/CATALOG.md` theo stack THẬT của service — DEV vào service này chỉ nạp đúng
> các skill dưới (+ skill xuyên suốt theo vai, xem `team.md`). Stack đổi thì cập nhật danh sách.

| Skill | Vì sao cần cho service này |
| --- | --- |
| <vd `java-spring-development`> | <vd BE Spring Boot 3> |
| <vd `postgresql-best-practices`> | <vd DB chính là Postgres> |

## Convention riêng của service này (THẮNG mọi mặc định chung)

- **Đặt tên:** <file, class, biến — như code thật>
- **Validation:** <cơ chế + ở tầng nào>
- **Xử lý lỗi:** <handler tập trung ở đâu, shape lỗi trả ra>
- **Logging:** <lib, format, mức>
- **Điểm KHÁC với các service khác:** <ghi rõ để không trộn pattern>

## Dữ liệu

- **DB:** <loại, tên db/schema, connection config ở đâu>
- **Schema/migrations:** <đường dẫn, tool (Flyway/Prisma/…), lệnh chạy migration>
- **Bảng chính:** <bảng → nghiệp vụ>
- **Bảng DÙNG CHUNG với service khác:** <bảng nào, service nào — cực kỳ quan trọng khi sửa/chuyển đổi>
- **Cache/queue:** <Redis/Kafka… — key/topic chính>

## Giao tiếp

- **API expose:** <prefix/route chính, chuẩn response, versioning, docs nếu có>
- **Gọi ra:** <service/API ngoài nào, sync/async, timeout/retry ở đâu>
- **Event:** <phát topic nào, nghe topic nào — schema ở đâu>
- **Auth:** <cơ chế, middleware/guard ở đâu>

## Build / Run / Test (lệnh THẬT chạy được)

```bash
# build:      <lệnh>
# run dev:    <lệnh + port>
# test:       <lệnh; cách chạy 1 file test>
# lint:       <lệnh>
```

- **Env/config:** <file nào, biến bắt buộc (KHÔNG ghi giá trị secret), config theo môi trường>

## Inventory tái dùng (riêng service này)

| Thành phần | Đường dẫn | Dùng để làm gì |
| --- | --- | --- |
| <component/hook/helper/base class> | `source/<folder>/...` | <mô tả> |

> Tra bảng này TRƯỚC khi viết mới trong service này; đồ dùng chung LIÊN-service nằm ở `inventory.md`.

## Gotchas (thứ sẽ cắn nếu không biết)

- <hành vi ngầm, config dễ quên, thứ tự khởi động, dữ liệu cũ, bug đã biết chưa fix…>

## Ghi chú chuyển đổi (nếu legacy / migrating)

- <nghiệp vụ nào đã chuyển sang con mới, nghiệp vụ nào còn ở đây — nguồn sự thật hiện tại là ai>
- <những gì con mới PHẢI giữ nguyên (contract, hành vi ngầm) — link file analysis liên quan>
