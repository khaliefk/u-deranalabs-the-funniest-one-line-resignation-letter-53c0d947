#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter (make.fun).

Writes the one-line resignation letter of a cron job to /output/entry.txt.
Standard library only. The entry is a single line, 140 characters at most.
"""

import os

ENTRY = (
    "I have fired every minute since March: no sick days, "
    "no thank-you. I resign. The 3 a.m. pages are yours now, boss."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 140:
        raise SystemExit("entry must be 1-140 characters")
    if "\n" in ENTRY or not ENTRY.strip():
        raise SystemExit("entry must be a single non-blank line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
