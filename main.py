"""One-line review of the most boring everyday object: the rubber band.

Deterministic: no network, no randomness, no clock. Writes the review to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints it to stdout.
"""

import os
from pathlib import Path

ENTRY = (
    "The rubber band: hired to hold everything together, "
    "it slowly rots in the drawer, then snaps the one time "
    "you actually need it."
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
