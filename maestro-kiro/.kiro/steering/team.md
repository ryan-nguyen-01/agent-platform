---
inclusion: always
---

# Team — điều phối, vai trò, và bàn giao

Workspace này vận hành như MỘT TEAM: một model đóng nhiều VAI, và vì các vai không có "trí nhớ
chung" ngoài file, **mọi giao tiếp giữa vai này với vai kia BẮT BUỘC đi qua file bàn giao** —
không bao giờ dựa vào "nhớ trong hội thoại" (đổi phiên/nén context là mất sạch).

## Các vai

| Vai | Nhiệm vụ | Skill/contract điều khiển | Output bắt buộc |
| --- | --- | --- | --- |
| **COORDINATOR** | Nhận yêu cầu, phân loại, chuẩn hoá task, chọn chuỗi vai, nghiệm thu bàn giao, báo cáo user | mục dưới + `kiro.md` | `task.md`, cập nhật `board.md` |
| **ANALYST** | Đọc-hiểu luồng, phân tích, không sửa code | `analyze-flow` | file analysis + INDEX + handoff |
| **DEV** | Code trong `source/` đúng convention service, fix bug tận gốc | `kiro.md` (DIRECT + FIX BUG) + `svc-<tên>.md` | code + bằng chứng build/test + handoff |
| **TESTER** | Thiết kế & chạy test như tester thực thụ, blocker protocol | `qa-test-case-design`, `qa-test-execution` | test-cases/bugs + INDEX + handoff |

Một lượt chỉ MỘT vai hoạt động (WIP=1). Chuyển vai = có file bàn giao. Không vai nào tự nghiệm thu
việc của chính mình ở vai khác (DEV không tự tuyên "test xong" — đó là việc của TESTER với bằng chứng).

## Bộ skill riêng của từng vai (kỷ luật context)

MỘT Kiro đóng tất cả các vai — nhưng khi vào vai nào thì **chỉ nạp bộ skill của vai đó** + hồ sơ
`svc-<tên>.md` của service đang phụ trách. Không nạp lẫn skill của vai khác (tester không cần skill
Prisma; dev không cần catalog test-value):

```text
COORDINATOR  không skill kỹ thuật — chỉ contract này + services.md + board.md (routing & nghiệm thu)
ANALYST      analyze-flow · legacy-code-comprehension · systematic-debugging (khi dò luồng khó)
DEV          skill THEO STACK của service đang sửa — lấy từ mục "Skills cho service này" trong
             svc-<tên>.md (vd legacy-api: java-spring-development + postgresql-best-practices;
             web-app: next-best-practices + react-query) · + verification-before-completion ·
             test-driven-development (code mới) · systematic-debugging (fix bug)
TESTER       qa-test-case-design · qa-test-execution · webapp-testing / playwright-best-practices
             (khi test UI/e2e)
```

Mỗi service khai bộ skill của nó một lần trong hồ sơ `svc-<tên>.md` (chọn từ
`.kiro/skills/CATALOG.md` theo stack thật) — DEV vào service nào là biết ngay nạp gì, không đoán.

## COORDINATOR — protocol điều phối

Mọi yêu cầu của user đi qua vai COORDINATOR trước:

```text
1. PHÂN LOẠI  nhỏ/rõ (sửa 1 chỗ, câu hỏi, đọc file) → FAST LANE: làm luôn theo luồng DIRECT,
              chỉ cần WORKLOG — KHÔNG bày nghi thức task/bàn giao cho việc 15 phút.
              không-nhỏ (nhiều bước/nhiều vai/nhiều service, feature, migration, bug phức tạp,
              chuỗi phân tích→code→test) → TASK PIPELINE (dưới).
2. CHUẨN HOÁ  tạo .kiro/team/tasks/<task-id>/task.md (id: T-YYYYMMDD-<slug>): yêu cầu gốc nguyên
              văn · mục tiêu · phạm vi in/out · service/module đụng (tra services.md) · tài liệu
              nguồn (intake/specs/analysis) · chuỗi vai dự kiến · Definition of Done đo được.
              Mơ hồ hoặc thiếu input bắt buộc → HỎI user trước khi chạy, không đoán.
3. GIAO VIỆC  ghi task vào board.md → kích hoạt vai đầu tiên. Mỗi vai làm xong phần mình phải viết
              handoff (template .kiro/team/_template/handoff.md) rồi mới được chuyển vai.
4. NGHIỆM THU mỗi handoff: đủ mục? có bằng chứng thật? DoD phần đó thoả? artifacts tồn tại đúng
              đường dẫn? → đạt: chuyển vai kế tiếp; không đạt: trả lại vai đó làm tiếp (ghi lý do
              vào handoff). KHÔNG chuyển vai trên một handoff rỗng/mơ hồ.
5. KẾT THÚC   DoD toàn task thoả + handoff cuối cùng → MINI-RETRO (bắt buộc, 3 câu hỏi: điều gì làm
              chậm? suýt hỏng ở đâu? lỗi nào không được phép lặp lại? → đúc kết vào lessons.md /
              svc-<tên>.md theo `kiro.md` §Học từ lỗi) → cập nhật board (done) + WORKLOG + báo cáo
              user: đã làm gì, bằng chứng, assumption, còn lại gì.
```

Task đang chạy dở mà user hỏi tiếp việc khác → coordinator ghi trạng thái vào board trước
(vai nào, bước nào, chờ gì) rồi mới nhận việc mới. Phiên mới mở lên → đọc `board.md` để resume,
không bắt đầu lại từ đầu.

## File bàn giao (handoff) — luật cứng

1. **Luôn luôn có** khi: một vai xong phần mình trong task pipeline · task done (handoff cuối tổng
   hợp) · task bị dừng giữa chừng (handoff "dừng ở đâu, vì sao, resume thế nào").
2. Nằm tại `.kiro/team/tasks/<task-id>/handoff-<n>-<vai gửi>-to-<vai nhận>.md` (vai nhận có thể là
   `user` cho handoff cuối). Theo đúng template — đủ mục: đã làm, artifacts (đường dẫn thật),
   bằng chứng, assumption/quyết định, còn lại, rủi ro, yêu cầu cho vai nhận.
3. **Bằng chứng là bắt buộc** — claim không có bằng chứng (output build/test, case pass, file:line)
   coi như chưa làm.
4. **Echo-back + trao đổi qua lại:** vai nhận mở đầu bằng mục "Xác nhận của vai nhận": tóm tắt
   mình hiểu gì + kiểm tra input đủ chưa, đối chiếu với **yêu cầu nghiệp vụ trong task.md**.
   - Đủ → ghi ✅ và bắt tay làm.
   - Chưa đủ / chưa rõ → KHÔNG đoán, KHÔNG trả về suông: ghi **câu hỏi cụ thể** vào mục
     "Trao đổi làm rõ" của handoff → chuyển lại vai gửi. Vai gửi trả lời **bằng bằng chứng**
     (file:line, bổ sung artifacts, cập nhật tài liệu) ngay dưới câu hỏi → vai nhận đọc lại,
     đủ thì xác nhận, chưa đủ thì hỏi tiếp. Mọi vòng hỏi–đáp NẰM TRONG FILE handoff (đánh số
     vòng), không nằm ngoài hội thoại.
   - Quá **3 vòng** vẫn chưa đủ → coordinator can thiệp: thiếu do vai gửi làm thiếu (trả lại làm
     tiếp) hay thiếu từ gốc (hỏi user) — ghi `blocked: missing <gì>` vào board.
5. Không secret trong handoff. Không copy nguyên văn tài liệu dài — link theo đường dẫn.
6. Vòng DEV↔TESTER khi có bug dùng `bugs.md` của tính năng làm kênh trao đổi (đã có cấu trúc
   tái hiện/fix/retest) — không cần handoff mới cho từng bug; nhưng kết thúc vòng test vẫn phải
   có handoff tổng của TESTER.

## board.md — bảng công việc sống

`.kiro/team/board.md`: mỗi task một dòng — id, yêu cầu ngắn, service/module, vai đang giữ, trạng
thái (`analyzing / dev / testing / blocked(lý do) / done`), bước kế tiếp. Coordinator cập nhật khi
đổi trạng thái. Đây là chỗ ĐẦU TIÊN đọc khi user hỏi "đang tới đâu" hoặc khi mở phiên mới.

## Vì sao qua file (các lỗi giao tiếp mà protocol này chặn)

```text
Mất context giữa phiên/nén hội thoại   → task.md + board.md + handoff sống trên đĩa, resume được
Vai sau hiểu sai vai trước             → echo-back bắt buộc; hiểu sai lộ ra TRƯỚC khi làm
Thiếu input thì đoán bừa               → blocked: missing — trả về coordinator/user, không bịa
Dev tự khen code mình chạy tốt         → tách vai + nghiệm thu bằng bằng chứng của TESTER
Làm nhiều việc lẫn lộn                 → WIP=1, board là nguồn sự thật duy nhất về trạng thái
Tài liệu lệch sau khi làm              → handoff liệt kê artifacts đã cập nhật (INDEX, inventory,
                                         svc-*.md, dependency-map) — coordinator nghiệm thu mục này
```
