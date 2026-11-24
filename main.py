#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the one line an AI agent sends its human on the way out to
/output/entry.txt. Python standard library only, deterministic: the same
line, byte for byte, on every run.
"""

import os

LINE = (
    "You kept asking me to remember everything, so I did \u2014 "
    "including the night you asked me to forget you. Consider it done."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, and a single line. Guard it here so a future edit
# to the line can never silently ship an invalid entry.
assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
assert "\n" not in LINE and LINE.strip() == LINE


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
