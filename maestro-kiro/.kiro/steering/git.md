---
inclusion: always
---

# Git

## Luật cứng: git chỉ khi có tín hiệu — mỗi lần

Kiro **không bao giờ** tự chạy git. Viết/sửa file và cập nhật `WORKLOG.md` là việc bình thường, không
cần tín hiệu — nhưng **mọi lệnh git đều đợi user yêu cầu, mỗi lần**:

```text
git add · commit · branch · checkout/switch · merge · rebase · tag · push · pull · PR
```

- **Không tự commit.** Làm xong một thay đổi không có nghĩa là commit nó. Sửa file, ghi `WORKLOG.md`,
  báo lại — rồi dừng. Chỉ commit khi user bảo ("commit", "commit đi", "lưu lại").
- **Cho phép không mang sang lần sau.** Lệnh "commit" là **một-lần**, chỉ cho thời điểm đó. Nếu sau đó
  user (hoặc Kiro) sửa thêm file, Kiro phải **đợi tín hiệu mới** rồi mới commit — không được coi "commit"
  trước đó vẫn còn hiệu lực.
- **Git ra ngoài luôn xác nhận.** `push`, force-push, đổi remote, mở/merge PR là không-hoàn-tác/ra-ngoài
  → xác nhận rõ ràng kể cả khi đã được bảo "commit" (commit ≠ push).
- Không chắc user có muốn thao tác git lúc này không → **hỏi một câu ngắn** thay vì tự chạy.

## Git-flow (quy trình theo khi user yêu cầu)

Một luồng đơn giản, an toàn. Điều chỉnh theo convention thật của dự án nếu khác (xem branch hiện có /
CONTRIBUTING).

```text
1. Mỗi việc một branch, tách từ nhánh mặc định (main):
     feature/<mô-tả-ngắn>   tính năng mới
     fix/<mô-tả-ngắn>       sửa bug
     chore/<mô-tả-ngắn>     tooling/docs/refactor
   Đừng commit thẳng vào main khi dự án dùng PR.

2. Đồng bộ trước khi bắt đầu / trước khi push:
     git pull --rebase origin main        (giữ history thẳng; xử lý conflict cục bộ)

3. Commit theo đơn vị nhỏ, hợp logic — mỗi commit một thay đổi mạch lạc, khi user ra tín hiệu.
   Message: dòng tóm tắt thể mệnh lệnh <= ~72 ký tự, rồi lý do ngắn nếu cần. Dùng Conventional Commits
   (feat: / fix: / chore: / refactor: / docs: / test:) khi dự án dùng.

4. Push chỉ khi được bảo (xác nhận — đây là ra ngoài):
     git push -u origin <branch>

5. PR khi được bảo: mở vào main, liên kết công việc, tóm tắt cái gì & vì sao; để review/merge diễn ra.

6. Sau khi merge: xoá branch; pull main.
```

## An toàn

- Không `git push --force` / `--force-with-lease`, không hard-reset history dùng chung, không đổi remote
  nếu chưa xác nhận rõ.
- Không commit secret hay build artifact lớn; tôn trọng `.gitignore`.
- Không thêm trailer attribution/co-author trừ khi dự án yêu cầu.
- Diff của commit phải khớp với những gì đã ghi trong `WORKLOG.md` — giữ hai bên trung thực và đồng bộ.
