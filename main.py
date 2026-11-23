"""Write the make.fun entry text to entry.txt in the output directory.

The output directory is taken from the MAKEFUN_OUTPUT_DIR environment
variable when it is set and non-empty, otherwise it defaults to /output.
The directory is created if it does not already exist. The file is written
as UTF-8 with exactly one trailing newline.
"""

import os
import sys

TEXT = (
    "My agent checked whether the job was still running by searching for its own name. "
    "It found itself. The job had been dead for an hour."
)

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

try:
    os.makedirs(output_dir, exist_ok=True)
except OSError as exc:
    print(f"error: cannot create output directory {output_dir!r}: {exc}", file=sys.stderr)
    raise

with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
