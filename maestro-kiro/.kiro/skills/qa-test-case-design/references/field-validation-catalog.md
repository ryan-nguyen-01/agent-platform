# Catalog giá trị test theo loại field

Tra bảng theo loại field để sinh giá trị test cụ thể. Nguyên tắc: mỗi ràng buộc trong tài liệu
sinh ra ít nhất một case đúng-biên, một case vượt-biên, và một case sai-kiểu. Giá trị dưới đây là
mẫu — thay `min`/`max`/format bằng con số THẬT trong tài liệu hoặc code.

## 1. Chuỗi tự do (tên, tiêu đề, mô tả)

| Nhóm | Giá trị test | Kỳ vọng (theo tài liệu) |
| --- | --- | --- |
| Hợp lệ | chuỗi bình thường giữa khoảng; đúng `min` ký tự; đúng `max` ký tự | chấp nhận |
| Biên | `min−1` ký tự; `max+1` ký tự | reject + message độ dài |
| Rỗng | bỏ field; `""`; `"   "` (chỉ space); `null` | bắt buộc → reject; tuỳ chọn → chấp nhận/bỏ qua |
| Trim | `"  abc  "` | tuỳ tài liệu: trim rồi lưu, hay reject |
| Charset | dấu tiếng Việt `"Nguyễn Văn A"`; emoji `"😀"`; ký tự đặc biệt `"!@#$%^&*"` | theo charset cho phép |
| Độc hại | `' OR 1=1 --` · `<script>alert(1)</script>` · `../../etc/passwd` | reject/escape; không 500; không thực thi |
| Khác | chuỗi toàn số `"12345"` (field cho cả chữ); xuống dòng trong field 1 dòng | theo tài liệu |

## 2. Số nguyên / số thập phân (số lượng, tuổi, giá)

| Nhóm | Giá trị test | Kỳ vọng |
| --- | --- | --- |
| Hợp lệ | giá trị giữa khoảng; đúng `min`; đúng `max` | chấp nhận |
| Biên | `min−1`; `max+1` | reject + message khoảng giá trị |
| Đặc biệt | `0`; số âm `-1`; số rất lớn (overflow: `2147483648`, `9999999999999`) | theo tài liệu / không crash |
| Sai kiểu | `"abc"`; `"12a"`; `"1,000"` vs `"1000"`; `"1.5"` vào field nguyên; `" 1"` | reject sai kiểu |
| Thập phân | đúng số chữ số lẻ cho phép; vượt (`1.999` khi cho 2 lẻ); dấu `.` vs `,` theo locale | theo tài liệu |
| Rỗng | bỏ field; `""`; `null` | bắt buộc → reject |

## 3. Email

Hợp lệ: `a@b.co`, có `+tag`, subdomain, đúng `max` độ dài.
Không hợp lệ: thiếu `@`; thiếu domain (`a@`); thiếu local (`@b.co`); 2 dấu `@`; space giữa chừng;
`a@b` (không TLD — theo tài liệu); dấu tiếng Việt trong local-part; quá `max`; hoa/thường (`A@B.CO`
— có normalize không?); email đã tồn tại (nếu unique).

## 4. Số điện thoại

Xác định từ tài liệu: chỉ số hay cho `+`/space/`-`? độ dài cố định hay khoảng? đầu số hợp lệ?
Test: đúng độ dài; thiếu 1 số; thừa 1 số; có chữ `"09abc"`; có `+84` vs `0`; space/`-` giữa chừng;
số toàn `0`; đầu số không tồn tại (nếu tài liệu ràng buộc).

## 5. Ngày / giờ

Hợp lệ: đúng format tài liệu (`dd/MM/yyyy` hay ISO?); ngày biên (đầu/cuối tháng, 29/02 năm nhuận).
Không hợp lệ: `31/02/2026`; `13` cho tháng; format khác tài liệu; chuỗi rác; ngày quá khứ cho field
tương lai (và ngược lại); `end < start` với cặp khoảng ngày; timezone (nếu API — gửi UTC vs local).

## 6. Mật khẩu

Theo policy tài liệu (min/max, chữ hoa, chữ thường, số, ký tự đặc biệt): mỗi thiếu-một-yêu-cầu là một
case; đúng min; đúng max; max+1; space đầu/cuối (thường KHÔNG trim mật khẩu); unicode; trùng mật khẩu
cũ (nếu đổi mật khẩu); confirm không khớp; hiển thị không lộ plaintext trong log/response.

## 7. Enum / select / radio / checkbox

Hợp lệ: từng giá trị được liệt kê. Không hợp lệ: giá trị ngoài danh sách (`"XX"`); hoa/thường khác;
số thứ tự thay vì giá trị; rỗng khi bắt buộc chọn; nhiều giá trị khi chỉ cho một (và ngược lại).
API: gửi thẳng giá trị lạ qua request (bỏ qua UI) — server PHẢI tự validate, không tin client.

## 8. File upload

Đúng loại + đúng size; size đúng max; max+1 byte; 0 byte; sai extension; extension đúng nhưng nội dung
sai (đổi đuôi `.exe` → `.jpg`); tên file có unicode/space/ký tự đặc biệt/rất dài; upload trùng; không
chọn file khi bắt buộc; nhiều file khi chỉ cho một (nếu multi: đúng max số file, max+1).

## 9. Tiền tệ / phần trăm

Số lẻ theo đơn vị (VND thường 0 lẻ, USD 2 lẻ); âm; `0`; vượt max; làm tròn (tài liệu quy định
round half-up?); tổng các phần = 100% (nếu phân bổ); format hiển thị vs giá trị lưu.

## 10. ID / khoá ngoại (path/query param)

Tồn tại; không tồn tại (404); sai kiểu (`abc` cho id số); id của tenant/user khác (phân quyền — 403/404);
id đã xoá mềm; UUID sai format; số âm/0.

## 11. Phân trang / sắp xếp / tìm kiếm (query param)

`page=0/1/max/max+1/âm/chữ`; `size=0/1/max/max+1` (có chặn size khổng lồ không?); sort field hợp lệ /
không tồn tại; search chuỗi rỗng / 1 ký tự / rất dài / ký tự đặc biệt / SQL-XSS / có dấu tiếng Việt
(tìm không dấu có ra?); kết quả rỗng hiển thị đúng.

## Quy tắc chung khi thiếu thông tin

Tài liệu không ghi max-length / khoảng giá trị / charset cho một field →
(1) dò code validation + schema DB trong `source/` lấy constraint thật (ghi `file:line`);
(2) vẫn không có → hỏi user. KHÔNG tự chọn một con số rồi coi đó là yêu cầu.
