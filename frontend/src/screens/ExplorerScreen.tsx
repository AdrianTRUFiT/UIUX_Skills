import { useCallback, useEffect, useState } from "react";
import { getProofObject, listProofObjects, originalUrl } from "../api";
import type { ProofObject, ProofObjectDetail } from "../types";
import { REPOSITORIES } from "../types";

function Detail({ poId }: { poId: string }) {
  const [detail, setDetail] = useState<ProofObjectDetail | null>(null);
  useEffect(() => {
    getProofObject(poId).then(setDetail);
  }, [poId]);
  if (!detail) return <div className="detail-panel">Loading…</div>;
  return (
    <div className="detail-panel" data-testid="explorer-detail">
      <dl>
        <dt>Proof Object</dt>
        <dd>{detail.po_id}</dd>
        <dt>SHA-256 integrity checkpoint (of acquired bytes; not proof of authorship or admissibility)</dt>
        <dd>{detail.sha256}</dd>
        <dt>Original filename</dt>
        <dd>{detail.original_filename}</dd>
        <dt>Source path</dt>
        <dd>{detail.source_path ?? "—"}</dd>
        <dt>Collection / repository</dt>
        <dd>
          {detail.source_collection ?? "—"} · <span className="pill repo">{detail.repository}</span>
        </dd>
        <dt>Imported / size / type</dt>
        <dd>
          {detail.imported_at} · {detail.size_bytes.toLocaleString()} bytes ·{" "}
          {detail.mime_type ?? detail.file_ext ?? "unknown"}
        </dd>
        <dt>Extraction</dt>
        <dd>
          <span className={`pill ${detail.extraction_status}`}>{detail.extraction_status}</span>
          {detail.extraction_error && (
            <span className="error-text"> {detail.extraction_error}</span>
          )}
        </dd>
        <dt>Review</dt>
        <dd>
          <span className={`pill ${detail.review_status === "Reviewed" ? "reviewed" : "pending"}`}>
            {detail.review_status}
          </span>
          {detail.operator_notes && <span> — {detail.operator_notes}</span>}
        </dd>
        {detail.duplicate_occurrences.length > 0 && (
          <>
            <dt>Duplicate occurrences (same bytes seen again)</dt>
            <dd>
              {detail.duplicate_occurrences
                .map((d) => `${d.original_filename} @ ${d.occurred_at}`)
                .join("; ")}
            </dd>
          </>
        )}
        {detail.classification_history.length > 0 && (
          <>
            <dt>Classification history</dt>
            <dd>
              {detail.classification_history
                .map((h) => `${h.changed_at} ${h.field}: ${h.old_value ?? "∅"} → ${h.new_value ?? "∅"}`)
                .join("; ")}
            </dd>
          </>
        )}
      </dl>
      <p>
        <a
          className="original-link"
          href={originalUrl(detail.po_id)}
          target="_blank"
          rel="noreferrer"
          data-testid="open-original"
        >
          Open preserved original ↗
        </a>
      </p>
    </div>
  );
}

export function ExplorerScreen() {
  const [repository, setRepository] = useState<string>("Operator");
  const [rows, setRows] = useState<ProofObject[]>([]);
  const [openRow, setOpenRow] = useState<string | null>(null);

  const refresh = useCallback(() => {
    listProofObjects({ repository, limit: 500 }).then(setRows);
    setOpenRow(null);
  }, [repository]);
  useEffect(refresh, [refresh]);

  return (
    <div className="card">
      <h2>Repository Explorer</h2>
      <p className="hint">
        Source repositories stay separate so Operator, Opposing, Former
        Counsel, Court, and Authority materials never mix.
      </p>
      <div className="repo-tabs" data-testid="repo-tabs">
        {REPOSITORIES.map((r) => (
          <button
            key={r}
            className={repository === r ? "active" : ""}
            onClick={() => setRepository(r)}
          >
            {r}
          </button>
        ))}
      </div>
      {rows.length === 0 ? (
        <div className="empty">No records in {repository}.</div>
      ) : (
        <table className="records" data-testid="explorer-table">
          <thead>
            <tr>
              <th>Proof Object</th>
              <th>File</th>
              <th>Type</th>
              <th>Date</th>
              <th>Extraction</th>
              <th>Review</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {rows.map((p) => (
              <>
                <tr key={p.po_id}>
                  <td>{p.po_id}</td>
                  <td>{p.original_filename}</td>
                  <td>{p.doc_type ?? p.file_ext ?? "—"}</td>
                  <td>{p.detected_date ?? "—"}</td>
                  <td><span className={`pill ${p.extraction_status}`}>{p.extraction_status}</span></td>
                  <td>
                    <span className={`pill ${p.review_status === "Reviewed" ? "reviewed" : "pending"}`}>
                      {p.review_status}
                    </span>
                  </td>
                  <td>
                    <button className="quiet" onClick={() => setOpenRow(openRow === p.po_id ? null : p.po_id)}>
                      {openRow === p.po_id ? "Close" : "Detail"}
                    </button>
                  </td>
                </tr>
                {openRow === p.po_id && (
                  <tr key={`${p.po_id}-detail`}>
                    <td colSpan={7}>
                      <Detail poId={p.po_id} />
                    </td>
                  </tr>
                )}
              </>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
