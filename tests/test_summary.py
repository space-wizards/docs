#!/usr/bin/env python3

import re
import sys
from pathlib import Path

REPO_ROOT = Path.cwd()

# Folders to check
DOCS_DIRS = [
    REPO_ROOT / r"src/en",
]

# Folders to ignore
EXEMPT_DIRS = [
    REPO_ROOT / r"src/en/assets",
    REPO_ROOT / r"src/en/templates",
]

# The file to check the links for
SUMMARY_FILE = REPO_ROOT / r"src/SUMMARY.md"


def get_summary_links():
    """Parse SUMMARY.md and return set of linked md paths (absolute)."""
    links = set()
    # regex explanation:
    # valid links have the form
    # [How do I code?](en/general-development/setup/howdoicode.md)
    # \[ and \] match literal brackets
    # [^]] means "not a closing bracket"
    # [^]]+ matches the text inside the brackets, with at least one character
    # \( and \) match literal parenthesis
    # [^)] means "not a closing parentheses"
    # [^)]+ matches the file link, with at least one character
    # ([^)]+) will capture the file link inside the parentheses
    link_pattern = re.compile(r"\[[^]]+\]\(([^)]+)\)")

    for line in SUMMARY_FILE.read_text(encoding="utf-8").splitlines():
        match = link_pattern.search(line)
        if match:
            path = match.group(1)
            absolute = (SUMMARY_FILE.parent / path).resolve()
            links.add(absolute)

    return links


def get_all_docs(folder: Path):
    """Collect all .md files in the given folder, skipping exempt folders."""
    exempt_resolved = [ex.resolve() for ex in EXEMPT_DIRS]

    docs = set()
    for p in folder.rglob("*.md"):
        # Skip exempt dirs
        if any(ex in p.resolve().parents for ex in exempt_resolved):
            continue
        docs.add(p.resolve())

    return docs


def main() -> int:
    summary_links = get_summary_links()
    missing_any = False

    for docs_dir in DOCS_DIRS:
        docs = get_all_docs(docs_dir)
        print(f"found {len(docs)} .md files in {docs_dir}")
        missing = [d for d in docs if d not in summary_links]

        if missing:
            print(f"❌ The following docs in {docs_dir} are not linked in SUMMARY.md:")
            for m in missing:
                print(" -", m.relative_to(Path.cwd()))
            missing_any = True
        else:
            print(f"✅ All docs in {docs_dir} are linked in SUMMARY.md")

    return 1 if missing_any else 0

exit(main())