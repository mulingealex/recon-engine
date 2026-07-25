"""
Request Ledger Writer.

Writes the request ledger for reconnaissance activity.
"""

from pathlib import Path
import csv
from datetime import datetime


class RequestLedgerWriter:
    """
    Writes the request ledger.
    """

    def __init__(self):
        """
        Initialize the request ledger writer.
        """

        self._output_directory = Path("output")

        self._output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def write(self, normalized_data: dict) -> dict:
        """
        Write the request ledger.

        Parameters
        ----------
        normalized_data : dict
            Normalized reconnaissance results.

        Returns
        -------
        dict
            Metadata describing the generated artifact.
        """

        output_file = self._output_directory / "request-ledger.csv"

        dns = normalized_data.get("dns", {})
        probe = normalized_data.get("probe", {})
        services = normalized_data.get("services", {})
        tls = normalized_data.get("tls", {})
        fingerprint = normalized_data.get("fingerprint", {})

        target = dns.get("hostname", "unknown")

        rows = [
            {
                "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
                "tool": "dig",
                "target": target,
                "protocol": "DNS",
                "method": "Lookup",
                "status": "Success",
                "artifact": "normalized.json",
            },
            {
                "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
                "tool": "curl",
                "target": target,
                "protocol": "HTTP",
                "method": "HEAD",
                "status": "Success" if probe.get("reachable") else "Failed",
                "artifact": "normalized.json",
            },
            {
                "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
                "tool": "nmap",
                "target": target,
                "protocol": "TCP",
                "method": "Service Scan",
                "status": (
                    "Success"
                    if services.get("services")
                    else "Failed"
                ),
                "artifact": "normalized.json",
            },
            {
                "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
                "tool": "openssl",
                "target": target,
                "protocol": "TLS",
                "method": "Certificate Inspection",
                "status": (
                    "Success"
                    if tls.get("tls_enabled")
                    else "Failed"
                ),
                "artifact": "normalized.json",
            },
            {
                "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
                "tool": "fingerprint",
                "target": target,
                "protocol": "HTTP",
                "method": "Technology Fingerprinting",
                "status": (
                    "Success"
                    if fingerprint.get("technologies")
                    else "Failed"
                ),
                "artifact": "normalized.json",
            },
        ]

        with output_file.open(
            mode="w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "timestamp",
                    "tool",
                    "target",
                    "protocol",
                    "method",
                    "status",
                    "artifact",
                ],
            )

            writer.writeheader()

            writer.writerows(rows)

        return {
            "success": True,
            "artifact": "request-ledger",
            "path": str(output_file),
        }


def main() -> None:
    """
    Run the request ledger writer as a standalone program.
    """

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
                    "service": "http",
                }
            ]
        },
        "tls": {
            "tls_enabled": True,
        },
        "fingerprint": {
            "technologies": [
                "cloudflare"
            ]
        },
    }

    writer = RequestLedgerWriter()

    results = writer.write(sample)

    print(results)


if __name__ == "__main__":
    main()