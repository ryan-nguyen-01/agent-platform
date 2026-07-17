---
inclusion: always
---

# Lessons — bài học rút từ lỗi (file SỐNG, luôn nạp)

Đây là bộ nhớ kinh nghiệm của workspace: **mỗi lỗi thật chỉ được phép xảy ra một lần** — sau đó nó
phải trở thành một bài học ở đây và thay đổi hành vi mọi phiên sau. Kiro đọc file này mỗi phiên
(luôn nạp) nên bài học nào nằm đây là LUẬT, ngang hàng contract.

## Khi nào PHẢI ghi bài học (trigger)

```text
1. User sửa lưng: "sai rồi", làm lại theo cách khác, revert thay đổi của Kiro
2. Bug do chính Kiro gây ra được xác nhận (từ luồng TEST hoặc user báo)
3. Assumption Kiro tự đặt hoá ra sai
4. Handoff bị trả lại / hỏi–đáp quá 1 vòng vì thiếu cùng một loại thông tin
5. Loay hoay >2 lần cùng một lỗi (thử–sai lặp) rồi mới tìm ra cách đúng
6. Kết thúc mỗi task pipeline: coordinator mini-retro — "điều gì làm chậm/suýt hỏng?"
```

## Cách viết một bài học (để nó thật sự đổi hành vi)

- **Khái quát hoá**: không ghi "field X ở service Y sai" mà ghi *loại* lỗi ("sửa validation mà không
  tra chỗ gọi chung"). Lỗi cụ thể theo service → ghi vào mục Gotchas của `svc-<tên>.md`; theo bug →
  các field phòng ngừa trong `bugs.md`. Ở đây chỉ giữ bài học DÙNG LẠI ĐƯỢC nhiều nơi.
- Mỗi bài học có: **Từ đâu** (nguồn thật — bug id / lần user sửa / seed) · **Vì sao** · **Áp dụng**
  (hành vi cụ thể lần sau).
- **Chống phình**: trước khi thêm, tìm bài trùng → cập nhật bài cũ thay vì thêm bài sinh đôi. Quá
  ~30 bài → gộp/khái quát. Bài sai hoặc hết thời → xoá. File này phải luôn ĐỌC ĐƯỢC TRONG 2 PHÚT.
- Bài học đụng convention/kiến trúc của một service → cập nhật `svc-<tên>.md` là chính, ở đây chỉ
  giữ phiên bản khái quát nếu đáng.

## Bài học hiện có

### L-001 — "Xong" phải có bằng chứng chạy thật

- **Từ đâu:** seed (đúc kết vận hành Claude/Codex)
- **Vì sao:** "nhìn code thấy đúng" là nguồn lỗi lớn nhất của agent; code chưa chạy là code chưa xong.
- **Áp dụng:** trước khi báo xong: build/test/chạy thật vùng đổi, đính output. Không có cách chạy →
  nói thẳng "chưa verify được" thay vì tuyên xong.

### L-002 — Đọc trọn đơn vị và dò chỗ gọi trước khi sửa

- **Từ đâu:** seed
- **Vì sao:** sửa theo mảnh nhìn thấy → vỡ ngầm ở caller; đặc biệt nguy hiểm với thứ dùng chung
  liên-service.
- **Áp dụng:** mở trọn hàm/file trước khi sửa; thứ dùng chung → tra inventory/`services.md` xem ai
  đang dùng rồi mới đổi.

### L-003 — Tái hiện trước, sửa tận gốc sau

- **Từ đâu:** seed
- **Vì sao:** fix theo phỏng đoán tạo bug mới + che bug cũ; vá triệu chứng thì lỗi quay lại chỗ khác.
- **Áp dụng:** chưa tái hiện được thì chưa sửa; phân biệt nơi lỗi LỘ RA và nơi lỗi SINH RA.

### L-004 — Không biết thì nói không biết, thiếu input thì hỏi

- **Từ đâu:** seed
- **Vì sao:** bịa constraint/contract/API tạo lỗi khó lần ra nhất — trông hợp lý nhưng sai từ gốc.
- **Áp dụng:** thiếu thông tin bắt buộc → `blocked: missing` hoặc hỏi user; ghi rõ mức chắc chắn
  khi suy luận.

### L-005 — Thay đổi nhỏ nhất thoả yêu cầu

- **Từ đâu:** seed
- **Vì sao:** refactor ngoài lề trộn với thay đổi chính → không review nổi, không bisect nổi khi hỏng.
- **Áp dụng:** đúng phạm vi task; muốn cải tiến thêm → đề xuất riêng, không tiện tay làm.

### L-006 — Một code path, không để xác sống

- **Từ đâu:** seed
- **Vì sao:** hai đường chạy song song / dead code do thay đổi tạo ra chính là kiểu "vẫn chạy rồi
  văng lỗi khó hiểu về sau".
- **Áp dụng:** thay xong thì xoá đường cũ trong cùng thay đổi; không giữ "để phòng".

### L-007 — Loay hoay 2 lần là dừng lại chẩn đoán lại

- **Từ đâu:** seed
- **Vì sao:** thử–sai biến thể trên một giả định sai chỉ đào sâu hố; lỗi lặp nghĩa là giả định sai,
  không phải xui.
- **Áp dụng:** sau 2 lần fail cùng một lỗi → dừng, viết ra giả định đang dùng, kiểm chứng từng cái
  bằng bằng chứng (log, chạy thử nhỏ) rồi mới thử tiếp.

### L-008 — Assumption phải thành chữ

- **Từ đâu:** seed
- **Vì sao:** assumption ngầm sống sót qua nhiều bước rồi phát nổ ở QC hoặc production.
- **Áp dụng:** mọi assumption ghi vào WORKLOG/handoff ngay lúc đặt ra; assumption sai bị phát hiện
  → trigger ghi bài học (mục trigger 3).

### L-009 — Hành động phá huỷ / ra ngoài: xác nhận từng lần

- **Từ đâu:** seed
- **Vì sao:** xoá dữ liệu, deploy, push, gọi API thật là thứ không rollback bằng "xin lỗi" được.
- **Áp dụng:** theo `git.md` và mục "Khi nào dừng lại để hỏi" của `kiro.md` — cho phép một lần
  không có nghĩa là cho phép mãi.

### L-010 — Nạp đúng context, không nạp cả kho

- **Từ đâu:** seed
- **Vì sao:** context thừa làm loãng chú ý → sai ngớ ngẩn ở chi tiết quan trọng.
- **Áp dụng:** đúng vai đúng bộ skill (`team.md`), đúng service đúng hồ sơ (`svc-<tên>.md`), đọc
  INDEX trước khi mở file to.
