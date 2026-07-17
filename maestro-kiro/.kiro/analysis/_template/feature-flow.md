# Luồng: <tên tính năng>

> Trạng thái: ⏳ chờ user xác nhận · Phạm vi: <một tính năng — vd "tạo đơn hàng">
> Tài liệu mô tả CODE HIỆN TẠI (không phải đề xuất). Mỗi mục có `file:line` để kiểm chứng.
> Liên hệ với tính năng khác: xem `.kiro/analysis/dependency-map.md`.

## 1. Tóm tắt nghiệp vụ

<Tính năng làm gì, cho ai, kết quả mong đợi — 2–4 câu.>

## 2. Phía FE (bỏ nếu không có UI)

- **Route/màn hình:** `<path>` — component `<Page>` — `file:line`; điều kiện render (guard/role)
- **Component & sự kiện:** <form/nút → handler nào> — `file:line`
- **Validation FE:** <rule từng field> — `file:line` (đối chiếu BE ở mục 5)
- **State:** <store/query key, cache/invalidate khi nào> — `file:line`
- **API client:** <hàm gọi, endpoint, dựng payload, token gắn ở đâu, retry/timeout> — `file:line`
- **Xử lý response:** thành công → <cập nhật state/điều hướng>; lỗi → xem bảng mục 6

## 3. Contract FE ↔ BE (phần PHẢI GIỮ khi chuyển đổi)

- **Endpoint:** `<METHOD /path>` — auth: <loại token, role/scope>
- **Request:** <từng field: tên, kiểu, bắt buộc, ràng buộc> — `file:line`
- **Response:** <từng field + status code theo tình huống> — `file:line`

## 4. Phía BE — luồng từng bước

| # | Bước | Thành phần (`file:line`) | Input → Output / side effect |
| --- | --- | --- | --- |
| 1 | Middleware/guard | | |
| 2 | Controller | | |
| 3 | Validation | | |
| 4 | Business rules | | <liệt kê TỪNG rule: điều kiện → hệ quả> |
| 5 | Repository/DB | | <bảng, đọc/ghi, query chính, index> |
| 6 | Transaction | | <bắt đầu/commit/rollback ở đâu> |
| 7 | Gọi ngoài/event | | <sync/async, timeout, retry, bù trừ khi fail> |
| 8 | Response mapping | | |

## 5. Business rules & validation BE

- <Rule 1: điều kiện → hệ quả> — `file:line`
- <FE chặn nhưng BE không validate lại field nào? — ghi rõ, đây là lỗ hổng> 

## 6. Bảng hành vi theo case (xuyên FE ↔ BE)

| Case | BE xử lý (`file:line`) | Response | FE hiển thị/hành xử (`file:line`) |
| --- | --- | --- | --- |
| Happy path | | | |
| Validation fail <field> | | | |
| Không có quyền / hết hạn token | | | |
| Resource không tồn tại | | | |
| Trùng / conflict | | | |
| Service ngoài fail / timeout | | | |
| Double-submit / concurrent | | | |
| Dữ liệu biên (rỗng / 0 / rất nhiều) | | | |
| <case KHÔNG được xử lý trong code> | **không xử lý** | | |

## 7. Dữ liệu & side effect

- **Bảng/entity:** <bảng nào đọc, bảng nào ghi, thao tác> — `file:line`
- **Side effect:** <mail, log, cache, event, file…> — `file:line`

## 8. Ghi chú chuyển đổi (migration notes)

- **Coupling cứng:** <join/transaction/gọi nội bộ chung với tính năng nào> — `file:line`
- **Contract phải giữ:** <endpoint/DTO bên nào đang phụ thuộc>
- **Trạng thái chia sẻ:** <session/cache/static/file cục bộ>
- **Thứ tự & idempotency:** <giả định tuần tự/duy nhất; retry có an toàn?>
- **Rủi ro khi chuyển:** <hành vi ngầm chỉ có trong code, case không xử lý>

## 9. Điểm chưa chắc / cần user xác nhận

- <chỗ mơ hồ — KHÔNG bịa>
