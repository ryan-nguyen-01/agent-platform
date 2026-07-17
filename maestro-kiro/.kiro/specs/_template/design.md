# Design — <tên-feature>

> Bám code thật và `.kiro/steering/` (tech.md, structure.md). Tham chiếu code/utility có sẵn để tái
> dùng — đừng phát minh lại.

## Tổng quan

<cách tiếp cận trong một đoạn: xây cái gì và hình dạng lời giải>

## Kiến trúc

<các mảnh ghép với nhau ra sao; sơ đồ nhỏ hoặc luồng gạch đầu dòng. Tầng BE + component FE bị đụng.>

## Backend (Spring Boot / Node.js)

- **Endpoint / contract:** <method + path + request/response DTO>
- **Domain / entity:** <entity, quan hệ, field mới>
- **Lưu trữ:** <repository, query, migration>
- **Validation & lỗi:** <quy tắc + response lỗi, khớp shape của dự án>

## Frontend (React / Next.js)

- **Component:** <component mới/đổi, nằm đâu, tái dùng component chung nào>
- **State & data:** <thay đổi store/hook/query>
- **UI:** <primitive thư viện + cách styling>

## Data model / thay đổi schema

<bảng/cột/DTO; kế hoạch migration>

## Trade-off & phương án khác

- <quyết định> — chọn vì <lý do>; phương án <X> loại vì <lý do>

## Chiến lược test

- <unit/integration/e2e cần thêm; cái gì chứng minh mỗi requirement>

## Rủi ro

- <rủi ro> → <giảm thiểu>
