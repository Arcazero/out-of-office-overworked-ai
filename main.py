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

# The gate only accepts 1-159 characters: fail loudly instead of
# silently submitting an over-long line after a future edit.
MAX_CHARS = 159


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"entry line is {len(LINE)} chars, must be 1-{MAX_CHARS}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
