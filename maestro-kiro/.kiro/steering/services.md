---
inclusion: always
---

# Sổ đăng ký service (source/ có NHIỀU service)

`source/` chứa nhiều service/app — cũ lẫn mới, FE lẫn BE. File này là **bản đồ mức hệ thống**, luôn
được nạp; chi tiết từng service nằm ở **hồ sơ riêng `svc-<tên>.md`** (nạp tự động qua `fileMatch`
khi đụng file của service đó — xem quy tắc dưới).

## Bảng service

| Service | Đường dẫn | Loại | Stack | DB / lưu trữ | Trạng thái | Gọi tới / bị gọi bởi |
| --- | --- | --- | --- | --- | --- | --- |
| <tên> | `source/<folder>/` | BE / FE / worker | <vd Spring Boot 3 / Next.js 15> | <vd Postgres `orders_db` · Redis> | active / legacy / new / migrating→<đích> | <vd → payment-api, ← web-app> |

> Trạng thái: `legacy` = con cũ đang chạy, chỉ fix không thêm feature · `new` = con mới đang xây ·
> `migrating→X` = đang được chuyển đổi sang service X (cả hai cùng chạy — ghi rõ cái nào là nguồn
> sự thật cho nghiệp vụ nào).

## Hạ tầng dùng chung

- **DB dùng chung bởi >1 service:** <bảng/schema nào — đây là coupling nguy hiểm nhất khi chuyển đổi>
- **Message/queue/event bus:** <Kafka/Rabbit/SQS — service nào phát, service nào nghe>
- **Shared package/lib nội bộ:** <đường dẫn — sửa là ảnh hưởng nhiều service>
- **Auth/session:** <SSO? token ký chung? service nào cấp>

## Quy tắc làm việc đa-service (BẮT BUỘC)

1. **Xác định service trước khi làm.** Yêu cầu không nói rõ đụng service nào → nhìn bảng trên, hỏi
   một câu ngắn nếu vẫn mơ hồ. Bug có thể nằm ở service khác với nơi lộ triệu chứng — dò theo chiều
   "gọi tới / bị gọi bởi".
2. **Mỗi service một hồ sơ** `.kiro/steering/svc-<tên>.md` (từ template `svc-_template.md`) — kiến
   trúc, convention, DB, lệnh build/run/test, inventory tái dùng RIÊNG của nó. Kiro tự nạp hồ sơ khi
   sửa file trong `source/<tên>/`; convention của service đó **thắng** mọi ghi chú chung
   (`tech.md`/`structure.md` chỉ còn là mặc định chung).
3. **Không trộn convention giữa các service.** Con cũ code kiểu cũ thì sửa theo kiểu cũ; đừng mang
   pattern con mới sang con cũ (và ngược lại) nếu không được yêu cầu.
4. **Đụng thứ dùng chung (DB chung, shared lib, event schema) → soi mọi service liên quan** trong
   bảng trước khi đổi; thay đổi contract giữa service phải được user xác nhận.
5. **Service mới xuất hiện / bị xoá / đổi trạng thái → cập nhật file này ngay** (khi quét dự án và
   khi phát hiện trong lúc làm việc). Hồ sơ `svc-*.md` lệch code thật → sửa hồ sơ.
6. Tài liệu analysis/testing đặt theo **module nghiệp vụ**; mỗi file ghi rõ nó thuộc service nào
   (một tính năng có thể xuyên nhiều service — FE + BE: ghi cả hai, trace đủ chuỗi).
