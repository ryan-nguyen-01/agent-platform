# Analysis — phân tích luồng & nghiệp vụ

Khi người dùng yêu cầu **"phân tích luồng / nghiệp vụ của X"** (một API, use-case, màn hình — hoặc
cả module để chuẩn bị chuyển đổi), Kiro nạp skill **`analyze-flow`**, **dò code thật rất kỹ** rồi
viết file phân tích bằng **tiếng Việt** vào đây để người dùng đọc và **xác nhận** — KHÔNG sửa code
trong bước này.

```text
.kiro/analysis/
├── INDEX.md                    mục lục SỐNG: module · tính năng · file · trạng thái — tìm ở đây trước
├── dependency-map.md           bản đồ SỐNG: tính năng nào dùng chung bảng/service/component/event
│                               với tính năng nào — căn cứ fix bug an toàn & tách microservices
├── _template/                  feature-flow.md (full-stack) · api-flow.md (BE-only)
└── <module>/                   MỖI MODULE MỘT FOLDER (vd order/, user/, payment/)
    └── <tinh-nang>.md          mỗi tính năng một file (vd order/order-create.md) — không gộp
```

Hai template trong `_template/`:

- `feature-flow.md` — **full-stack**: trace FE (route → component → state → API client) sang BE
  (controller → rules → DB → transaction → gọi ngoài), bảng hành vi theo case, ghi chú migration.
- `api-flow.md` — bản gọn chỉ BE cho một API.

## Quy trình

1. **Dò end-to-end** theo code thật (không đoán): entrypoint → controller → validation/DTO → service /
   business rules → repository / truy vấn DB → gọi service ngoài / event / message → response → xử lý
   lỗi & edge case → auth/phân quyền → side effect (gửi mail, ghi log, cập nhật cache…).
2. **Trích dẫn vị trí thật** (đường dẫn `file:line`) cho mỗi bước — để người dùng kiểm chứng.
3. **Viết file** từ `_template/api-flow.md`, bằng tiếng Việt (tên code/thuật ngữ giữ tiếng Anh).
4. **Chờ người dùng xác nhận.** Nếu sai/thiếu, sửa lại tài liệu. Chỉ khi được xác nhận mới làm bước
   tiếp theo (sửa/bổ sung code), và việc đó vẫn theo luồng Ask → Do → Log bình thường.

Mục tiêu: tài liệu phản ánh ĐÚNG code hiện tại — nếu chỗ nào chưa chắc thì ghi rõ "chưa chắc / cần xác
nhận", tuyệt đối không bịa.
