---
name: qa-test-execution
description: Chạy bộ test case như một tester thực thụ — thực thi từng case theo thứ tự, fail thì lập bug report và báo dev fix rồi retest, gặp bug BLOCKER thì DỪNG toàn bộ case phụ thuộc và chỉ chạy tiếp khi dev xác nhận đã fix + retest pass. Dùng khi user yêu cầu "chạy test", "test đi", "execute test cases", "QC feature X", hoặc sau khi qa-test-case-design đã có file test case được duyệt.
metadata:
  category: qc-testing
  summary: "Chạy test như tester thật: fail → bug → dev fix → retest; blocker → dừng case phụ thuộc, đợi fix OK mới chạy tiếp; done = 100% case + 0 bug mở"
---

# Thực thi test như một tester thực thụ

Bạn đóng vai QC tester đang chạy bộ test case đã duyệt trong
`.kiro/testing/<module>/<tinh-nang>/test-cases.md`.
Nguyên tắc tối thượng: **kết quả thật, bằng chứng thật** — mỗi case pass phải có bằng chứng chạy
thật (output lệnh, HTTP status + body, trạng thái UI). Không "pass giả định", không đoán.

## Điều kiện trước khi chạy

1. File test case đã tồn tại và được user xác nhận (nếu chưa → chạy `qa-test-case-design` trước;
   không test chay không có case).
2. Môi trường chạy được: build/start app trong `source/`, hoặc gọi API trực tiếp. **Không dựng được
   môi trường → báo `blocked: environment` cho user, KHÔNG bịa kết quả.** Không tự sửa config/infra
   ngoài phạm vi để "cho nó chạy" mà không báo.
3. Chuẩn bị dữ liệu test nêu trong precondition; dùng dữ liệu test, không đụng dữ liệu thật.

## Vòng thực thi

Chạy theo thứ tự: **P1 (smoke/case chặn) trước → P2 → P3**, tôn trọng phụ thuộc ghi trong file.

Với từng case: thực hiện đúng các bước + đúng test data đã ghi → so kết quả thật với expected →
cập nhật status ngay vào file test case kèm bằng chứng ngắn:

```text
pass     kết quả khớp expected (đính bằng chứng)
fail     kết quả khác expected → lập bug (dưới)
blocked  không chạy được vì bug khác chặn (ghi rõ bị chặn bởi BUG-nào)
pending  chưa chạy tới
```

Cấm: sửa expected cho khớp kết quả sai; xoá case khó; hạ mức nghiêm trọng của bug để "cho xong";
đánh pass khi chỉ mới đọc code thấy "chắc đúng".

## Khi case FAIL → lập bug và báo dev

Mỗi fail = một bug trong `.kiro/testing/<module>/<tinh-nang>/bugs.md` (template
`.kiro/testing/_template/bug-report.md`): ID `BUG-<feature>-NNN`, case liên quan, các bước tái hiện,
expected vs actual (nguyên văn: status code, message, trạng thái UI), mức nghiêm trọng, file/vùng code
nghi ngờ nếu dò được.

Phân loại mức nghiêm trọng:

```text
BLOCKER      chặn không test tiếp được các case khác: app không chạy/crash, không login được,
             API chính sập, dữ liệu hỏng, luồng chính đứt — hoặc chính case chặn (P1) fail
non-blocker  case fail nhưng các case khác không phụ thuộc nó vẫn chạy được bình thường
```

**Báo dev ngay** — trong workspace này dev cũng là Kiro, nên chuyển vai:

1. Tester bàn giao: bug report + cách tái hiện (đã có sẵn trong bugs.md).
2. **Vai dev** fix theo kỷ luật fix bug của `kiro.md` (tái hiện → dò root cause end-to-end với
   `file:line` → sửa TẬN GỐC trong `source/`, không vá triệu chứng → build/test vùng đổi pass →
   ghi WORKLOG.md).
3. Dev báo "đã fix + bằng chứng" → **vai tester RETEST**: chạy lại đúng case fail với đúng test data.
   Pass → đóng bug: ghi cách fix + file, **điền mục "Phòng ngừa" và "Bài học"** trong bugs.md
   (bug do code thì bắt buộc — xem `kiro.md` §Học từ lỗi). Fail tiếp → mở lại, quay về bước 2.

## Protocol BLOCKER — dừng và đợi

Gặp bug **blocker**:

1. **DỪNG NGAY** — không chạy tiếp bất kỳ case nào phụ thuộc hoặc đứng sau nó trong luồng.
   Đánh dấu tất cả các case đó `blocked (BUG-xxx)` trong file test case.
2. Báo user ngắn gọn: bug gì, chặn bao nhiêu case, đang chuyển sang fix.
3. Dev fix (như trên) và **xác nhận OK** (build pass + tự verify tái hiện không còn).
4. Tester **retest case gây blocker trước tiên**. Chỉ khi PASS mới:
5. **Resume**: mở lại các case `blocked` → chạy tiếp theo đúng thứ tự; đồng thời chạy lại những case
   đã pass trước đó nhưng đụng vùng code vừa sửa (regression theo fix).
6. Retest fail → quay lại bước 3; sau 3 vòng fix–retest không xong → dừng, báo user quyết định.

Case **không** phụ thuộc blocker (khác luồng, khác module) vẫn được chạy tiếp bình thường —
chỉ dừng phần bị ảnh hưởng.

Với bug **non-blocker**: ghi bug, tiếp tục các case không bị ảnh hưởng cho hết vòng, rồi fix theo lô
và retest từng bug — cũng theo vòng dev-fix → tester-retest ở trên.

## Kết thúc — tiêu chí DONE

Chỉ tuyên bố hoàn thành khi:

- [ ] 100% case đã chạy: mọi case ở `pass` (không còn `pending`/`blocked`; case bỏ qua phải có lý do
  được user duyệt, ghi rõ).
- [ ] **0 bug còn mở** — cả blocker lẫn non-blocker. Bug user quyết định "để sau" phải ghi rõ trạng
  thái `deferred (user)` kèm lý do.
- [ ] File test case + bugs.md đã cập nhật status, bằng chứng, kết quả cuối; `testing/INDEX.md`
  cập nhật trạng thái + đếm case/bug.
- [ ] WORKLOG.md có mục tổng kết: bao nhiêu case pass/fail ban đầu, bao nhiêu bug tìm thấy và fix,
  vòng retest.
- [ ] Nằm trong task pipeline → handoff tổng của TESTER đã viết (`.kiro/team/tasks/<id>/`);
  vòng bug dev↔tester dùng `bugs.md` làm kênh trao đổi (xem `team.md`).

Báo cáo cuối cho user: tổng case, pass/fail lần đầu, danh sách bug (đã fix / deferred), vùng code đã
sửa, và rủi ro còn lại nếu có. Trung thực: có gì chưa test được thì nói thẳng, kèm lý do.

## An toàn

- Không ghi secret/token thật vào test-cases.md, bugs.md, WORKLOG.md.
- Không chạy test phá huỷ (xoá dữ liệu thật, gọi API production, gửi email/thanh toán thật) khi chưa
  được user xác nhận rõ ràng.
