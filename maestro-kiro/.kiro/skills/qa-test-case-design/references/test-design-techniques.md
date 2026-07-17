# Kỹ thuật thiết kế test case

Dùng khi cần chọn cách sinh case cho một yêu cầu phức tạp (nhiều điều kiện, nhiều trạng thái)
thay vì chỉ liệt kê theo field.

## Phân vùng tương đương (Equivalence Partitioning)

Chia input thành các vùng mà hệ thống xử lý GIỐNG nhau; mỗi vùng lấy 1 đại diện.
Ví dụ field tuổi 18–60: vùng hợp lệ [18–60], vùng dưới (<18), vùng trên (>60), vùng sai kiểu (chữ),
vùng rỗng. → 5 case đại diện thay vì thử vô hạn giá trị.

## Phân tích giá trị biên (Boundary Value Analysis)

Bug tập trung ở biên. Với khoảng [min, max] test: `min−1, min, min+1, max−1, max, max+1`.
Áp cho cả độ dài chuỗi, giá trị số, số phần tử danh sách, số trang, kích thước file.

## Bảng quyết định (Decision Table)

Khi kết quả phụ thuộc TỔ HỢP nhiều điều kiện (ví dụ: loại khách × mã giảm giá × giá trị đơn):
liệt kê điều kiện thành cột, mỗi tổ hợp có nghĩa là một rule = một case. Nén các tổ hợp cho cùng
kết quả. Đảm bảo phủ mọi rule trong tài liệu nghiệp vụ, kể cả nhánh "không áp dụng".

## Chuyển trạng thái (State Transition)

Cho đối tượng có vòng đời (đơn hàng: draft → confirmed → shipped → done/cancelled):
- mỗi chuyển hợp lệ = 1 case;
- mỗi chuyển KHÔNG hợp lệ trong tài liệu (ship một đơn draft, hủy đơn đã done) = 1 case negative,
  kỳ vọng bị chặn với message/status đúng.

## Pairwise (khi tổ hợp bùng nổ)

Nhiều tham số độc lập mỗi cái vài giá trị (browser × role × ngôn ngữ…) → phủ từng CẶP giá trị thay vì
tích Descartes đầy đủ. Chỉ dùng cho tham số thật sự độc lập; điều kiện nghiệp vụ liên quan nhau phải
dùng bảng quyết định.

## Đoán lỗi (Error Guessing) — kinh nghiệm tester

Các điểm hay vỡ: double-click nút submit (tạo 2 bản ghi?); back/refresh giữa luồng; hết hạn session
giữa form dài; hai user sửa cùng bản ghi; mất mạng lúc submit; dữ liệu cũ (bản ghi tạo trước khi đổi
schema); danh sách 0 / 1 / rất nhiều phần tử; ký tự có dấu trong search/sort; timezone lệch ngày.

## Ma trận API (mỗi endpoint)

| Chiều | Case |
| --- | --- |
| Thành công | 2xx, body đúng contract (đủ field, đúng kiểu), side effect đúng (DB, event) |
| Validation | 400 cho từng nhóm field sai (theo catalog field) — message/mã lỗi đúng error shape dự án |
| AuthN | không token 401; token sai/hết hạn 401 |
| AuthZ | đúng đăng nhập nhưng sai quyền/khác tenant 403 (hoặc 404 theo thiết kế) |
| Not found | resource không tồn tại 404 |
| Xung đột | trùng unique 409; trạng thái không cho phép 409/422 |
| Method/format | method sai 405; content-type sai 415; body không phải JSON 400 |
| Ổn định | server error không lộ stacktrace; idempotency khi retry (nếu tài liệu yêu cầu) |

## Ma trận màn hình (mỗi screen)

| Chiều | Case |
| --- | --- |
| Trạng thái | empty (chưa có dữ liệu) · loading · error (API fail) · success · phân trang |
| Form | từng field theo catalog · message lỗi hiển thị đúng chỗ · submit disable khi đang gửi |
| Tương tác | submit thành công · cancel · double-submit · điều hướng đi/quay lại giữ trạng thái? |
| Hiển thị | dữ liệu dài (truncate?) · unicode · số/ngày/tiền theo locale |
| Responsive & a11y | breakpoint tài liệu yêu cầu · focus/label cơ bản |

## Regression — chọn case khi sửa code có sẵn

Sửa vùng X → chạy lại: (1) case của chính X; (2) case của tính năng GỌI hoặc DÙNG CHUNG X (tra
`.kiro/steering/inventory.md` xem component/helper nào dùng chung); (3) smoke toàn luồng chính.
