"""Standalone WO-001 acceptance runner (no pytest required).

Usage:  python3 -m backend.tests.run_acceptance
Runs the twenty acceptance criteria against an isolated temporary data
root in live mode and prints one PASS line per criterion. Exit code 0
means all twenty passed.
"""
from __future__ import annotations

import os
import sys
import tempfile
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="eiw-acceptance-") as tmp:
        tmp_path = Path(tmp)
        data_dir = tmp_path / "eiw-data"
        os.environ["EIW_DATA_DIR"] = str(data_dir)
        os.environ.pop("EIW_MODE", None)

        from fastapi.testclient import TestClient

        from backend.app.main import create_app
        from backend.tests.acceptance_core import run_criteria

        client = TestClient(create_app())
        try:
            run_criteria(client, data_dir, tmp_path / "scratch")
        except AssertionError:
            traceback.print_exc()
            print("ACCEPTANCE: FAILED")
            return 1
        finally:
            client.app.state.conn.close()
    print("ACCEPTANCE: ALL 20 CRITERIA PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
