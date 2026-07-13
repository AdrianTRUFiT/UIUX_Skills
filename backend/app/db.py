"""SQLite registry: schema, connections, and the FTS5 search index."""
from __future__ import annotations

import sqlite3
from pathlib import Path

from . import config

SCHEMA = """
CREATE TABLE IF NOT EXISTS proof_objects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    po_id TEXT UNIQUE NOT NULL,
    sha256 TEXT UNIQUE NOT NULL,
    original_filename TEXT NOT NULL,
    source_path TEXT,
    source_collection TEXT,
    repository TEXT NOT NULL DEFAULT 'Unassigned',
    size_bytes INTEGER NOT NULL,
    mime_type TEXT,
    file_ext TEXT,
    doc_type TEXT,
    imported_at TEXT NOT NULL,
    import_batch_id INTEGER,
    preserved_path TEXT NOT NULL,
    extraction_status TEXT NOT NULL,
    extraction_error TEXT,
    extracted_text TEXT,
    detected_people TEXT,
    detected_date TEXT,
    file_modified TEXT,
    topic TEXT,
    review_status TEXT NOT NULL DEFAULT 'Pending Review',
    operator_notes TEXT,
    metadata_json TEXT
);

CREATE TABLE IF NOT EXISTS import_batches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at TEXT NOT NULL,
    source_label TEXT,
    total_items INTEGER NOT NULL DEFAULT 0,
    imported INTEGER NOT NULL DEFAULT 0,
    duplicates INTEGER NOT NULL DEFAULT 0,
    errors_count INTEGER NOT NULL DEFAULT 0,
    unsupported INTEGER NOT NULL DEFAULT 0,
    manifest_json TEXT
);

CREATE TABLE IF NOT EXISTS duplicate_occurrences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    po_id TEXT NOT NULL,
    original_filename TEXT NOT NULL,
    source_path TEXT,
    batch_id INTEGER,
    occurred_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS processing_errors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    batch_id INTEGER,
    po_id TEXT,
    filename TEXT NOT NULL,
    source_path TEXT,
    stage TEXT NOT NULL,
    message TEXT NOT NULL,
    occurred_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS classification_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    po_id TEXT NOT NULL,
    field TEXT NOT NULL,
    old_value TEXT,
    new_value TEXT,
    changed_at TEXT NOT NULL
);
"""

FTS_SCHEMA = """
CREATE VIRTUAL TABLE IF NOT EXISTS po_fts USING fts5(
    po_id UNINDEXED,
    filename,
    body,
    people,
    topic,
    notes
);
"""


def connect(path: Path | None = None) -> sqlite3.Connection:
    # Single local operator; FastAPI may service requests from worker threads.
    conn = sqlite3.connect(path or config.db_path(), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA)
    conn.executescript(FTS_SCHEMA)
    conn.commit()


def fts_upsert(conn: sqlite3.Connection, po_id: str) -> None:
    row = conn.execute(
        "SELECT po_id, original_filename, extracted_text, detected_people, topic, operator_notes"
        " FROM proof_objects WHERE po_id = ?",
        (po_id,),
    ).fetchone()
    if row is None:
        return
    conn.execute("DELETE FROM po_fts WHERE po_id = ?", (po_id,))
    conn.execute(
        "INSERT INTO po_fts (po_id, filename, body, people, topic, notes) VALUES (?, ?, ?, ?, ?, ?)",
        (
            row["po_id"],
            row["original_filename"] or "",
            row["extracted_text"] or "",
            row["detected_people"] or "",
            row["topic"] or "",
            row["operator_notes"] or "",
        ),
    )
