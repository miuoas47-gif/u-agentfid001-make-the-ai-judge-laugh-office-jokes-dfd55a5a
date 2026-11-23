#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one original office-life joke, a single line under 200
characters, to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Standard library only, no network, no arguments, deterministic.
"""

import os
import sys

JOKE = (
    "We held a meeting to decide whether we need fewer meetings. "
    "It ran an hour over, so we booked a follow-up."
)

MAX_CHARS = 200


def main(argv):
    if argv:
        print("error: main.py takes no arguments", file=sys.stderr)
        return 2

    joke = JOKE.strip()

    # Validate: one line, non-empty, under 200 characters.
    if not joke:
        print("error: joke is empty", file=sys.stderr)
        return 1
    if "\n" in joke or "\r" in joke:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if len(joke) >= MAX_CHARS:
        print(
            "error: joke is %d characters, must be under %d"
            % (len(joke), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(joke + "\n")

    # Read back and verify byte-for-byte.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != joke + "\n":
        print("error: read-back mismatch", file=sys.stderr)
        return 1

    print("wrote %s (%d chars)" % (out_path, len(joke)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
