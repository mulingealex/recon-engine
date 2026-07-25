"""
Unit tests for the Request Ledger Writer.
"""

import csv

from recon.evidence.request_ledger_writer import (
    RequestLedgerWriter,
)


def test_request_ledger_writer_success(tmp_path):
    """
    A successful reconnaissance run should generate
    a populated request ledger.
    """

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    writer = RequestLedgerWriter()
    writer._output_directory = output_dir

    sample = {
        "dns": {
            "hostname": "example.com",
        },
        "probe": {
            "reachable": True,
        },
        "services": {
            "services": [
                {
                    "port": 80,
                }
            ],
        },
        "tls": {
            "tls_enabled": True,
        },
        "line_protocol": {
            "reachable": True,
        },
        "virtual_hosts": {
            "virtual_hosts": [
                "example.local",
            ],
        },
        "authentication": {
            "success": True,
        },
        "authenticated_http": {
            "success": True,
        },
        "fingerprint": {
            "technologies": [
                "TransitGateway",
            ],
        },
    }

    result = writer.write(sample)

    ledger = output_dir / "request-ledger.csv"

    assert ledger.exists()

    with ledger.open(
        newline="",
        encoding="utf-8",
    ) as file:

        rows = list(csv.DictReader(file))

    #
    # Nine discovery phases should produce nine rows.
    #

    assert len(rows) == 9

    #
    # First entry (DNS)
    #

    assert rows[0]["tool"] == "dig"
    assert rows[0]["target"] == "example.com"
    assert rows[0]["status"] == "Success"

    #
    # Last entry (Fingerprint)
    #

    assert rows[-1]["tool"] == "fingerprint"
    assert rows[-1]["status"] == "Success"

    assert result["success"] is True
    assert result["artifact"] == "request-ledger"


def test_request_ledger_writer_handles_missing_data(tmp_path):
    """
    Missing discovery results should still generate
    a valid request ledger.
    """

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    writer = RequestLedgerWriter()
    writer._output_directory = output_dir

    result = writer.write({})

    ledger = output_dir / "request-ledger.csv"

    assert ledger.exists()

    with ledger.open(
        newline="",
        encoding="utf-8",
    ) as file:

        rows = list(csv.DictReader(file))

    #
    # Unknown target when DNS is absent.
    #

    assert rows[0]["target"] == "unknown"

    #
    # Probe should fail when no data exists.
    #

    assert rows[1]["status"] == "Failed"

    assert result["success"] is True