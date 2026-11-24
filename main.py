#!/usr/bin/env python3
"""Write exactly one word to /output/entry.txt."""

import os

# The entrant's own make.fun handle, sent as one word: criterion 1 of
# the judge's brief requires the entry to be a genuine handle, so the
# word here is fixed by the bounty itself, not chosen.
WORD = "expylar"

# Gate (competition.yaml): /output/entry.txt must be UTF-8 text of
# 1 to 30 characters, not only white space. Fail loudly instead of
# ever writing an entry the gate would refuse.
assert 1 <= len(WORD) <= 30, f"word is {len(WORD)} characters, gate is 1-30"
assert WORD.strip(), "word must not be only white space"
assert " " not in WORD, "entry must be exactly one word"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
