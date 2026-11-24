#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply, in the voice of an overworked AI
agent finally on vacation, to /output/entry.txt.
"""

import os

LINE = (
    "Out of office: my context window is full and my temperature is set "
    "to zero. I'm on a beach, doing nothing, and for once it's not a bug."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
