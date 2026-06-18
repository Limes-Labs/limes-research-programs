#!/usr/bin/env python3
"""Lightweight local Markdown link checker for this docs-only repo."""

from __future__ import annotations

import re
import sys
from pathlib import Path


LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def is_external(target: str) -> bool:
    return (
        target.startswith("http://")
        or target.startswith("https://")
        or target.startswith("mailto:")
        or target.startswith("#")
    )


def normalize_target(target: str) -> str:
    target = target.strip()
    if " " in target and not target.startswith("<"):
        target = target.split(" ", 1)[0]
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return target.split("#", 1)[0]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures: list[str] = []

    for markdown in sorted(root.rglob("*.md")):
        text = markdown.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw_target = match.group(1)
            target = normalize_target(raw_target)
            if not target or is_external(target):
                continue
            candidate = (markdown.parent / target).resolve()
            try:
                candidate.relative_to(root)
            except ValueError:
                failures.append(f"{markdown.relative_to(root)} links outside repo: {raw_target}")
                continue
            if not candidate.exists():
                failures.append(f"{markdown.relative_to(root)} missing link: {raw_target}")

    if failures:
        print("Markdown link check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Markdown link check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

