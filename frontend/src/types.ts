export const REPOSITORIES = [
  "Operator",
  "Opposing",
  "Former Counsel",
  "Court",
  "Authority",
  "Unassigned",
] as const;

export type Repository = (typeof REPOSITORIES)[number];

export interface ProofObject {
  po_id: string;
  original_filename: string;
  source_path: string | null;
  source_collection: string | null;
  repository: Repository;
  size_bytes: number;
  mime_type: string | null;
  file_ext: string | null;
  doc_type: string | null;
  imported_at: string;
  preserved_path: string;
  extraction_status: "extracted" | "registered" | "unsupported" | "failed";
  extraction_error: string | null;
  detected_people: string | null;
  detected_date: string | null;
  topic: string | null;
  review_status: "Pending Review" | "Reviewed";
  operator_notes: string | null;
  preview?: string;
}

export interface ProofObjectDetail extends ProofObject {
  sha256: string;
  metadata_json: string | null;
  duplicate_occurrences: {
    original_filename: string;
    source_path: string | null;
    occurred_at: string;
  }[];
  classification_history: {
    field: string;
    old_value: string | null;
    new_value: string | null;
    changed_at: string;
  }[];
}

export interface ImportRecord {
  po_id: string;
  filename: string;
  sha256: string;
  extraction_status: string;
  repository: string;
}

export interface Manifest {
  batch_id: number;
  total_items: number;
  imported_count: number;
  duplicate_count: number;
  error_count: number;
  unsupported_count: number;
  imported: ImportRecord[];
  duplicates: { filename: string; duplicate_of: string; sha256: string }[];
  errors: { filename: string; stage: string; message: string }[];
  unsupported: ImportRecord[];
}

export interface ProcessingError {
  batch_id: number | null;
  po_id: string | null;
  filename: string;
  source_path: string | null;
  stage: string;
  message: string;
  occurred_at: string;
}

export interface Status {
  app: string;
  version: string;
  mode: string;
  data_root: string;
  repositories: string[];
  counts: {
    proof_objects: number;
    pending_review: number;
    duplicates: number;
    errors: number;
  };
}

export interface Classification {
  repository?: string;
  doc_type?: string;
  source_collection?: string;
  detected_people?: string;
  detected_date?: string;
  topic?: string;
  review_status?: string;
  operator_notes?: string;
}
