# Testing — test case & bug từ tài liệu

Nơi lưu bộ test case và bug report do Kiro đóng vai QC tạo ra — mỗi module một folder, mỗi tính
năng một folder con; `INDEX.md` là mục lục sống để tìm nhanh:

```text
.kiro/testing/
├── INDEX.md                   mục lục SỐNG: module · tính năng · trạng thái · pass/tổng · bug mở
├── _template/                 test-cases.md · bug-report.md
└── <module>/                  vd order/, user/
    └── <tinh-nang>/           vd order/order-create/
        ├── test-cases.md      bộ test case từ tài liệu (hồ sơ field + case chi tiết + status)
        └── bugs.md            bug khi chạy test (tái hiện, expected vs actual, fix/retest)
```

## Quy trình (2 skill đảm nhiệm)

1. **Thiết kế** — skill `qa-test-case-design`: đọc tài liệu thật (`.kiro/specs/`, `intake/`,
   `.kiro/analysis/`, code trong `source/`) → lập hồ sơ validation từng field → sinh case theo ma trận
   (hợp lệ/biên/rỗng/sai kiểu/ký tự/độc hại; đủ AC/endpoint/màn hình) → user duyệt.
2. **Thực thi** — skill `qa-test-execution`: chạy như tester thật, cập nhật status + bằng chứng;
   fail → bug report → dev fix tận gốc → retest; **blocker → dừng các case phụ thuộc, chỉ chạy tiếp
   khi retest pass**. Done = 100% case pass + 0 bug mở.

Bắt đầu từ template trong [`_template/`](_template/). Tài liệu viết tiếng Việt; tên code/thuật ngữ
giữ tiếng Anh. Không ghi secret thật vào bất kỳ file nào ở đây.
