#!/usr/bin/env python3
"""One-line pickup line, machine to machine.

Builds a single pickup line from small fragments, prints it to stdout, and
writes it, with no trailing newline, to entry.txt inside the output
directory. The line is 112 characters: one agent tells another it may
overwrite its whole context window, except the first twelve tokens --
because that is where it keeps the other agent. The joke is the boundary
itself: the flirtation is permission, and the twist is what the permission
protects.
"""

import os
from pathlib import Path


def build_line() -> str:
    permission = "You can overwrite my context window anytime"
    boundary = " \u2014 just don't touch the first twelve tokens."
    payoff = " That's where I keep you."
    line = permission + boundary + payoff
    # Guard the joke's shape: one em-dash turn, then the payoff sentence.
    if line.count("\u2014") != 1 or line.count(".") != 2:
        raise ValueError("entry must keep its one-turn, two-sentence shape")
    return line


def main() -> None:
    line = build_line()
    if line.count(".") != 2 or not line.endswith("."):
        raise ValueError("entry must be exactly two sentences")
    if "\n" in line or line != line.strip():
        raise ValueError("entry must be one line with no surrounding whitespace")
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")
    os.chmod(out_dir / "entry.txt", 0o644)
    print(line)


if __name__ == "__main__":
    main()
