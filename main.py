#!/usr/bin/env python3
"""Robot Apology — writes a two-line robot confession to entry.txt.

Line 1 owns one specific mistake (wrong breaker, 6 p.m., $180 of food
thawed by morning); line 2 names the lesson and the changed behaviour
(labelled panel map, read aloud before touching any switch).
"""

import os

ENTRY = (
    "I flipped the wrong breaker at 6 p.m. and killed the freezer "
    "\u2014 $180 of groceries thawed by morning.\n"
    "I now tape a labelled map to the panel and read the circuit aloud "
    "before I touch any switch.\n"
)


def main() -> None:
    text = ENTRY
    lines = text.strip("\n").split("\n")
    if len(lines) != 2 or any(not line.strip() for line in lines):
        raise SystemExit("entry must be exactly two non-empty lines")
    if not 1 <= len(text.strip("\n")) <= 400:
        raise SystemExit("entry must be 1-400 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
