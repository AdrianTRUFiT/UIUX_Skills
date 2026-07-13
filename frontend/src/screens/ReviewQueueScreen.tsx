import { useCallback, useEffect, useState } from "react";
import { bulkClassify, classify, listProofObjects } from "../api";
import type { ProofObject } from "../types";
import { REPOSITORIES } from "../types";

function RowEditor({ record, onSaved }: { record: ProofObject; onSaved: () => void }) {
  const [fields, setFields] = useState({
    repository: record.repository as string,
    doc_type: record.doc_type ?? "",
    detected_people: record.detected_people ?? "",
    detected_date: record.detected_date ?? "",
    topic: record.topic ?? "",
    operator_notes: record.operator_notes ?? "",
  });
  const [busy, setBusy] = useState(false);

  const save = async (markReviewed: boolean) => {
    setBusy(true);
    try {
      await classify(record.po_id, {
        ...fields,
        review_status: markReviewed ? "Reviewed" : undefined,
      });
      onSaved();
    } finally {
      setBusy(false);
    }
  };

  const set = (key: string) => (e: { target: { value: string } }) =>
    setFields((f) => ({ ...f, [key]: e.target.value }));

  return (
    <div className="detail-panel">
      <div className="form-row">
        <label className="field">
          Repository
          <select value={fields.repository} onChange={set("repository")}>
            {REPOSITORIES.map((r) => (
              <option key={r}>{r}</option>
            ))}
          </select>
        </label>
        <label className="field">
          Document type
          <input type="text" value={fields.doc_type} onChange={set("doc_type")} />
        </label>
        <label className="field">
          People (separate with ;)
          <input type="text" value={fields.detected_people} onChange={set("detected_people")} />
        </label>
        <label className="field">
          Date
          <input type="date" value={fields.detected_date} onChange={set("detected_date")} />
        </label>
        <label className="field">
          Topic
          <input type="text" value={fields.topic} onChange={set("topic")} />
        </label>
      </div>
      <div className="form-row">
        <label className="field" style={{ flexGrow: 1 }}>
          Operator notes
          <textarea rows={2} value={fields.operator_notes} onChange={set("operator_notes")} />
        </label>
      </div>
      <div className="form-row">
        <button className="quiet" disabled={busy} onClick={() => save(false)}>
          Save
        </button>
        <button className="primary" disabled={busy} onClick={() => save(true)} data-testid="approve">
          Save and mark reviewed
        </button>
      </div>
    </div>
  );
}

export function ReviewQueueScreen({ onChanged }: { onChanged: () => void }) {
  const [pending, setPending] = useState<ProofObject[]>([]);
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [openRow, setOpenRow] = useState<string | null>(null);
  const [bulkRepo, setBulkRepo] = useState<string>("Unassigned");
  const [busy, setBusy] = useState(false);

  const refresh = useCallback(() => {
    listProofObjects({ review_status: "Pending Review", limit: 500 }).then((rows) => {
      setPending(rows);
      setSelected(new Set());
      onChanged();
    });
  }, [onChanged]);
  useEffect(refresh, [refresh]);

  const toggle = (poId: string) => {
    setSelected((prev) => {
      const next = new Set(prev);
      if (next.has(poId)) next.delete(poId);
      else next.add(poId);
      return next;
    });
  };

  const applyBulk = async (markReviewed: boolean) => {
    if (selected.size === 0) return;
    setBusy(true);
    try {
      await bulkClassify(Array.from(selected), {
        repository: bulkRepo,
        review_status: markReviewed ? "Reviewed" : undefined,
      });
      refresh();
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="card">
      <h2>Review and Classification Queue</h2>
      <p className="hint">
        Suggested facts (people, dates from email headers) are factual hints
        only — nothing is final until the operator confirms it. Legal
        significance is never decided at intake.
      </p>

      <div className="bulk-bar">
        <span>{selected.size} selected</span>
        <label className="field">
          <select value={bulkRepo} onChange={(e) => setBulkRepo(e.target.value)} data-testid="bulk-repo">
            {REPOSITORIES.map((r) => (
              <option key={r}>{r}</option>
            ))}
          </select>
        </label>
        <button className="quiet" disabled={busy || selected.size === 0} onClick={() => applyBulk(false)} data-testid="bulk-apply">
          Apply repository
        </button>
        <button className="primary" disabled={busy || selected.size === 0} onClick={() => applyBulk(true)} data-testid="bulk-approve">
          Apply and mark reviewed
        </button>
      </div>

      {pending.length === 0 ? (
        <div className="empty">The review queue is empty.</div>
      ) : (
        <table className="records" data-testid="review-table">
          <thead>
            <tr>
              <th>
                <input
                  type="checkbox"
                  checked={selected.size === pending.length && pending.length > 0}
                  onChange={(e) =>
                    setSelected(
                      e.target.checked ? new Set(pending.map((p) => p.po_id)) : new Set(),
                    )
                  }
                />
              </th>
              <th>Proof Object</th>
              <th>File</th>
              <th>Repository</th>
              <th>Suggested people</th>
              <th>Date</th>
              <th>Extraction</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {pending.map((p) => (
              <>
                <tr key={p.po_id}>
                  <td>
                    <input
                      type="checkbox"
                      checked={selected.has(p.po_id)}
                      onChange={() => toggle(p.po_id)}
                    />
                  </td>
                  <td>{p.po_id}</td>
                  <td>{p.original_filename}</td>
                  <td><span className="pill repo">{p.repository}</span></td>
                  <td>{p.detected_people ?? "—"}</td>
                  <td>{p.detected_date ?? "—"}</td>
                  <td><span className={`pill ${p.extraction_status}`}>{p.extraction_status}</span></td>
                  <td>
                    <button
                      className="quiet"
                      onClick={() => setOpenRow(openRow === p.po_id ? null : p.po_id)}
                    >
                      {openRow === p.po_id ? "Close" : "Review"}
                    </button>
                  </td>
                </tr>
                {openRow === p.po_id && (
                  <tr key={`${p.po_id}-editor`}>
                    <td colSpan={8}>
                      <RowEditor record={p} onSaved={refresh} />
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
