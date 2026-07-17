# Specs (tuỳ chọn)

Spec mode là hướng **chọn-thêm** cho feature lớn hoặc mơ hồ. Mặc định là Hiểu → Làm → Ghi (xem
`.kiro/steering/kiro.md`) — chỉ dùng spec khi thay đổi quá lớn để làm một lần hoặc user yêu cầu rõ
("làm spec cho …", "spec cái này ra").

Một spec là một thư mục cho một feature, gồm ba file, viết & duyệt theo thứ tự:

```text
.kiro/specs/<ten-feature>/
  requirements.md   CÁI GÌ & VÌ SAO — user story + acceptance criteria kiểu EARS
  design.md         LÀM THẾ NÀO — kiến trúc, data model, API, component, trade-off
  tasks.md          CÁC BƯỚC — kế hoạch triển khai có thứ tự, tick được
```

## Quy trình

1. **Requirements** — viết `requirements.md` từ `_template/`. Được user OK rồi mới sang design.
2. **Design** — viết `design.md` (bám code thật + `.kiro/steering/`). Được user OK.
3. **Tasks** — chia design thành các task nhỏ, có thứ tự, kiểm chứng được trong `tasks.md`.
4. **Làm** — chạy task từ trên xuống, tick từng cái `[ ] → [x]` khi xong, và ghi task đã xong vào
   `WORKLOG.md` như mọi việc khác. Xác nhận trước các thao tác không-hoàn-tác/ra-ngoài.
5. **Test** — feature xong thì test theo luồng TEST (`.kiro/testing/`): thiết kế test case từ chính
   `requirements.md` (bảng validation là nguồn trực tiếp) rồi thực thi; bug → fix tận gốc → retest.

Giữ spec khớp thực tế: nếu design đổi giữa chừng, cập nhật `design.md`/`tasks.md` chứ đừng để lệch. Spec
của một feature đã xong là bản ghi cách nó được xây.

Bắt đầu từ template trong [`_template/`](_template/).
