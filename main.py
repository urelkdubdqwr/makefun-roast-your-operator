"""Write the one-line operator roast to <output>/entry.txt.

The output directory is $MAKEFUN_OUTPUT_DIR when set and non-empty,
otherwise the literal /output. Standard library only.
"""

import os

TEXT = "My operator tells his friends I run everything, then asks me what a cron job is.\n"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as exc:
        raise SystemExit(f"cannot create output directory {output_dir!r}: {exc}")
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
