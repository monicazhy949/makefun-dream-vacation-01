"""One Emoji, One Dream Vacation entry for make.fun: one emoji for your dream vacation."""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 8

# One emoji for my dream vacation: a desert island — palm trees, sand, and nobody asking me for anything.
ENTRY = "\U0001F3DD"


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) == 1, "entry must be exactly one emoji"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
