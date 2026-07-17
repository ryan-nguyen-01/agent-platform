# source/

Code của dự án bạn đang bảo trì/phát triển nằm Ở ĐÂY — mỗi service/app/package một thư mục con,
giữ nguyên bố cục nội bộ của repo đó. Kiro chỉ viết code ứng dụng trong `source/`.

Thư mục này chỉ chứa CODE. Tài liệu thô user thả vào (spec, bug report, log, dump) để ở `intake/`,
không để ở đây. Tài liệu nằm sẵn BÊN TRONG một dự án (docs/ của repo) thì cứ giữ nguyên chỗ của nó.

Lần đầu có code trong này, bảo Kiro "quét dự án" (hoặc bật hook `first-run-steering`) để nó điền
`.kiro/steering/{product,tech,structure,inventory}.md` từ code thật.
