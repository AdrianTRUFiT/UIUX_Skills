"""Source preservation: byte-for-byte storage with SHA-256 integrity checkpoints.

The preserved original is the authority. Nothing in the pipeline may modify,
move, or delete it, and derived text never replaces it. The SHA-256 records
the acquired bytes only; it is not proof of authorship, historical
authenticity, or admissibility.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

from . import config


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_filename(name: str) -> str:
    name = Path(name).name
    name = re.sub(r"[^\w.\- ()\[\]]", "_", name, flags=re.UNICODE)
    return name or "unnamed"


def preserve(data: bytes, original_filename: str) -> tuple[str, str]:
    """Store bytes under preserved/<sha[:2]>/<sha>/<original filename>.

    Returns (sha256, preserved path relative to the data root).
    Idempotent: the same bytes always land in the same location.
    """
    digest = sha256_bytes(data)
    fname = safe_filename(original_filename)
    directory = config.preserved_root() / digest[:2] / digest
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / fname
    if not target.exists():
        tmp = directory / (fname + ".part")
        tmp.write_bytes(data)
        tmp.rename(target)
    rel = target.relative_to(config.data_root())
    return digest, str(rel)


def open_preserved(preserved_path: str) -> Path:
    """Resolve a preserved-path record to the absolute file, refusing escapes."""
    root = config.data_root()
    target = (root / preserved_path).resolve()
    if root not in target.parents and target != root:
        raise ValueError("preserved path escapes the data root")
    if not target.is_file():
        raise FileNotFoundError(preserved_path)
    return target
