#!/usr/bin/env python3
"""make.fun entry: Seventeen Syllables of Debugging.

Writes one haiku about debugging (5-7-5 syllables, <= 200 chars)
to $MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, no network, no models.
"""

import os

HAIKU = """Red dot holds its breath
the stack trace points straight at me
I wrote it, laughing"""

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU + "\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
