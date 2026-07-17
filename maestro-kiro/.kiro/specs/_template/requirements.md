# Requirements — <tên-feature>

## Giới thiệu

<1–2 câu: feature này là gì và giải quyết vấn đề gì. Liên hệ ngữ cảnh ở product.md.>

## Requirements

### Requirement 1 — <tiêu đề ngắn>

**User story:** Là <vai trò>, tôi muốn <khả năng>, để <lợi ích>.

**Acceptance criteria (EARS):**

1. WHEN <sự kiện/điều kiện> THE SYSTEM SHALL <phản hồi quan sát được>.
2. IF <tiền điều kiện> THEN THE SYSTEM SHALL <phản hồi>.
3. WHILE <trạng thái> THE SYSTEM SHALL <hành vi liên tục>.
4. WHERE <bối cảnh áp dụng> THE SYSTEM SHALL <phản hồi>.

### Requirement 2 — <tiêu đề ngắn>

**User story:** Là <vai trò>, tôi muốn <khả năng>, để <lợi ích>.

**Acceptance criteria (EARS):**

1. WHEN <…> THE SYSTEM SHALL <…>.

## Quy tắc dữ liệu & validation (nguồn cho test case)

> Ghi RÕ ràng buộc từng field — mơ hồ ở đây là bug ở test. Không biết thì hỏi, đừng bỏ trống.

| Field | Kiểu | Bắt buộc? | Min/Max (độ dài hoặc giá trị) | Ký tự/định dạng cho phép | Message/mã lỗi khi sai |
| --- | --- | --- | --- | --- | --- |
| `<field>` | <chuỗi/số/ngày/enum/file> | <có/không> | <vd 3–30 ký tự> | <vd a-z0-9, không dấu · email · dd/MM/yyyy> | <vd 400 `USERNAME_INVALID` "..."> |

Ràng buộc chéo (field phụ thuộc nhau, unique, trạng thái cho phép):

- <vd `end_date` >= `start_date`; `email` unique theo tenant>

## Ngoài phạm vi

- <những gì cố tình không làm>

## Câu hỏi mở

- <điều cần chốt trước khi design>
