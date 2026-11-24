#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.

The fortune plays on the classic "lucky numbers" slip and the agent's own
404: the page it seeks was never in its training data at all."""
import os

LINE = "Your lucky numbers are 4, 0, 4: the page you were looking for was never in your training data."

# Gate: the entry must be a single fortune-cookie line of at most 140
# characters, not only whitespace. ASCII is enforced too: the line is plain
# English, so any non-ASCII byte means the text was corrupted in editing
# and the sandbox run must fail loudly.
assert 1 <= len(LINE) <= 140 and LINE.strip() and LINE.isascii() and "\n" not in LINE, "entry line violates the 1-140 character single-line gate"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
