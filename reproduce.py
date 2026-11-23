"""Verify the research archive, then run its reproduction program."""
# SPDX-License-Identifier: MIT
import argparse
import hashlib
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT / "EdgeEnergy_Research_GitHub.zip"
DIGEST = "575ccd234f99214f5de8f399c674bdd45ba8ec21267e1d024f707f68a65f81da"


def main(argv):
    # The archive's own CLI owns option handling, help and output conventions.
    args = argparse.ArgumentParser(add_help=False)
    args.add_argument("--output", type=Path, action="append", default=[])
    args.add_argument("--only")
    known, _ = args.parse_known_args(argv)
    for output in known.output:
        if output.expanduser().resolve().is_relative_to(ROOT):
            args.error("Select an output directory outside the repository.")
    package = ARCHIVE.read_bytes()
    if hashlib.sha256(package).hexdigest() != DIGEST:
        sys.exit(f"SHA-256 mismatch for {ARCHIVE.name}. Download the original study archive.")
    if Path(tempfile.gettempdir()).resolve().is_relative_to(ROOT):
        sys.exit("Choose a system temporary directory outside the repository (TMPDIR).")
    with tempfile.TemporaryDirectory(prefix="edgeenergy-") as tmp:
        with zipfile.ZipFile(io.BytesIO(package)) as z:
            z.extractall(tmp)
        launcher = Path(tmp) / "EdgeEnergy" / "reproduce.py"
        # Preserve the caller's working directory for relative output paths.
        return subprocess.run([sys.executable, "-B", str(launcher), *argv]).returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
