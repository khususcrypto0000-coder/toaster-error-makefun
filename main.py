"""The Funniest Toaster Error Message — make.fun one-line entry.

Writes the single final entry line to /output/entry.txt (no trailing
newline), creating the output directory if needed. Python stdlib only.

The entry is exactly 86 characters long, inside the 1-120 limit.
"""

import os

ENTRY_TEXT = (
    "ERROR 12: The bread has filed for separation. "
    "I am legally required to stay out of it."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
