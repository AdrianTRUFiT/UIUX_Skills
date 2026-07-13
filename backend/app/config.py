"""Runtime configuration for the Evidence Intake Workstation.

Evidence safety: the data root must live outside the repository clone so
preserved originals and the registry can never be committed to GitHub.
The exact production evidence root is an open human decision; until it is
made, the default below applies and EIW_DATA_DIR overrides it.
"""
from __future__ import annotations

import os
from pathlib import Path

APP_NAME = "Evidence Intake Workstation"
VERSION = "1.0.0"

REPOSITORIES = [
    "Operator",
    "Opposing",
    "Former Counsel",
    "Court",
    "Authority",
    "Unassigned",
]

REVIEW_PENDING = "Pending Review"
REVIEW_REVIEWED = "Reviewed"

# Live mode never seeds, samples, or fabricates records.
MODE = os.environ.get("EIW_MODE", "live")

SUPPORTED_TEXT_EXTENSIONS = {
    ".pdf", ".docx", ".txt", ".csv", ".xlsx", ".eml",
}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tiff", ".tif"}
ARCHIVE_EXTENSIONS = {".zip"}
SUPPORTED_EXTENSIONS = SUPPORTED_TEXT_EXTENSIONS | IMAGE_EXTENSIONS | ARCHIVE_EXTENSIONS

MAX_EXTRACTED_CHARS = 2_000_000
MAX_ZIP_DEPTH = 2


def data_root() -> Path:
    root = os.environ.get("EIW_DATA_DIR")
    if root:
        return Path(root).expanduser().resolve()
    return (Path.home() / "EvidenceIntakeWorkstation").resolve()


def preserved_root() -> Path:
    return data_root() / "preserved"


def db_path() -> Path:
    return data_root() / "registry.db"


def ensure_dirs() -> None:
    preserved_root().mkdir(parents=True, exist_ok=True)
