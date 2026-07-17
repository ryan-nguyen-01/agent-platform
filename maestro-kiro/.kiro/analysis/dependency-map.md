# Bản đồ phụ thuộc giữa các tính năng

> File SỐNG — skill `analyze-flow` cập nhật sau mỗi tính năng phân tích xong. Mục đích: nhìn một
> chỗ biết tính năng nào dính tính năng nào qua cái gì (bảng, service, component, event) — căn cứ
> để fix bug không vỡ chỗ khác và để tách monolith → microservices.
> Chưa có dữ liệu — sẽ được điền khi chạy phân tích tính năng đầu tiên.

## Tính năng đã phân tích

| Tính năng | File phân tích | Trạng thái |
| --- | --- | --- |
| <tên> | `.kiro/analysis/<module>/<file>.md` | ⏳ chờ xác nhận / ✅ đã chốt |

## Dùng chung dữ liệu (bảng/entity)

| Bảng | Tính năng ĐỌC | Tính năng GHI | Ghi chú (transaction chung?) |
| --- | --- | --- | --- |

## Dùng chung code (service/helper BE · component/hook FE)

| Thành phần | Đường dẫn | Tính năng dùng | Ghi chú |
| --- | --- | --- | --- |

## Gọi nhau & event

| Từ | Đến | Kiểu (sync API / async event / gọi hàm nội bộ) | `file:line` |
| --- | --- | --- | --- |

## Cụm coupling (đơn vị cân nhắc khi tách service)

- **Cụm <tên>:** <các tính năng dính nhau qua bảng/transaction nào — tách thì phải đổi gì>
