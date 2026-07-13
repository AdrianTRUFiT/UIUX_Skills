import { useState } from "react";
import { originalUrl, search } from "../api";
import type { SearchParams } from "../api";
import type { ProofObject } from "../types";
import { REPOSITORIES } from "../types";

export function SearchScreen() {
  const [params, setParams] = useState<SearchParams>({});
  const [results, setResults] = useState<ProofObject[] | null>(null);
  const [busy, setBusy] = useState(false);

  const set = (key: keyof SearchParams) => (e: { target: { value: string } }) =>
    setParams((p) => ({ ...p, [key]: e.target.value || undefined }));

  const run = async () => {
    setBusy(true);
    try {
      setResults(await search(params));
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="card">
      <h2>Universal Search</h2>
      <p className="hint">
        Search extracted content and metadata across every repository. Every
        result links straight back to its preserved original.
      </p>
      <div className="form-row">
        <label className="field">
          Phrase
          <input type="text" placeholder="exact words or phrase" onChange={set("q")} data-testid="search-phrase" />
        </label>
        <label className="field">
          Person
          <input type="text" onChange={set("person")} data-testid="search-person" />
        </label>
        <label className="field">
          Filename
          <input type="text" onChange={set("filename")} data-testid="search-filename" />
        </label>
        <label className="field">
          From date
          <input type="date" onChange={set("date_from")} />
        </label>
        <label className="field">
          To date
          <input type="date" onChange={set("date_to")} />
        </label>
        <label className="field">
          Repository
          <select onChange={set("repository")} defaultValue="">
            <option value="">All repositories</option>
            {REPOSITORIES.map((r) => (
              <option key={r}>{r}</option>
            ))}
          </select>
        </label>
        <button className="primary" onClick={run} disabled={busy} data-testid="search-run">
          {busy ? "Searching…" : "Search"}
        </button>
      </div>

      {results !== null &&
        (results.length === 0 ? (
          <div className="empty">No records matched.</div>
        ) : (
          <table className="records" data-testid="search-results">
            <thead>
              <tr>
                <th>Proof Object</th>
                <th>File</th>
                <th>Repository</th>
                <th>Date</th>
                <th>Status</th>
                <th>Original</th>
              </tr>
            </thead>
            <tbody>
              {results.map((p) => (
                <tr key={p.po_id}>
                  <td>{p.po_id}</td>
                  <td>
                    {p.original_filename}
                    {p.preview && <div className="preview">{p.preview}</div>}
                  </td>
                  <td><span className="pill repo">{p.repository}</span></td>
                  <td>{p.detected_date ?? "—"}</td>
                  <td>
                    <span className={`pill ${p.extraction_status}`}>{p.extraction_status}</span>{" "}
                    <span className={`pill ${p.review_status === "Reviewed" ? "reviewed" : "pending"}`}>
                      {p.review_status}
                    </span>
                  </td>
                  <td>
                    <a
                      className="original-link"
                      href={originalUrl(p.po_id)}
                      target="_blank"
                      rel="noreferrer"
                    >
                      Open ↗
                    </a>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        ))}
    </div>
  );
}
