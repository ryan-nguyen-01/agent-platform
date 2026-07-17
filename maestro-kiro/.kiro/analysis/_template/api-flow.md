# Phân tích: <Tên API / use-case>

> Trạng thái: ⏳ chờ người dùng xác nhận · Phạm vi: <API/endpoint hoặc luồng nghiệp vụ>
> Tài liệu mô tả CODE HIỆN TẠI (không phải đề xuất). Mỗi mục có trích dẫn `file:line` để kiểm chứng.

## 1. Tóm tắt nghiệp vụ

<API/luồng này làm gì, phục vụ ai, kết quả mong đợi — 2–4 câu, tiếng Việt.>

## 2. Đầu vào / Đầu ra

- **Endpoint / trigger:** `<METHOD /path>` hoặc `<event/queue>` — `file:line`
- **Đầu vào (request/DTO):** <các field, kiểu, ràng buộc validation> — `file:line`
- **Đầu ra (response):** <shape trả về, mã trạng thái> — `file:line`
- **Auth / phân quyền:** <yêu cầu đăng nhập? role/scope nào?> — `file:line`

## 3. Luồng xử lý (từng bước)

| # | Bước | Thành phần (file:line) | Mô tả việc xảy ra |
|---|------|------------------------|-------------------|
| 1 | Nhận request | `controller ...` | <…> |
| 2 | Validate | `...` | <…> |
| 3 | Business logic | `service ...` | <…> |
| 4 | Truy cập DB | `repository ...` | <bảng/query, đọc hay ghi> |
| 5 | Gọi ngoài / event | `...` | <API ngoài, message, …> |
| 6 | Trả kết quả | `...` | <…> |

## 4. Quy tắc nghiệp vụ (business rules)

- <Quy tắc 1: điều kiện → hệ quả> — `file:line`
- <Quy tắc 2 …> — `file:line`

## 5. Dữ liệu & trạng thái thay đổi

- **Bảng/entity bị ghi:** <bảng, thao tác, transaction?> — `file:line`
- **Side effect:** <gửi mail, ghi log, cập nhật cache, bắn event…> — `file:line`

## 6. Lỗi & trường hợp biên

| Tình huống | Xử lý hiện tại | Mã/định dạng lỗi | `file:line` |
|------------|----------------|------------------|-------------|
| <vd: không tìm thấy> | <…> | <…> | <…> |

## 7. Phụ thuộc

- <Service/module/thư viện/bảng mà luồng này phụ thuộc.>

## 8. Điểm chưa chắc / cần người dùng xác nhận

- <Chỗ code mơ hồ hoặc giả định — nêu rõ để người dùng chốt. KHÔNG bịa.>

## 9. Nhận xét (tuỳ chọn)

- <Rủi ro / nợ kỹ thuật / đề xuất — chỉ ghi chú, không tự sửa.>
