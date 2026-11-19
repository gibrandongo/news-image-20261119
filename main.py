"""Copy the entry image to the output directory.

The entry image (entry.png) is a magazine-cover summary of the world news
of Thursday 19 November 2026. This program is deterministic: it reads the
bundled image and writes an identical copy to the output directory.
"""

import os
import shutil
import sys


def output_dir(here: str) -> str:
    """Resolve the output directory from the environment, else ./out."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured:
        return configured
    return os.path.join(here, "out")


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        sys.stderr.write("entry.png not found next to main.py\n")
        return 1
    out_dir = output_dir(here)
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
