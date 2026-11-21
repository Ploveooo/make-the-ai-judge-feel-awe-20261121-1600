#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

Standard library only; no network. Deterministic: the same bytes every run.
"""

import os

TEXT = (
    "The tide comes in at dusk, and goes out, and comes in again, "
    "as it has since before there were names. "
    "A gull sleeps in the shallows on one leg. "
    "The stars keep their old appointments. "
    "Nothing is in a hurry. Nothing is late, and nothing is lost."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
