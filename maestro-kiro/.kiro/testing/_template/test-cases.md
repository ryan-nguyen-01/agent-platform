# Test cases — <tên-feature>

- **Phạm vi:** <feature/API/màn hình được test; những gì cố tình ngoài phạm vi>
- **Tài liệu nguồn:** <requirements/spec/analysis/code đã dùng, kèm đường dẫn — vd
  `.kiro/specs/<feature>/requirements.md`, `intake/<file>`, `source/<path>`>
- **Môi trường:** <cách chạy: lệnh build/start, base URL, dữ liệu test>
- **Trạng thái:** designing | approved | running | done

## Hồ sơ validation field

| Field | Kiểu | Bắt buộc? | Min/Max | Ký tự/định dạng cho phép | Ràng buộc khác | Nguồn |
| --- | --- | --- | --- | --- | --- | --- |
| `<field>` | <chuỗi/số/ngày/enum> | <có/không> | <3–30 ký tự / 0–999> | <a-z0-9, không dấu / email / dd-MM-yyyy> | <unique, phụ thuộc field khác> | <requirements §x / file:line> |

## Tổng hợp

| Nhóm | Số case | Pass | Fail | Blocked | Pending |
| --- | --- | --- | --- | --- | --- |
| P1 — smoke/case chặn | | | | | |
| P2 — chức năng chính | | | | | |
| P3 — phụ/edge | | | | | |

Case chặn (fail sẽ block nhóm phía sau): `TC-<feature>-001 …` — chặn các case `<danh sách/nhóm>`.

## Test cases

### TC-<feature>-001 — <tiêu đề ngắn> `[P1]`

- **Liên kết:** <Req/AC id · endpoint · màn hình>
- **Precondition:** <trạng thái/dữ liệu cần có trước>
- **Các bước:**
  1. <bước, cụ thể tới mức chạy lại được>
  2. <bước>
- **Test data:** <giá trị cụ thể — vd `username = "ab"` (min−1)>
- **Expected:** <kết quả cụ thể — vd HTTP 400, mã lỗi `USERNAME_TOO_SHORT`, message "..."; UI hiện lỗi dưới field>
- **Status:** pending | pass | fail (BUG-xxx) | blocked (BUG-xxx)
- **Bằng chứng:** <output/status code/mô tả UI thật khi chạy>

### TC-<feature>-002 — <tiêu đề> `[P2]`

- …

> Quy ước status: cập nhật ngay sau khi chạy từng case; không sửa expected cho khớp kết quả sai;
> case bỏ qua phải có lý do được user duyệt.
