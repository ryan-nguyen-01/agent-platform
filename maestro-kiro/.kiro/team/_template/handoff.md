# Handoff <n> — <vai gửi> → <vai nhận> · <T-YYYYMMDD-slug>

- **Task:** `tasks/<task-id>/task.md` · thời điểm: <ISO>
- **Đã làm:** <việc đã hoàn thành trong phần của vai này — cụ thể, không chung chung>
- **Artifacts (đường dẫn thật):**
  - <vd `source/new-api/src/...` (code) · `.kiro/analysis/order/order-create.md` · `.kiro/testing/order/order-create/test-cases.md`>
- **Bằng chứng:** <output build/test, số case pass/tổng, file:line — claim nào không có bằng chứng
  coi như chưa làm>
- **Assumption & quyết định:** <tự quyết gì, vì sao — để vai sau và user soát lại>
- **Còn lại / ngoài phạm vi:** <chưa làm gì, vì sao>
- **Rủi ro & điểm cần chú ý:** <chỗ dễ vỡ, vùng code nhạy cảm, coupling đụng phải>
- **Yêu cầu cho vai nhận:** <việc cụ thể + tiêu chí xong của bước kế>
- **Tài liệu đã cập nhật:** <INDEX / inventory / svc-*.md / dependency-map / board — cái nào chưa
  cần thì ghi "không">

## Xác nhận của vai nhận (echo-back — điền TRƯỚC khi bắt tay làm)

- **Tôi hiểu:** <2–3 câu tóm tắt việc phải làm + tiêu chí xong, đối chiếu yêu cầu nghiệp vụ trong task.md>
- **Input:** ✅ đủ / ❓ chưa đủ → hỏi ở mục Trao đổi dưới / ⛔ `blocked: missing <gì>` (sau 3 vòng
  hỏi vẫn thiếu) → trả về coordinator, KHÔNG đoán

## Trao đổi làm rõ (hỏi–đáp giữa vai nhận ↔ vai gửi, tối đa 3 vòng)

### Vòng 1

- **[vai nhận] hỏi:** <câu hỏi cụ thể — thiếu gì, chỗ nào chưa rõ so với yêu cầu nghiệp vụ>
- **[vai gửi] đáp:** <trả lời KÈM BẰNG CHỨNG: file:line, artifact bổ sung, tài liệu đã cập nhật>

### Vòng 2 (nếu cần)

- …

> Kết thúc trao đổi: vai nhận cập nhật lại mục Input ở trên (✅/⛔). Quá 3 vòng → coordinator xử lý.
