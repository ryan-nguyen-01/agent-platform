#!/usr/bin/env python3
"""Sinh .kiro/skills/CATALOG.md từ frontmatter của các skill.

CATALOG.md là file SINH TỰ ĐỘNG — đừng sửa tay. Nguồn sự thật là frontmatter của từng
.kiro/skills/<tên>/SKILL.md: `metadata.category` (nhóm) + `metadata.summary` (mô tả ngắn tiếng Việt).

Dùng:
  python3 scripts/build-skill-catalog.py            # sinh lại CATALOG.md
  python3 scripts/build-skill-catalog.py --check    # exit 1 nếu CATALOG.md lệch (dùng trong CI)
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.join(HERE, "..", ".kiro", "skills")
OUT = os.path.join(SKILLS, "CATALOG.md")

# Thứ tự & tiêu đề section theo category — skill có category lạ sẽ báo lỗi.
SECTIONS = [
    ("backend-java", "Backend — Java / Spring Boot"),
    ("backend-node", "Backend — Node.js"),
    ("frontend-react", "Frontend — ReactJS"),
    ("frontend-next", "Frontend — Next.js"),
    ("ui-styling", "Thư viện UI & styling"),
    ("data-orm", "Data & ORM"),
    ("auth", "Auth"),
    ("qc-testing", "QC / Testing (luồng TEST — như tester thực thụ)"),
    ("cross-cutting", "Xuyên suốt"),
]

HEADER = """<!-- FILE SINH TỰ ĐỘNG từ frontmatter của skills — ĐỪNG SỬA TAY.
     Đổi metadata.category / metadata.summary trong SKILL.md rồi chạy:
     python3 scripts/build-skill-catalog.py -->

# Danh mục skills

{n} skill how-to đã tuyển cho web full-stack: **Java/Spring Boot · Node.js · Next.js · ReactJS · thư
viện UI · database · QC/testing**. Mỗi skill là một thư mục có `SKILL.md` theo đúng format Agent
Skills của Kiro (frontmatter `name` + `description`; tài liệu phụ trong `references/`, code chạy được
trong `scripts/`, template trong `assets/`). Nạp skill liên quan trước khi viết code trong mảng đó;
bắt đầu bằng `legacy-code-comprehension` để đọc code lạ.
"""


def parse_skill(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm = m.group(1)
    get = lambda key: re.search(rf"^  {key}: (.+)$", fm, re.M)
    cat, summary = get("category"), get("summary")
    return (
        cat.group(1).strip() if cat else None,
        summary.group(1).strip().strip('"') if summary else None,
    )


def build():
    groups = {cid: [] for cid, _ in SECTIONS}
    errors = []
    for d in sorted(os.listdir(SKILLS)):
        full = os.path.join(SKILLS, d)
        if not os.path.isdir(full) or d.startswith("."):
            continue
        parsed = parse_skill(os.path.join(full, "SKILL.md"))
        if not parsed or not parsed[0] or not parsed[1]:
            errors.append(f"{d}: thiếu metadata.category hoặc metadata.summary")
            continue
        cat, summary = parsed
        if cat not in groups:
            errors.append(f"{d}: category lạ '{cat}' (hợp lệ: {', '.join(g for g, _ in SECTIONS)})")
            continue
        groups[cat].append((d, summary))
    if errors:
        print("\n".join("LỖI " + e for e in errors))
        sys.exit(1)
    n = sum(len(v) for v in groups.values())
    parts = [HEADER.format(n=n).rstrip("\n")]
    for cid, title in SECTIONS:
        if not groups[cid]:
            continue
        parts.append(f"\n## {title}\n")
        parts.append("| Skill | Dùng cho |")
        parts.append("| --- | --- |")
        for name, summary in groups[cid]:
            parts.append(f"| `{name}` | {summary} |")
    return "\n".join(parts) + "\n", n


def main():
    content, n = build()
    if "--check" in sys.argv:
        current = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if current != content:
            print("CATALOG.md lệch với frontmatter skills — chạy: python3 scripts/build-skill-catalog.py")
            sys.exit(1)
        print(f"CATALOG.md khớp ({n} skills)")
        return
    open(OUT, "w", encoding="utf-8").write(content)
    print(f"đã sinh {os.path.relpath(OUT, os.path.join(HERE, '..'))} ({n} skills)")


if __name__ == "__main__":
    main()
