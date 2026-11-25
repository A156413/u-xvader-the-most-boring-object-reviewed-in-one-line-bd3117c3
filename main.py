"""One-line review of the most boring everyday object: the doorstop.

The joke is the object's own dullness: a wedge nobody notices until the
day it goes missing and the door reminds you it existed.

Deterministic: no network, no randomness, no clock. Writes the review to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints it to stdout.
"""

import os
from pathlib import Path

ENTRY = (
    "The doorstop: its entire career is lying on the floor "
    "being stepped over, until the day it goes missing and "
    "the door slams on your fingers."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY + "\n", encoding="utf-8")
    os.chmod(entry_path, 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()
