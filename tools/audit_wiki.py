from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PLACEHOLDER_PATTERNS = [
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"\bFIXME\b", re.IGNORECASE),
    re.compile("\u2026"),
    re.compile("\u5f85\u8865"),
    re.compile("\u5f85\u5b8c\u5584"),
    re.compile("\u5f85\u786e\u8ba4"),
]

HTML_IMG_RE = re.compile(r"<img\b[^>]*\bsrc=[\"']([^\"']+)[\"']", re.IGNORECASE)
MD_IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
FENCED_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def is_external(target: str) -> bool:
    lowered = target.lower()
    return lowered.startswith(("http://", "https://", "mailto:", "#"))


def clean_target(target: str) -> str:
    target = target.strip().split("#", 1)[0].split("?", 1)[0]
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return target


def resolve_doc_target(md_file: Path, target: str) -> Path | None:
    target = clean_target(target)
    if not target or is_external(target):
        return None
    if target.startswith("/"):
        return ROOT / target.lstrip("/")
    return (md_file.parent / target).resolve()


def resolve_site_target(md_file: Path, target: str) -> Path | None:
    target = clean_target(target)
    if not target or is_external(target):
        return None

    rel_md = md_file.relative_to(DOCS)
    if rel_md.name == "index.md":
        output_dir = rel_md.parent
    else:
        output_dir = rel_md.with_suffix("")

    if target.startswith("/"):
        site_target = Path(target.lstrip("/"))
    else:
        site_target = (output_dir / target)

    parts: list[str] = []
    for part in site_target.parts:
        if part in ("", "."):
            continue
        if part == "..":
            if parts:
                parts.pop()
            continue
        parts.append(part)
    return DOCS.joinpath(*parts).resolve()


def text_without_code(text: str) -> str:
    text = FENCED_CODE_RE.sub("", text)
    return INLINE_CODE_RE.sub("", text)


def audit_placeholders(md_file: Path, text: str, errors: list[str]) -> None:
    stripped = text_without_code(text)
    for pattern in PLACEHOLDER_PATTERNS:
        for match in pattern.finditer(stripped):
            rel = md_file.relative_to(ROOT).as_posix()
            errors.append(f"{rel}:{line_number(stripped, match.start())}: placeholder-like text '{match.group(0)}'")


def audit_images(md_file: Path, text: str, errors: list[str]) -> None:
    stripped = text_without_code(text)
    for match in HTML_IMG_RE.finditer(stripped):
        target = match.group(1)
        resolved = resolve_site_target(md_file, target)
        if resolved is None:
            continue
        if not resolved.exists():
            rel = md_file.relative_to(ROOT).as_posix()
            errors.append(f"{rel}:{line_number(stripped, match.start())}: missing HTML image '{target}'")

    for match in MD_IMG_RE.finditer(stripped):
        target = match.group(1)
        resolved = resolve_doc_target(md_file, target)
        if resolved is None:
            continue
        if not resolved.exists():
            rel = md_file.relative_to(ROOT).as_posix()
            errors.append(f"{rel}:{line_number(stripped, match.start())}: missing markdown image '{target}'")


def audit_markdown_links(md_file: Path, text: str, errors: list[str]) -> None:
    for match in MD_LINK_RE.finditer(text):
        target = clean_target(match.group(1))
        if not target or is_external(target):
            continue
        if target.endswith(".md"):
            resolved = resolve_doc_target(md_file, target)
            if resolved is not None and not resolved.exists():
                rel = md_file.relative_to(ROOT).as_posix()
                errors.append(f"{rel}:{line_number(text, match.start())}: missing markdown link '{target}'")


def main() -> int:
    errors: list[str] = []
    markdown_files = sorted(DOCS.rglob("*.md"))
    for md_file in markdown_files:
        text = md_file.read_text(encoding="utf-8")
        audit_placeholders(md_file, text, errors)
        audit_images(md_file, text, errors)
        audit_markdown_links(md_file, text, errors)

    if errors:
        print("Yetrealm Wiki audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Yetrealm Wiki audit passed ({len(markdown_files)} markdown files checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
