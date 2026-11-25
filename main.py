#!/usr/bin/env python3
"""Invent a Word We Need - make.fun entry.

Writes a single invented English word plus its one-line definition to
/output/entry.txt. Standard library only, no network, no secrets, fully
deterministic: the same bytes are written on every run.
"""

import os

ENTRY = (
    "Notifizzle (n.): the quiet letdown when your phone buzzes "
    "and it is only an update."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
