import { useEffect, useRef, useState } from "react";
import { getErrors, importFiles } from "../api";
import type { Manifest, ProcessingError } from "../types";
import { REPOSITORIES } from "../types";

export function IntakeScreen({ onImported }: { onImported: () => void }) {
  const fileInput = useRef<HTMLInputElement>(null);
  const [repository, setRepository] = useState<string>("Unassigned");
  const [collection, setCollection] = useState("");
  const [busy, setBusy] = useState(false);
  const [manifest, setManifest] = useState<Manifest | null>(null);
  const [errors, setErrors] = useState<ProcessingError[]>([]);
  const [failure, setFailure] = useState<string | null>(null);

  const refreshErrors = () => {
    getErrors().then(setErrors).catch(() => setErrors([]));
  };
  useEffect(refreshErrors, [manifest]);

  const runImport = async () => {
    const files = fileInput.current?.files;
    if (!files || files.length === 0) return;
    setBusy(true);
    setFailure(null);
    try {
      const result = await importFiles(files, repository, collection);
      setManifest(result);
      onImported();
      if (fileInput.current) fileInput.current.value = "";
    } catch (err) {
      setFailure(String(err));
    } finally {
      setBusy(false);
    }
  };

  return (
    <div>
      <div className="card">
        <h2>Evidence Intake</h2>
        <p className="hint">
          Select files or a ZIP production. Every original is preserved
          byte-for-byte, checkpointed with SHA-256, registered as a Proof
          Object, and placed in the Review Queue. Nothing is lost: unsupported
          or failed files are preserved and reported.
        </p>
        <div className="form-row">
          <label className="field">
            Source repository
            <select
              value={repository}
              onChange={(e) => setRepository(e.target.value)}
              data-testid="intake-repository"
            >
              {REPOSITORIES.map((r) => (
                <option key={r}>{r}</option>
              ))}
            </select>
          </label>
          <label className="field">
            Source collection (optional label)
            <input
              type="text"
              placeholder="e.g. Attorney production 2024-03"
              value={collection}
              onChange={(e) => setCollection(e.target.value)}
            />
          </label>
          <label className="field">
            Files (multiple, or a .zip archive)
            <input type="file" multiple ref={fileInput} data-testid="intake-files" />
          </label>
          <button className="primary" onClick={runImport} disabled={busy} data-testid="intake-run">
            {busy ? "Importing…" : "Import and preserve"}
          </button>
        </div>
        {failure && <div className="error-text">Import failed: {failure}</div>}
      </div>

      {manifest && (
        <div className="card" data-testid="import-summary">
          <h2>Import summary — batch #{manifest.batch_id}</h2>
          <div className="summary-grid">
            <div className="stat"><div className="num">{manifest.total_items}</div><div className="lbl">items received</div></div>
            <div className="stat"><div className="num">{manifest.imported_count}</div><div className="lbl">new Proof Objects</div></div>
            <div className="stat"><div className="num">{manifest.duplicate_count}</div><div className="lbl">duplicates detected</div></div>
            <div className="stat"><div className="num">{manifest.unsupported_count}</div><div className="lbl">unsupported / failed (preserved)</div></div>
            <div className="stat"><div className="num">{manifest.error_count}</div><div className="lbl">processing errors</div></div>
          </div>
          <p className="hint">
            <a className="original-link" href="/api/export/registry.csv">Export registry (CSV)</a>
            {"  ·  "}
            <a className="original-link" href="/api/export/registry.json">Export registry (JSON)</a>
          </p>
          {manifest.duplicates.length > 0 && (
            <p className="hint">
              Duplicates: {manifest.duplicates.map((d) => `${d.filename} = ${d.duplicate_of}`).join("; ")}
            </p>
          )}
        </div>
      )}

      <div className="card">
        <h2>Processing-error report</h2>
        <p className="hint">
          Extraction failures and unsupported types. The preserved original is
          never deleted or rejected — it stays retrievable while listed here.
        </p>
        {errors.length === 0 ? (
          <div className="empty">No processing errors recorded.</div>
        ) : (
          <table className="records" data-testid="error-report">
            <thead>
              <tr><th>File</th><th>Stage</th><th>Message</th><th>When</th></tr>
            </thead>
            <tbody>
              {errors.map((e, i) => (
                <tr key={i}>
                  <td>{e.filename}</td>
                  <td>{e.stage}</td>
                  <td className="error-text">{e.message}</td>
                  <td>{e.occurred_at}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}
