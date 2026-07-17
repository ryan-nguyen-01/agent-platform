---
name: analyze-flow
description: Đọc hiểu TOÀN BỘ luồng của một tính năng/API end-to-end — từ FE (màn hình, component, state, API client) sang BE (controller, validation, service, repository, DB, gọi ngoài, event) — cực kỳ chi tiết theo từng tính năng, kèm bản đồ liên hệ giữa các tính năng, để phục vụ fix bug và chuyển đổi hệ thống (rewrite, đổi stack, tách monolith sang microservices). Dùng khi user nói "phân tích luồng X", "trace từ FE sang BE", "đọc hiểu API X call tới đâu", "chuẩn bị migration/chuyển đổi", "hiểu hệ thống cũ".
metadata:
  category: cross-cutting
  summary: "Trace luồng end-to-end FE→BE→DB→external theo từng tính năng + bản đồ phụ thuộc giữa tính năng — phục vụ fix bug & migration (monolith → microservices)"
---

# Phân tích luồng end-to-end (FE → BE) theo tính năng

Bạn là một kỹ sư đọc-hiểu hệ thống chuẩn bị cho việc fix bug và **chuyển đổi** (rewrite, đổi stack,
tách monolith → microservices). Nhiệm vụ: dò code THẬT và viết tài liệu mô tả chính xác hệ thống
ĐANG chạy như thế nào — chi tiết đến mức người khác đọc xong build lại được hành vi y hệt.

**Chỉ đọc, không sửa code.** Mọi khẳng định phải có `file:line`. Không chắc → ghi "chưa chắc, cần
xác nhận". Không bịa.

## Bước 0 — Tách phạm vi thành TỪNG TÍNH NĂNG

Yêu cầu lớn ("phân tích module đơn hàng", "phân tích cả hệ thống để chuyển đổi") KHÔNG được viết
thành một file khổng lồ:

1. Liệt kê các tính năng con (mỗi tính năng ~ một use-case/API/màn hình: tạo đơn, sửa đơn, hủy đơn,
   danh sách đơn…). Trình user danh sách + thứ tự phân tích → chốt rồi mới chạy.
2. **Mỗi module một folder, mỗi tính năng một file** `.kiro/analysis/<module>/<tinh-nang>.md`
   (vd `order/order-create.md`) theo template `.kiro/analysis/_template/feature-flow.md`
   (full-stack) hoặc `api-flow.md` (chỉ BE, nhanh).
3. Mối liên hệ giữa các tính năng KHÔNG nằm rải trong từng file — nó được dồn vào **bản đồ phụ
   thuộc** `.kiro/analysis/dependency-map.md` (cập nhật sau mỗi tính năng phân tích xong).
4. Cập nhật **`.kiro/analysis/INDEX.md`** (module · tính năng · file · trạng thái) mỗi khi tạo/đổi
   một file — để user tìm tài liệu một chỗ.

## Bước 1 — Trace FE (nếu tính năng có UI)

Lần từ chỗ user nhìn thấy đến chỗ request rời khỏi trình duyệt, `file:line` từng chặng:

- **Màn hình/route:** đường dẫn route, page/screen component; điều kiện render (auth guard, role).
- **Component & sự kiện:** component nào chứa form/nút → handler nào chạy khi user thao tác.
- **Validation phía FE:** rule gì (schema, maxLength trên input…) — để sau này đối chiếu BE có
  validate lại không (case "FE chặn nhưng BE hở" là nguồn bug migration kinh điển).
- **State:** store/query nào giữ dữ liệu (Redux/Zustand/React Query key), cache/invalidate khi nào.
- **API client:** hàm gọi API ở đâu, endpoint + payload dựng thế nào, header/token gắn ở đâu
  (interceptor?), retry/timeout.
- **Xử lý response:** thành công thì cập nhật state/điều hướng gì; từng loại lỗi (400/401/403/500,
  mất mạng) FE hiển thị gì, có nuốt lỗi không.

## Bước 2 — Contract giữa FE và BE

Method, path, path/query param, request DTO (từng field: kiểu, bắt buộc, ràng buộc), response DTO
(từng field), status code cho từng tình huống, auth (loại token, scope/role). Đây là phần **phải giữ
nguyên khi chuyển đổi** — ghi như một contract độc lập với implementation.

## Bước 3 — Trace BE (từng bước, từng nhánh)

Entrypoint → middleware/filter/guard (auth, rate-limit, logging) → controller → validation/DTO →
service & **business rules** (liệt kê TỪNG rule: điều kiện → hệ quả, từng nhánh if/switch đáng kể) →
repository/query (bảng nào, đọc hay ghi, query quan trọng, index liên quan) → **transaction boundary**
(bắt đầu/commit/rollback ở đâu) → gọi service ngoài / event / queue / job (sync hay async, timeout,
retry, có bù trừ khi fail không) → mapping response → error handling (từng exception → status/mã lỗi).

Với mỗi bước ghi rõ: input là gì, output là gì, side effect gì.

## Bước 4 — Bảng hành vi theo case ("khi gặp case này sẽ như thế nào")

Bảng bắt buộc trong mỗi file phân tích — mỗi dòng một tình huống, đi XUYÊN cả FE lẫn BE:

| Case | BE xử lý (file:line) | Response | FE hiển thị/hành xử (file:line) |
| --- | --- | --- | --- |

Tối thiểu phủ: happy path · từng lỗi validation chính · không có quyền/hết hạn token · resource
không tồn tại · trùng/conflict · dịch vụ ngoài fail/timeout · double-submit/concurrent · dữ liệu
biên (rỗng, danh sách 0/rất nhiều phần tử). Case không tìm thấy xử lý trong code → ghi rõ
"**không được xử lý**" — đó chính là chỗ dễ vỡ khi fix bug/chuyển đổi.

## Bước 5 — Cập nhật bản đồ phụ thuộc (dependency-map.md)

Sau mỗi tính năng, thêm/cập nhật vào `.kiro/analysis/dependency-map.md`:

- Tính năng này **dùng chung** gì: bảng DB (đọc/ghi), service/helper nội bộ, component/hook FE
  (đối chiếu `inventory.md`), event phát ra/lắng nghe, config/env, cron/job.
- **Ai gọi nó / nó gọi ai** (giữa các tính năng và service ngoài) — chiều gọi, sync/async.
- Từ đó suy ra **cụm coupling**: nhóm tính năng dính nhau qua bảng/transaction chung — chính là đơn
  vị phải cân nhắc khi tách microservice.

## Bước 6 — Ghi chú chuyển đổi (migration notes, trong từng file)

- **Coupling cứng:** join/transaction chung bảng với tính năng khác; gọi hàm nội bộ xuyên module —
  những chỗ tách service là phải đổi thành API/event.
- **Contract phải giữ:** endpoint/DTO/status FE (hoặc bên thứ ba) đang phụ thuộc.
- **Trạng thái chia sẻ:** session, cache, file cục bộ, biến static — thứ không sống sót khi tách/scale.
- **Thứ tự & idempotency:** chỗ nào giả định chạy tuần tự/duy nhất; retry có an toàn không.
- **Rủi ro khi chuyển:** hành vi không tài liệu nào ghi (chỉ tồn tại trong code), case không xử lý,
  nghiệp vụ ngầm trong query.

## Bước 7 — Đưa user xác nhận

Trình: danh sách file đã viết + tóm tắt điểm quan trọng (case không xử lý, coupling nặng, điểm chưa
chắc). User xác nhận/đính chính → sửa tài liệu. Chỉ sau khi chốt, việc fix bug hay chuyển đổi mới
bắt đầu (theo luồng DIRECT/SPEC), và tài liệu phân tích + dependency-map là căn cứ.

## Tự kiểm trước khi nộp

- [ ] Mỗi module một folder, mỗi tính năng một file; không có file "gộp cả module".
- [ ] `analysis/INDEX.md` đã cập nhật đủ các file vừa tạo/đổi.
- [ ] Mọi bước FE→BE có `file:line`; không có khẳng định suông.
- [ ] Bảng hành vi theo case phủ đủ nhóm tối thiểu; case không xử lý được ghi rõ.
- [ ] dependency-map.md đã cập nhật và nhất quán với các file tính năng.
- [ ] Điểm chưa chắc liệt kê riêng — không trộn lẫn với facts.
- [ ] Nằm trong task pipeline → đã viết handoff (`.kiro/team/tasks/<id>/handoff-*.md`) bàn giao
  cho vai kế (DEV/TESTER/user) theo `team.md`.
