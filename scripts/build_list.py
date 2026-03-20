#!/usr/bin/env python3
"""
Build LIST.md from local Zotero CSL JSON export (awesome-style, grouped by item type).

Requires: exports/aprt-*.csljson (run Zotero export into exports/ first; exports/ is gitignored).

Usage:
  python scripts/build_list.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPORTS = ROOT / "exports"
OUT = ROOT / "LIST.md"

# (zotero type, section title) — GitHub TOC uses auto-generated heading anchors
TYPE_SECTIONS = [
    ("report", "Reports and specifications"),
    ("webpage", "Web and specifications"),
    ("article", "Articles and preprints"),
    ("article-journal", "Journal articles"),
    ("paper-conference", "Conference papers"),
    ("post", "Posts"),
    ("software", "Software and tools"),
]


def pick_csljson() -> Path:
    files = sorted(EXPORTS.glob("aprt-*.csljson"))
    if not files:
        raise SystemExit(f"No aprt-*.csljson in {EXPORTS}. Export Zotero to exports/ first.")
    return files[-1]


def one_line_abstract(s: str | None, max_len: int = 200) -> str:
    if not s:
        return ""
    s = re.sub(r"\s+", " ", s.strip())
    if len(s) > max_len:
        s = s[: max_len - 1].rsplit(" ", 1)[0] + "…"
    return s


def main() -> None:
    path = pick_csljson()
    items: list[dict] = json.loads(path.read_text(encoding="utf-8"))
    by_type: dict[str, list[dict]] = {}
    for it in items:
        t = it.get("type") or "unknown"
        by_type.setdefault(t, []).append(it)

    lines: list[str] = [
        "# akzept — curated list",
        "",
        f"> Generated from `{path.name}` ({len(items)} items). Regenerate: `python scripts/build_list.py`",
        "",
        "[Zotero library (aprt)](https://www.zotero.org/groups/6473906/aprt)",
        "",
        "## Contents",
        "",
    ]
    def slug(title: str) -> str:
        s = title.lower().replace(" ", "-")
        return re.sub(r"[^a-z0-9-]", "", s)

    for typ, title in TYPE_SECTIONS:
        if by_type.get(typ):
            lines.append(f"- [{title}](#{slug(title)})")
    lines.append("")
    lines.append("---")
    lines.append("")

    for typ, title in TYPE_SECTIONS:
        bucket = by_type.get(typ)
        if not bucket:
            continue
        lines.append(f"## {title}")
        lines.append("")
        bucket.sort(key=lambda x: (x.get("title") or "").lower())
        for it in bucket:
            title_text = it.get("title") or "(untitled)"
            url = it.get("URL") or it.get("url") or ""
            if url:
                line = f"- [{title_text}]({url})"
            else:
                line = f"- {title_text}"
            abst = one_line_abstract(it.get("abstract"))
            if abst:
                line += f" — {abst.rstrip('.')}"
                if not line.endswith("."):
                    line += "."
            lines.append(line)
        lines.append("")

    OUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({len(items)} items from {path.name})")


if __name__ == "__main__":
    main()
