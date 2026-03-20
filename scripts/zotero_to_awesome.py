#!/usr/bin/env python3
"""
Generate awesome-style markdown from a Zotero API snapshot export.

Input: exports/aprt-snapshot-YYYY-MM-DD.json
Output: markdown with categorized entries
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def _find_repo_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / ".git").exists() or (candidate / "pyproject.toml").exists():
            return candidate
    return start.resolve()


REPO_ROOT = _find_repo_root(Path(__file__).resolve().parent)


def _pick_latest_snapshot(exports_dir: Path) -> Path | None:
    snaps = sorted(exports_dir.glob("aprt-snapshot-*.json"))
    return snaps[-1] if snaps else None


def _short_desc(item: dict, max_len: int = 180) -> str:
    data = item.get("data", {})
    text = (data.get("abstractNote") or "").strip()
    if not text:
        text = data.get("itemType", "resource")
    text = " ".join(text.split())
    if len(text) > max_len:
        return text[: max_len - 1].rstrip() + "…"
    return text


def _item_md(item: dict) -> str:
    data = item.get("data", {})
    title = (data.get("title") or "(untitled)").strip()
    url = (data.get("url") or "").strip()
    desc = _short_desc(item)
    if not desc.endswith("."):
        desc = desc + "."
    if url:
        return f"- [{title}]({url}) - {desc}"
    return f"- {title} - {desc}"


def _normalize_anchor(text: str) -> str:
    anchor = (
        text.lower()
        .replace("&", "and")
        .replace("(", "")
        .replace(")", "")
        .replace(",", "")
        .replace("/", " ")
        .replace("'", "")
    )
    return "-".join(anchor.split())


def _parse_whitelist(values: str | None, file_path: Path | None) -> set[str] | None:
    if values:
        return {v.strip() for v in values.split(",") if v.strip()}
    if file_path and file_path.exists():
        lines = [ln.strip() for ln in file_path.read_text(encoding="utf-8").splitlines()]
        return {ln for ln in lines if ln and not ln.startswith("#")}
    return None


def generate(
    snapshot_path: Path,
    out_path: Path,
    include_categories: set[str] | None = None,
    exclude_uncategorized: bool = False,
) -> None:
    data = json.loads(snapshot_path.read_text(encoding="utf-8"))
    collections = {c["data"]["key"]: c["data"]["name"] for c in data.get("collections", [])}
    grouped: dict[str, list[dict]] = defaultdict(list)

    for item in data.get("items", []):
        d = item.get("data", {})
        col_keys = d.get("collections") or []
        if col_keys:
            # Use the first collection as primary category.
            group = collections.get(col_keys[0], "Uncategorized")
        else:
            group = f"Uncategorized ({d.get('itemType', 'resource')})"
        if exclude_uncategorized and group.startswith("Uncategorized"):
            continue
        if include_categories and group not in include_categories:
            continue
        grouped[group].append(item)

    lines = [
        "# akzept",
        "",
        f"> Seeded from `{snapshot_path.relative_to(REPO_ROOT)}`.",
        "",
        "Curated references for agentic provenance R&D.",
        "",
        "## Contents",
        "",
    ]

    for group in sorted(grouped):
        anchor = _normalize_anchor(group)
        lines.append(f"- [{group}](#{anchor})")

    lines.append("")

    for group in sorted(grouped):
        lines.append(f"## {group}")
        lines.append("")
        entries = sorted(grouped[group], key=lambda i: (i.get("data", {}).get("title") or "").lower())
        for item in entries:
            lines.append(_item_md(item))
        lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_path} ({sum(len(v) for v in grouped.values())} entries)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate awesome-style markdown from Zotero snapshot")
    parser.add_argument("snapshot", nargs="?", help="Path to aprt-snapshot-*.json")
    parser.add_argument("-o", "--output", help="Output markdown path")
    parser.add_argument(
        "--include-categories",
        help="Comma-separated category names to include (exact match).",
    )
    parser.add_argument(
        "--category-whitelist-file",
        help="Path to category whitelist file (one category per line).",
    )
    parser.add_argument(
        "--exclude-uncategorized",
        action="store_true",
        help="Exclude Uncategorized groups.",
    )
    args = parser.parse_args()

    exports_dir = REPO_ROOT / "exports"
    snapshot = Path(args.snapshot) if args.snapshot else _pick_latest_snapshot(exports_dir)
    if snapshot is None:
        raise SystemExit("No snapshot found. Provide a snapshot path.")
    if not snapshot.is_absolute():
        snapshot = REPO_ROOT / snapshot
    if not snapshot.exists():
        raise SystemExit(f"Snapshot not found: {snapshot}")

    out = Path(args.output) if args.output else (REPO_ROOT / "refactor" / "output" / "awesome-seed.md")
    if not out.is_absolute():
        out = REPO_ROOT / out

    whitelist_path = Path(args.category_whitelist_file) if args.category_whitelist_file else None
    if whitelist_path and not whitelist_path.is_absolute():
        whitelist_path = REPO_ROOT / whitelist_path
    include = _parse_whitelist(args.include_categories, whitelist_path)

    generate(
        snapshot,
        out,
        include_categories=include,
        exclude_uncategorized=args.exclude_uncategorized,
    )


if __name__ == "__main__":
    main()
