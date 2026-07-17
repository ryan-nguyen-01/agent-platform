---
inclusion: fileMatch
fileMatchPattern: "**/*.{ts,tsx,js,jsx,java}"
---
<!-- Tải khi đang sửa code (lúc cần tái dùng) để tiết kiệm context. Nếu Kiro không nạp được
     (bug fileMatch theo ext), đổi 2 dòng trên thành `inclusion: always`. -->

# Inventory — thứ dùng chung LIÊN-SERVICE

> Sổ này ghi những thứ dùng chung **giữa nhiều service** (shared package, design system, util chung).
> Đồ tái dùng **riêng từng service** nằm trong hồ sơ `svc-<tên>.md` của service đó — tra ở đó trước.

> Sổ ghi nhớ những thứ **dùng chung đã có sẵn** trong dự án, để Kiro **tái dùng thay vì viết lại**.
> Kiro điền sổ này khi quét dự án và **cập nhật mỗi khi phát hiện hoặc tạo thêm** một thành phần dù
> chung. Trước khi viết một component/hook/helper mới, Kiro PHẢI tra sổ này trước — nếu đã có thì dùng lại.
> (Tài liệu viết bằng tiếng Việt; tên code/thuật ngữ giữ nguyên tiếng Anh.)

## Component dùng chung (FE)

| Tên | Đường dẫn | Dùng để làm gì | Props/cách dùng chính |
|-----|-----------|----------------|-----------------------|
| `<Tên>` | `source/<app>/src/...` | <mô tả ngắn> | <props quan trọng / ví dụ dùng> |

## Hook tuỳ biến (FE)

| Hook | Đường dẫn | Dùng để làm gì | Chữ ký / trả về |
|------|-----------|----------------|-----------------|
| `useXxx` | `source/<app>/src/...` | <mô tả> | `useXxx(args) => ...` |

## Tiện ích / helper dùng chung (FE & BE)

| Tên | Đường dẫn | Dùng để làm gì |
|-----|-----------|----------------|
| `formatXxx` | `source/<app>/src/...` | <mô tả> |

## Thành phần dùng chung phía Backend

| Tên | Đường dẫn | Dùng để làm gì |
|-----|-----------|----------------|
| `BaseService` / `@ControllerAdvice` / mapper / DTO chung / exception chung | `...` | <mô tả> |

---

**Quy tắc giữ sổ:**
- Khi quét dự án (hoặc chạy hook `refresh-inventory`): liệt kê đầy đủ component/hook/helper/thành phần
  BE dùng chung kèm đường dẫn thật và công dụng.
- Khi tạo MỚI một thứ dùng chung: thêm ngay một dòng vào sổ.
- Khi phát hiện một thứ dùng chung chưa có trong sổ: bổ sung.
- Khi một thứ bị đổi tên/xoá: cập nhật/loại bỏ dòng tương ứng (sổ phải khớp với code thật).
