# Requirements — Trang hồ sơ người dùng (ví dụ)

> Spec MẪU để minh hoạ luồng requirements → design → tasks. Xoá thư mục này khi bắt đầu dự án thật.

## Introduction

Cho phép người dùng đã đăng nhập xem và cập nhật hồ sơ cá nhân (tên hiển thị, ảnh đại diện). Backend
Spring Boot, frontend ReactJS.

## Requirements

### Requirement 1 — Xem hồ sơ

**User story:** Là người dùng đã đăng nhập, tôi muốn xem hồ sơ của mình, để biết thông tin hiện tại.

**Acceptance criteria (EARS):**

1. WHEN người dùng mở trang hồ sơ THE SYSTEM SHALL hiển thị tên hiển thị và ảnh đại diện hiện tại.
2. IF chưa đăng nhập THEN THE SYSTEM SHALL chuyển hướng sang trang đăng nhập.

### Requirement 2 — Cập nhật hồ sơ

**User story:** Là người dùng, tôi muốn đổi tên hiển thị và ảnh đại diện, để hồ sơ luôn cập nhật.

**Acceptance criteria (EARS):**

1. WHEN người dùng lưu form hợp lệ THE SYSTEM SHALL cập nhật hồ sơ và hiển thị thông báo thành công.
2. IF tên hiển thị rỗng hoặc > 50 ký tự THEN THE SYSTEM SHALL báo lỗi validation và KHÔNG lưu.

## Quy tắc dữ liệu & validation (nguồn cho test case)

| Field | Kiểu | Bắt buộc? | Min/Max (độ dài hoặc giá trị) | Ký tự/định dạng cho phép | Message/mã lỗi khi sai |
| --- | --- | --- | --- | --- | --- |
| `displayName` | chuỗi | có | 1–50 ký tự (sau trim) | chữ (có dấu), số, khoảng trắng; không emoji | 400 `DISPLAY_NAME_INVALID` "Tên hiển thị 1–50 ký tự" |
| `avatar` | file ảnh | không | ≤ 2 MB | jpg/png; kiểm content-type thật, không tin extension | 400 `AVATAR_INVALID` "Ảnh jpg/png tối đa 2MB" |

Ràng buộc chéo (field phụ thuộc nhau, unique, trạng thái cho phép):

- Chỉ chủ tài khoản (đúng token) được cập nhật hồ sơ của mình — user khác trả 403.

## Out of scope

- Đổi mật khẩu, đổi email (spec khác).

## Open questions

- Ảnh đại diện lưu ở đâu (S3 / local)? — cần chốt ở `design.md`.
