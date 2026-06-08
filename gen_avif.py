#!/usr/bin/env python3
"""
gen_avif — generate AVIF derivatives for every JPEG under static/.

For each `*-<width>.jpg` it writes a sibling `*-<width>.avif` (quality 63),
matching the existing webp/jpg pipeline. Idempotent: existing .avif files are
skipped, so it's safe to re-run after adding new photos.

Requires the JPEGs to be hydrated from Git LFS first:
    git lfs pull --include="*.jpg"

Usage:
    python3 gen_avif.py            # generate missing AVIFs
    python3 gen_avif.py --force    # re-encode even if .avif exists
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

REPO = Path(__file__).parent
STATIC = REPO / "static"
QUALITY = 63          # measured sweet spot: ~30% smaller than shipped webp, quality retained
SPEED = 6             # AVIF encoder effort (0=slow/smaller .. 10=fast/larger); 6 is a good balance
MIN_REAL_BYTES = 5000  # smaller than this == unhydrated LFS pointer, not a real image


def main() -> int:
    force = "--force" in sys.argv
    jpgs = sorted(STATIC.rglob("*.jpg"))
    if not jpgs:
        print("No .jpg files found under static/.")
        return 1

    made = skipped = pointers = 0
    for jpg in jpgs:
        if jpg.stat().st_size < MIN_REAL_BYTES:
            pointers += 1
            print(f"  ! POINTER (run `git lfs pull --include='*.jpg'`): {jpg.relative_to(REPO)}")
            continue

        avif = jpg.with_suffix(".avif")
        if avif.exists() and not force:
            skipped += 1
            continue

        with Image.open(jpg) as im:
            im.convert("RGB").save(avif, format="AVIF", quality=QUALITY, speed=SPEED)
        made += 1
        print(f"  + {avif.relative_to(REPO)}  ({avif.stat().st_size // 1024} KB)")

    print(f"\nDone. created={made} skipped(existing)={skipped} unhydrated_pointers={pointers}")

    # Integrity gate: one .avif per .jpg. Wiring <source> tags before this holds
    # would 404 for AVIF-capable browsers (no fallback). Caller should check exit code.
    n_jpg = sum(1 for j in jpgs if j.stat().st_size >= MIN_REAL_BYTES)
    n_avif = sum(1 for _ in STATIC.rglob("*.avif"))
    print(f"Integrity: real_jpg={n_jpg}  avif={n_avif}  ->  {'OK' if n_avif >= n_jpg else 'MISMATCH'}")
    return 0 if (pointers == 0 and n_avif >= n_jpg) else 2


if __name__ == "__main__":
    raise SystemExit(main())
