import type {
  Classification,
  Manifest,
  ProcessingError,
  ProofObject,
  ProofObjectDetail,
  Status,
} from "./types";

async function json<T>(resp: Response): Promise<T> {
  if (!resp.ok) {
    const body = await resp.text();
    throw new Error(`${resp.status}: ${body}`);
  }
  return resp.json() as Promise<T>;
}

export function getStatus(): Promise<Status> {
  return fetch("/api/status").then((r) => json<Status>(r));
}

export function importFiles(
  files: FileList,
  repository: string,
  sourceCollection: string,
): Promise<Manifest> {
  const form = new FormData();
  for (const file of Array.from(files)) form.append("files", file);
  form.append("repository", repository);
  form.append("source_collection", sourceCollection);
  form.append("source_label", `ui-import ${new Date().toISOString()}`);
  return fetch("/api/import", { method: "POST", body: form }).then((r) =>
    json<Manifest>(r),
  );
}

export function listProofObjects(params: {
  repository?: string;
  review_status?: string;
  limit?: number;
}): Promise<ProofObject[]> {
  const query = new URLSearchParams();
  if (params.repository) query.set("repository", params.repository);
  if (params.review_status) query.set("review_status", params.review_status);
  if (params.limit) query.set("limit", String(params.limit));
  return fetch(`/api/proof-objects?${query}`).then((r) => json<ProofObject[]>(r));
}

export function getProofObject(poId: string): Promise<ProofObjectDetail> {
  return fetch(`/api/proof-objects/${poId}`).then((r) => json<ProofObjectDetail>(r));
}

export function classify(
  poId: string,
  fields: Classification,
): Promise<ProofObjectDetail> {
  return fetch(`/api/proof-objects/${poId}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(fields),
  }).then((r) => json<ProofObjectDetail>(r));
}

export function bulkClassify(
  poIds: string[],
  fields: Classification,
): Promise<{ updated: number }> {
  return fetch("/api/proof-objects/bulk-classify", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ po_ids: poIds, fields }),
  }).then((r) => json<{ updated: number }>(r));
}

export interface SearchParams {
  q?: string;
  person?: string;
  date_from?: string;
  date_to?: string;
  filename?: string;
  repository?: string;
  file_ext?: string;
}

export function search(params: SearchParams): Promise<ProofObject[]> {
  const query = new URLSearchParams();
  for (const [key, value] of Object.entries(params)) {
    if (value) query.set(key, value);
  }
  return fetch(`/api/search?${query}`).then((r) => json<ProofObject[]>(r));
}

export function getErrors(): Promise<ProcessingError[]> {
  return fetch("/api/errors").then((r) => json<ProcessingError[]>(r));
}

export function originalUrl(poId: string): string {
  return `/api/proof-objects/${poId}/original`;
}
