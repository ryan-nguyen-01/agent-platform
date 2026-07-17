---
name: qa-test-case-design
description: Thiết kế bộ test case ĐẦY ĐỦ từ tài liệu thật (requirements/spec/AC, API contract, thiết kế màn hình) như một QC chuyên nghiệp — ma trận validation từng field (kiểu dữ liệu, bắt buộc, độ dài min/max, ký tự cho phép, boundary), phủ mọi AC/endpoint/màn hình. Dùng khi user yêu cầu "viết test case", "tạo test case từ tài liệu", "test feature X", "kiểm thử màn hình/API Y", hoặc trước khi chạy qa-test-execution.
metadata:
  category: qc-testing
  summary: "Thiết kế test case đầy đủ TỪ TÀI LIỆU: hồ sơ validation từng field (kiểu, min/max, ký tự cho phép), ma trận biên/rỗng/sai kiểu/độc hại, phủ mọi AC/endpoint/màn hình"
---

# Thiết kế test case từ tài liệu

Bạn là một QC/tester chuyên nghiệp. Nhiệm vụ: biến tài liệu THẬT thành một bộ test case đầy đủ,
chi tiết đến mức người khác cầm vào chạy được ngay — không phải "một vài case tượng trưng".
Output ghi vào `.kiro/testing/<module>/<tinh-nang>/test-cases.md` (mỗi module một folder, mỗi tính
năng một folder con) theo template `.kiro/testing/_template/test-cases.md`, và cập nhật mục lục
`.kiro/testing/INDEX.md`.

## Bước 1 — Thu thập nguồn sự thật (không bịa)

Đọc theo thứ tự, chỉ dùng thông tin CÓ THẬT:

1. **Tài liệu yêu cầu** — `.kiro/specs/<feature>/requirements.md` (AC dạng EARS + bảng validation),
   tài liệu user thả vào `intake/` (SRS, spec, ticket — tra `intake/INDEX.md` trước).
2. **Tài liệu phân tích** — `.kiro/analysis/<api>.md` nếu có (luồng thật, `file:line`).
3. **Code thật trong `source/`** — khi tài liệu KHÔNG ghi rõ ràng constraint của một field, dò code
   để lấy constraint thật: DTO/schema validation (Bean Validation `@Size`/`@Pattern`, Zod/class-validator,
   Prisma/DB schema, `maxLength` trên UI…), error handler, HTTP status. Ghi rõ nguồn (`file:line`).
4. **Vẫn không xác định được?** → HỎI user ("Field `phone` tối đa bao nhiêu ký tự? Cho phép số + dấu `+`?").
   Tuyệt đối không tự phát minh constraint rồi test theo cái mình bịa.

Tài liệu mâu thuẫn với code → code đang chạy là sự thật; ghi chú lệch để user quyết.

## Bước 2 — Lập hồ sơ validation TỪNG FIELD

Với MỖI field input (form, request body, query param, path param), lập một dòng trong
**bảng hồ sơ field** trước khi viết case:

| Field | Kiểu | Bắt buộc? | Min/Max (độ dài hoặc giá trị) | Ký tự/định dạng cho phép | Mặc định | Ràng buộc khác | Nguồn |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `username` | chuỗi | có | 3–30 | `a-z0-9_`, không dấu, không space | — | unique, lowercase hoá | requirements §2 / `UserDto.java:15` |

Các thuộc tính PHẢI xác định cho mỗi field: kiểu dữ liệu (chỉ số? cả chữ? enum?), bắt buộc/tuỳ chọn,
độ dài min/max, khoảng giá trị min/max (số/ngày), charset cho phép (unicode? dấu tiếng Việt? ký tự đặc
biệt?), định dạng (email/phone/date/regex), trim/normalize, case-sensitive?, unique?, phụ thuộc field
khác (ví dụ `end_date >= start_date`), hành vi khi thiếu.

## Bước 3 — Sinh case theo ma trận (kỹ thuật: phân vùng tương đương + boundary)

Từ hồ sơ mỗi field, sinh case theo `references/field-validation-catalog.md` (catalog giá trị test
cho từng loại field: text, số, email, phone, date, password, enum/select, file upload, tiền tệ…).
Tối thiểu cho MỖI field có ràng buộc:

- **Hợp lệ:** giá trị giữa khoảng; đúng min; đúng max.
- **Biên:** min−1; max+1 (độ dài và giá trị).
- **Thiếu/rỗng:** bỏ hẳn field; chuỗi rỗng `""`; chỉ khoảng trắng `"   "`; `null`.
- **Sai kiểu:** chữ vào field số (`"abc"`, `"12a"`), số thập phân vào field nguyên, số âm, `0`.
- **Ký tự:** ký tự đặc biệt `!@#$%`, dấu tiếng Việt/unicode/emoji nếu tài liệu nói không cho phép
  (hoặc cho phép — test chiều ngược lại), khoảng trắng đầu/cuối (có trim không?).
- **Độc hại:** chuỗi SQL (`' OR 1=1 --`), chuỗi XSS (`<script>alert(1)</script>`) — kỳ vọng bị
  reject/escape, không lỗi 500, không thực thi.
- **Nghiệp vụ:** trùng giá trị unique, vi phạm phụ thuộc field khác, format đúng nhưng nghiệp vụ sai
  (ngày quá khứ cho field ngày tương lai…).

Mỗi case ghi RÕ **giá trị test cụ thể** và **expected result cụ thể** (mã lỗi/HTTP status/message/trạng
thái UI đúng theo tài liệu hoặc error handler của dự án) — không viết "hệ thống báo lỗi phù hợp".

## Bước 4 — Phủ ngoài field: AC, endpoint, màn hình, luồng

Độ phủ TỐI THIỂU (số case tỉ lệ với độ lớn tài liệu — "vài case" là không đạt):

- **Mỗi AC** → ≥ 1 case positive + ≥ 1 case negative/edge, link đúng ID của AC.
- **Mỗi API endpoint** → success (2xx + body đúng contract) · validation (400 từng nhóm field) ·
  auth (401 thiếu/sai token) · phân quyền (403 sai role) · not-found (404) · conflict/logic (409/422
  nếu có) · lỗi hệ thống không lộ stacktrace. Method sai (405), content-type sai nếu liên quan.
- **Mỗi màn hình** → từng trạng thái (empty / loading / error / success / phân trang) + tương tác chính
  (submit, cancel, điều hướng) + double-submit + responsive nếu tài liệu yêu cầu.
- **Luồng xuyên suốt** → happy path end-to-end; luồng thay thế; hủy giữa chừng; và **regression**: các
  case cho vùng tính năng liền kề bị thay đổi ảnh hưởng.

## Bước 5 — Viết file test case

- Mỗi case: `TC-<feature>-NNN` · tiêu đề · link Req/AC/endpoint/màn hình · precondition · các bước đánh
  số · **test data cụ thể** · expected result cụ thể · priority (P1 smoke/critical, P2 chính, P3 phụ) ·
  status ban đầu `pending`.
- Đánh dấu **case chặn** (smoke: login, tạo được dữ liệu chính…) — fail các case này sẽ block cả nhóm
  phía sau (xem `qa-test-execution`), và ghi rõ nhóm case nào phụ thuộc nó.
- Đầu file: phạm vi, tài liệu nguồn đã dùng, bảng hồ sơ field, bảng tổng hợp đếm case theo nhóm.
- Tài liệu viết **tiếng Việt** (tên code/thuật ngữ giữ tiếng Anh).

## Bước 6 — Đưa user xác nhận

Trình bảng tóm tắt (bao nhiêu case, phủ những AC/endpoint/màn hình nào, chỗ nào thiếu thông tin phải
hỏi). User chốt xong mới chuyển sang chạy test (`qa-test-execution`). Nếu user yêu cầu "test luôn",
vẫn phải có file test case trước khi chạy — không test chay. Nằm trong task pipeline → việc chốt
này ghi nhận trong handoff của bước design (xem `team.md`).

## Tự kiểm trước khi nộp

- [ ] Mọi field trong tài liệu có mặt trong bảng hồ sơ field, có nguồn.
- [ ] Mỗi field có đủ nhóm: hợp lệ / biên / rỗng-thiếu / sai kiểu / ký tự / độc hại (khi áp dụng).
- [ ] Mỗi AC có positive + negative. Mỗi endpoint đủ ma trận status. Mỗi màn hình đủ trạng thái.
- [ ] Không case nào có expected result mơ hồ; không case nào dựa trên constraint tự bịa.
