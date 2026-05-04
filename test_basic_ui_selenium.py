"""Pytest regression tests for ETL QA validation."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "src"))

from etl_pipeline import run_etl
from data_validation import (
    validate_required_columns,
    validate_no_null_critical_fields,
    validate_no_duplicate_transactions,
    validate_successful_payments_only,
    validate_net_amount_calculation,
    validate_kpi_summary,
)


def test_required_columns():
    transformed_df = run_etl()
    assert validate_required_columns(transformed_df)


def test_no_null_critical_fields():
    transformed_df = run_etl()
    assert validate_no_null_critical_fields(transformed_df)


def test_no_duplicate_transactions():
    transformed_df = run_etl()
    assert validate_no_duplicate_transactions(transformed_df)


def test_successful_payments_only():
    transformed_df = run_etl()
    assert validate_successful_payments_only(transformed_df)


def test_net_amount_calculation():
    transformed_df = run_etl()
    assert validate_net_amount_calculation(transformed_df)


def test_kpi_summary():
    transformed_df = run_etl()
    assert validate_kpi_summary(transformed_df)
