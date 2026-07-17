# Đóng góp

Cảm ơn bạn cải thiện Maestro Kiro. Đây là workspace nhỏ, docs-first, nên đóng góp chủ yếu vào nội dung
`.kiro/`.

## Cái gì nằm ở đâu

- `source/`, `intake/` — chỗ của USER (code dự án + tài liệu thô); repo chỉ giữ README định nghĩa
  quy tắc của từng thư mục.
- `.kiro/steering/` — contract vận hành + template kiến thức dự án. Giữ thay đổi gọn và khớp cách Kiro
  thật sự đọc steering ([docs](https://kiro.dev/docs/steering/)).
- `.kiro/skills/` — Kiro Agent Skills đúng chuẩn ([docs](https://kiro.dev/docs/skills/)): frontmatter
  chỉ gồm `name` (= tên thư mục, `a-z0-9-`, ≤64) + `description` (≤1024, giàu từ khoá) + tuỳ chọn
  `license`/`compatibility`/`metadata`; layout chỉ `SKILL.md` + `scripts/` + `references/` + `assets/`
  (+ LICENSE). CI job `kiro-skills` chặn skill lệch chuẩn. `CATALOG.md` là file **sinh tự động** —
  đừng sửa tay: mỗi skill khai `metadata.category` + `metadata.summary` (tiếng Việt) trong SKILL.md,
  rồi chạy `python3 scripts/build-skill-catalog.py` (CI check bằng `--check`).
- `.kiro/hooks/` — JSON `*.kiro.hook`, hợp lệ theo [định dạng hooks](https://kiro.dev/docs/hooks/). Hook
  mới nên **mặc định tắt**.
- `.kiro/specs/`, `.kiro/analysis/`, `.kiro/testing/`, `.kiro/team/` — template quy trình + khu làm
  việc (INDEX/board là file sống); spec `example-*` chỉ để minh hoạ.
- Steering vai/đa-service: `team.md` (vai + bàn giao), `services.md` (sổ service), `svc-_template.md`
  (hồ sơ per-service, dùng `inclusion: fileMatch`).

## Quy ước

- Tài liệu cho user (analysis, inventory, worklog, requirements/design của spec) viết **tiếng Việt**;
  code và thuật ngữ kỹ thuật giữ tiếng Anh.
- Giữ gọn — giá trị của repo là nhỏ và dễ nhận diện. Đừng thêm lại bloat framework.
- Validate trước khi mở PR: `*.kiro.hook` và `settings/mcp.json` là JSON hợp lệ; front-matter steering
  (`inclusion:`) nằm ở dòng đầu.

## PR

Commit nhỏ, tập trung, message rõ. Mô tả đổi gì và vì sao.
