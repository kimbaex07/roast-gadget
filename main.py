#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day entry.

Writes one short roast of the TV remote to
$MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python standard library only. No network access.
"""

import os
import sys

ROAST = (
    "My TV remote only works if I aim it like a sniper, hold my breath, "
    "and apologise to the ceiling \u2014 one degree off and the volume "
    "button files for divorce."
)


def load_roast():
    """Read entry.txt beside this script if present, else use ROAST."""
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.txt")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        if text.endswith("\n"):
            text = text[:-1]
        return text
    return ROAST


def main():
    text = load_roast()
    if not text or not text.strip():
        print("error: roast is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in text:
        print("error: roast must be a single line of text", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(
            "error: roast is %d characters, must be 1-200" % len(text),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "entry.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod(out, 0o644)
    print("wrote %s (%d characters)" % (out, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
