"""Pytest wrapper for the WO-001 acceptance criteria.

The shared implementation lives in acceptance_core.py so the suite also
runs without pytest via `python3 -m backend.tests.run_acceptance`.
"""
from __future__ import annotations

from .acceptance_core import run_criteria


def test_acceptance_criteria_1_to_20(workstation, tmp_path):
    client, data_dir = workstation
    run_criteria(client, data_dir, tmp_path)
