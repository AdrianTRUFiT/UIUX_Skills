"""Universal Search over the registry: phrase (FTS5), person, date, filename,
repository, and file-type filters. Results always carry enough identity to
reopen the preserved original."""
from __future__ import annotations

import sqlite3

PO_COLUMNS = (
    "po_id, original_filename, source_path, source_collection, repository,"
    " size_bytes, mime_type, file_ext, doc_type, imported_at, preserved_path,"
    " extraction_status, extraction_error, detected_people, detected_date,"
    " topic, review_status, operator_notes"
)


def _fts_quote(term: str) -> str:
    # Treat operator input as a literal phrase, not FTS query syntax.
    return '"' + term.replace('"', '""') + '"'


def search(
    conn: sqlite3.Connection,
    phrase: str | None = None,
    person: str | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
    filename: str | None = None,
    repository: str | None = None,
    file_ext: str | None = None,
    limit: int = 100,
) -> list[dict]:
    where: list[str] = []
    params: list = []

    if phrase:
        where.append(
            "p.po_id IN (SELECT po_id FROM po_fts WHERE po_fts MATCH ?)"
        )
        params.append(_fts_quote(phrase))
    if person:
        where.append("(p.detected_people LIKE ? OR p.extracted_text LIKE ?)")
        params.extend([f"%{person}%", f"%{person}%"])
    if date_from:
        where.append("(COALESCE(p.detected_date, substr(p.imported_at, 1, 10)) >= ?)")
        params.append(date_from)
    if date_to:
        where.append("(COALESCE(p.detected_date, substr(p.imported_at, 1, 10)) <= ?)")
        params.append(date_to)
    if filename:
        where.append("p.original_filename LIKE ?")
        params.append(f"%{filename}%")
    if repository:
        where.append("p.repository = ?")
        params.append(repository)
    if file_ext:
        where.append("p.file_ext = ?")
        params.append(file_ext.lower() if file_ext.startswith(".") else "." + file_ext.lower())

    sql = f"SELECT {PO_COLUMNS}, substr(COALESCE(p.extracted_text, ''), 1, 20000) AS preview FROM proof_objects p"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY p.imported_at DESC, p.po_id DESC LIMIT ?"
    params.append(limit)

    rows = conn.execute(sql, params).fetchall()
    results = []
    for row in rows:
        item = dict(row)
        text = item.get("preview") or ""
        if phrase:
            pos = text.lower().find(phrase.lower())
            if pos > 120:
                text = "…" + text[pos - 60 : pos + 340]
        item["preview"] = text[:400]
        results.append(item)
    return results
