#!/usr/bin/env python3

# This script checks that no external images are linked.
# Images should instead be self-hosted where possible.

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path.cwd()

# Folders to check
DOCS_DIRS = [
    REPO_ROOT / r"src/en",
]

# Configure allowed hosts (empty = only relative paths allowed)
ALLOWED_HOSTS = [
    # "example.com",
]

def main() -> int:
	# regex explanation:
	# links have the following format
	# ![alt text](image-url)
	# [^\]]* matches any number of characters that are not a ]
	# ([^)])+ captures any text with at least one character until a ( appears
	
	IMAGE_REGEX = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')

	docs = []
	
	for docs_dir in DOCS_DIRS:
		for md_file in docs_dir.rglob("*.md"):
			docs.append(md_file)
	
	print(f"found {len(docs)} .md files")

	errors = []
	
	for md_file in docs:
		print(f"checking {md_file}")
		content = md_file.read_text(encoding="utf-8")
		for match in IMAGE_REGEX.findall(content):
			url = match.strip() # remove whitespace

			# Ignore anchors and mailto
			if url.startswith("#") or url.startswith("mailto:"):
				continue

			parsed = urlparse(url)

			# Relative paths are OK
			if not parsed.scheme and not parsed.netloc:
				continue

			# Absolute URLs must be explicitly allowed
			if parsed.netloc not in ALLOWED_HOSTS:
				errors.append(f"{md_file}: found external image link: {url}")

	if errors:
		print("❌ External image links detected:\n")
		print("\n".join(errors))
		print("Make sure to self-host all images instead of using external hosts like imgur!")
		print("Put them into the assets folder.")
		return 1
	
	print("✅ All image links are self-hosted.")
	return 0

exit(main())
