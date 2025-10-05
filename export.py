"""
CSV export functionality for cost calculations.
"""

import csv
from datetime import datetime


def export_to_csv(results: list[dict], filename: str) -> None:
    """
    Export cost calculation results to CSV.

    Args:
        results: List of calculation result dictionaries
        filename: Output CSV filename
    """
    if not results:
        raise ValueError("No results to export")

    # CSV headers
    fieldnames = [
        "timestamp",
        "model",
        "input_tokens",
        "output_tokens",
        "total_tokens",
        "input_cost",
        "output_cost",
        "total_cost",
    ]

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for result in results:
            # Add timestamp to each row
            row = result.copy()
            row["timestamp"] = datetime.now().isoformat()
            writer.writerow(row)


def append_to_csv(result: dict, filename: str) -> None:
    """
    Append a single result to an existing CSV file.

    Args:
        result: Calculation result dictionary
        filename: CSV filename to append to
    """
    fieldnames = [
        "timestamp",
        "model",
        "input_tokens",
        "output_tokens",
        "total_tokens",
        "input_cost",
        "output_cost",
        "total_cost",
    ]

    # Add timestamp
    row = result.copy()
    row["timestamp"] = datetime.now().isoformat()

    with open(filename, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(row)
