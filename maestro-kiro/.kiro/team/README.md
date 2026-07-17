# Team — task, board, bàn giao

Khu làm việc của "team" (các vai COORDINATOR / ANALYST / DEV / TESTER — contract ở
`.kiro/steering/team.md`). Giao tiếp giữa vai đi qua FILE ở đây, không qua trí nhớ hội thoại.

```text
.kiro/team/
├── board.md                    bảng công việc sống — task nào, vai nào giữ, trạng thái, bước kế
├── _template/
│   ├── task.md                 template chuẩn hoá yêu cầu (coordinator viết)
│   └── handoff.md              template file bàn giao giữa các vai
└── tasks/<task-id>/            mỗi task một folder (id: T-YYYYMMDD-<slug>)
    ├── task.md                 yêu cầu chuẩn hoá + Definition of Done
    └── handoff-<n>-<từ>-to-<đến>.md   bàn giao từng bước (cuối cùng là *-to-user.md)
```

Việc nhỏ/rõ đi FAST LANE (làm luôn + WORKLOG), không tạo task folder — nghi thức chỉ dành cho việc
nhiều bước/nhiều vai. Xem luật đầy đủ trong `team.md`.
