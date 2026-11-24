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


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
