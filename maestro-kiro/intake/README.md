# intake/

Thả MỌI tài liệu thô vào đây: SRS/spec, yêu cầu tính năng, bug report, error log, screenshot,
data dump, biên bản họp… Kiro sẽ triage: phân loại từng file, lập mục lục `intake/INDEX.md`,
và dùng chúng làm CĂN CỨ khi phân tích, viết code, và **thiết kế test case** — không tự bịa
thông tin khi tài liệu đã có.

Quy tắc:

- Thư mục này chứa TÀI LIỆU, không chứa code. Code của dự án để ở `source/`. Lỡ thả code vào đây,
  Kiro sẽ hỏi trước khi chuyển sang `source/` — không tự chuyển.
- Tài liệu mâu thuẫn với code đang chạy → code là sự thật; Kiro đánh dấu tài liệu là "nghi cũ"
  và hỏi user, không âm thầm tin theo tài liệu.
- **CẢNH BÁO secret:** đừng thả secret thật (.env, credential, token, dump có mật khẩu). Kiro phát
  hiện sẽ gắn cờ và không bao giờ trích nội dung đó vào bất kỳ file nào — nhưng an toàn nhất là
  đừng để nó vào đây.
