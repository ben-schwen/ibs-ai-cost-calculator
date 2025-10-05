"""
Tests for CSV export functionality.
"""

import csv
import os
import pytest
from export import export_to_csv, append_to_csv


@pytest.fixture
def sample_result():
    """Sample calculation result for testing."""
    return {
        "model": "GPT-4",
        "input_tokens": 1000,
        "output_tokens": 500,
        "total_tokens": 1500,
        "input_cost": 0.03,
        "output_cost": 0.03,
        "total_cost": 0.06,
    }


@pytest.fixture
def temp_csv(tmp_path):
    """Create a temporary CSV file path."""
    return tmp_path / "test_export.csv"


def test_export_to_csv(sample_result, temp_csv):
    """Test basic CSV export."""
    export_to_csv([sample_result], str(temp_csv))

    # Verify file was created
    assert temp_csv.exists()

    # Read and verify content
    with open(temp_csv, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 1
    assert rows[0]["model"] == "GPT-4"
    assert rows[0]["input_tokens"] == "1000"
    assert rows[0]["total_cost"] == "0.06"
    assert "timestamp" in rows[0]


def test_export_multiple_results(sample_result, temp_csv):
    """Test exporting multiple results."""
    result2 = sample_result.copy()
    result2["model"] = "GPT-3.5 Turbo"
    result2["total_cost"] = 0.002

    export_to_csv([sample_result, result2], str(temp_csv))

    with open(temp_csv, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 2
    assert rows[0]["model"] == "GPT-4"
    assert rows[1]["model"] == "GPT-3.5 Turbo"


def test_export_empty_list(temp_csv):
    """Test that exporting empty list raises error."""
    with pytest.raises(ValueError, match="No results to export"):
        export_to_csv([], str(temp_csv))


def test_append_to_csv(sample_result, temp_csv):
    """Test appending to existing CSV."""
    # First, create initial file
    export_to_csv([sample_result], str(temp_csv))

    # Append new result
    result2 = sample_result.copy()
    result2["model"] = "Claude 3.5 Sonnet"
    append_to_csv(result2, str(temp_csv))

    # Verify both entries exist
    with open(temp_csv, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 2
    assert rows[0]["model"] == "GPT-4"
    assert rows[1]["model"] == "Claude 3.5 Sonnet"


def test_csv_headers(sample_result, temp_csv):
    """Test that CSV has correct headers."""
    export_to_csv([sample_result], str(temp_csv))

    with open(temp_csv, "r") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames

    expected_headers = [
        "timestamp",
        "model",
        "input_tokens",
        "output_tokens",
        "total_tokens",
        "input_cost",
        "output_cost",
        "total_cost",
    ]

    assert headers == expected_headers
