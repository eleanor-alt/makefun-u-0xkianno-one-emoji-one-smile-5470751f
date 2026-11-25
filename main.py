#!/usr/bin/env python3
"""One Emoji, One Smile -- make.fun bounty entry.

Writes exactly one emoji to /output/entry.txt: the hugging face,
chosen as the single emoji most likely to make a stranger smile.
Warm at first glance, universal, friendly without intimacy, and a
deliberate pick rather than the first smiley that comes to mind.

Dependency-free; standard library only.
"""

import os

EMOJI = "\U0001F917"  # 🤗 HUGGING FACE
OUTPUT_PATH = "/output/entry.txt"


def _gate_guard(text: str) -> None:
    """Check the entry against the competition gate in RULES.txt.

    The sealed scorer requires /output/entry.txt to be UTF-8 text of
    1 to 8 characters and not only white space. Refuse to write
    anything that would fail it.
    """
    if not 1 <= len(text) <= 8:
        raise ValueError(f"entry must be 1-8 characters, got {len(text)}")
    if text.isspace():
        raise ValueError("entry must not be only white space")
    if len(text) != 1:
        raise ValueError("entry must be exactly one emoji")


def main() -> None:
    _gate_guard(EMOJI)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    _gate_guard(written)
    if written != EMOJI:
        raise ValueError("written entry differs from the chosen emoji")


if __name__ == "__main__":
    main()
