"""Funniest Autocorrect Fail entry program.

Writes one autocorrect-fail line to MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only. The line is a single line of 1-199 characters, per the
bounty gate: UTF-8 text, not only whitespace. The fail itself is one
swapped word: "pudding" autocorrected to "poison" in a text to a new
boyfriend, and the silence afterwards is the punchline.
"""

import os
import sys

LINE = (
    "At 8:02 last night I texted my new boyfriend 'I love your cooking, "
    "especially the poison' \u2014 autocorrect swapped 'pudding' for "
    "'poison' and he hasn't replied since."
)


def main():
    # Gate: one line, 1-199 characters, UTF-8, not only whitespace.
    if not 1 <= len(LINE) <= 199:
        print(
            "entry must be 1-199 characters, got %d" % len(LINE),
            file=sys.stderr,
        )
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
