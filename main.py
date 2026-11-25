"""Midnight Fridge Roast: one-line roast of a smart fridge that locks
itself after midnight. Pure Python standard library, deterministic:
every run writes the exact same single line to /output/entry.txt."""

import os

ROAST = (
    "Midnight hits and my fridge turns bouncer: "
    "'No snacks after twelve \u2014 your diet hired me, I just enforce it.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # The gate accepts 1 to 200 characters of UTF-8 text, not only
    # whitespace; refuse loudly here rather than shipping an invalid line.
    if not 1 <= len(ROAST) <= 200 or not ROAST.strip():
        raise SystemExit("roast line fails the 1-200 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")
    print(ROAST)


if __name__ == "__main__":
    main()
