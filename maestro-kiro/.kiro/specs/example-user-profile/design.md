# Design — Trang hồ sơ người dùng (ví dụ)

## Overview

Thêm endpoint đọc/cập nhật hồ sơ ở backend Spring Boot và một trang React tái dùng các component/hook
dùng chung (xem `inventory.md`). Ảnh đại diện: upload qua endpoint riêng, lưu URL vào `users.avatar_url`.

## Backend (Spring Boot)

- **Endpoints:**
  - `GET /api/me/profile` → `ProfileDto { displayName, avatarUrl }`
  - `PUT /api/me/profile` ← `UpdateProfileRequest { displayName }` → `ProfileDto`
- **Layering:** `ProfileController` → `ProfileService` → `UserRepository` (theo convention dự án)
- **Validation:** `@Valid`, `displayName` `@NotBlank @Size(max = 50)`
- **Errors:** trả theo `@ControllerAdvice` sẵn có (shape lỗi chuẩn của dự án)

## Frontend (React)

- **Trang:** `ProfilePage` — dùng `useCurrentUser` (hook chung) + `Card`, `Button`, `TextField` (component chung)
- **Data:** React Query — `useQuery(['profile'])`, `useMutation` cập nhật + invalidate
- **State lỗi/thành công:** dùng `useToast` (hook chung) thay vì tự viết

## Data model

- `users.display_name VARCHAR(50)`, `users.avatar_url TEXT` (migration nếu chưa có)

## Trade-offs

- Upload ảnh tách endpoint riêng (đơn giản, tái dùng) thay vì multipart trong `PUT profile`.

## Testing

- BE: test service (validation + cập nhật), test controller (200/400/401)
- FE: test form (submit hợp lệ/không hợp lệ), e2e Playwright luồng xem→sửa→lưu

## Risks

- Nơi lưu ảnh chưa chốt → mặc định lưu local, đánh dấu cần xác nhận.
