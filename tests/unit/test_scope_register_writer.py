"""
Unit tests for the Scope Register Writer.
"""

import csv

from recon.evidence.scope_register_writer import (
    ScopeRegisterWriter,
)


def test_scope_register_writer_creates_csv(tmp_path):
    """
    The scope register writer should create a CSV
    containing the target information.
    """

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    writer = ScopeRegisterWriter()

    # Redirect output to the temporary directory
    writer._output_directory = output_dir

    sample = {
        "dns": {
            "hostname": "example.com",
            "addresses": [
                "93.184.216.34",
                "93.184.216.35",
            ],
        }
    }

    result = writer.write(sample)

    csv_file = output_dir / "scope-register.csv"

    assert csv_file.exists()

    with csv_file.open(
        newline="",
        encoding="utf-8",
    ) as file:

        rows = list(csv.reader(file))

    assert rows[0] == [
        "Target",
        "Addresses",
        "Status",
    ]

    assert rows[1] == [
        "example.com",
        "93.184.216.34;93.184.216.35",
        "In Scope",
    ]

    assert result["success"] is True
    assert result["artifact"] == "scope-register"
    assert result["path"] == str(csv_file)


def test_scope_register_writer_handles_missing_dns(tmp_path):
    """
    Missing DNS information should still produce
    a valid CSV.
    """

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    writer = ScopeRegisterWriter()
    writer._output_directory = output_dir

    result = writer.write({})

    csv_file = output_dir / "scope-register.csv"

    assert csv_file.exists()

    with csv_file.open(
        newline="",
        encoding="utf-8",
    ) as file:

        rows = list(csv.reader(file))

    assert rows[1] == [
        "",
        "",
        "In Scope",
    ]

    assert result["success"] is True