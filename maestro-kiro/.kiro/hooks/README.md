# Hooks

Agent hook của Kiro — hành động tự động của agent theo sự kiện. Mỗi `*.kiro.hook` là một file JSON
([định dạng hook của Kiro](https://kiro.dev/docs/hooks/)): `version`, `hooks[]` với `trigger`, `matcher`
tuỳ chọn (regex trên đường dẫn file / tool), và một `action` (prompt `agent` hoặc lệnh shell `command`).

Các hook này **mặc định tắt** (`"enabled": false`) — hành vi cốt lõi của Kiro (worklog, convention,
tái dùng inventory) đã được steering (luôn bật) bảo đảm, nên hook chỉ là *tự động hoá tuỳ chọn* bạn bật
khi cần. Bật hook từ UI của Kiro, hoặc đặt `"enabled": true` trong file.

| Hook | Trigger | Làm gì |
|------|---------|--------|
| `first-run-steering` | `SessionStart` | Quét repo điền steering còn trống (một lần) |
| `worklog-on-stop` | `Stop` | Đảm bảo có mục WORKLOG.md sau lượt có đổi file |
| `backend-convention-check` | `PostFileSave` (`.java`) | Tự soi file Java/Spring vừa lưu theo convention |
| `frontend-convention-check` | `PostFileSave` (`.ts/.tsx/.js/.jsx`) | Tự soi file FE/Node vừa lưu theo convention |
| `inventory-on-new-shared` | `PostFileCreate` (thư mục dùng chung) | Ghi component/hook/helper chung mới vào inventory.md |

> Hook `action: agent` sẽ tạo một lượt agent (tốn token) — chỉ bật cái đáng cho luồng của bạn. Không
> hook nào chạy git (git luôn do user điều khiển, xem `steering/git.md`).
