# Bugs — <tên-feature>

Mỗi bug một mục, mới nhất trên cùng. Không secret, không log dài (trích phần liên quan).

## BUG-<feature>-001 — <tiêu đề ngắn>

- **Mức:** blocker | non-blocker
- **Case liên quan:** TC-<feature>-NNN (+ các case bị chặn nếu blocker)
- **Các bước tái hiện:**
  1. <bước>
  2. <bước>
- **Test data:** <giá trị dùng khi phát hiện>
- **Expected:** <theo tài liệu/AC>
- **Actual:** <nguyên văn: status code, message, stacktrace rút gọn, trạng thái UI>
- **Vùng nghi ngờ:** <file:line nếu dò được>
- **Trạng thái:** open → fixing → fixed (chờ retest) → closed | reopened | deferred (user)
- **Fix:** <root cause + đã sửa gì, file nào — dev điền>
- **Retest:** <kết quả chạy lại case + regression liên quan — tester điền, kèm bằng chứng>
- **Phòng ngừa (bắt buộc khi đóng bug do code):** <luật để lỗi này không lặp — vd "mọi field
  validation FE phải có bản sao ở BE"; kiểm tra regression nào cần thêm>
- **Bài học:** <đáng khái quát cho nhiều nơi? → ghi vào `lessons.md` (ghi id L-xxx ở đây) ·
  đặc thù service? → Gotchas trong `svc-<tên>.md` · không đáng → "không">
