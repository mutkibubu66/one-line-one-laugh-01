#!/usr/bin/env python3
"""Write one original one-line joke about everyday life.

Pure standard library, no network. Writes the joke to /output/entry.txt
and prints it to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "My smart fridge just sent me a breakup text - apparently I've been "
    "sneaking out with the takeout menus behind its back."
)


def main() -> None:
    assert 1 <= len(LINE) <= 140, "entry line must be 1-140 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
