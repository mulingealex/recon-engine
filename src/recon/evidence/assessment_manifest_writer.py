"""
Assessment Manifest Writer.

Writes the assessment manifest.
"""

from pathlib import Path
import json
from datetime import datetime


class AssessmentManifestWriter:
    """
    Writes the assessment manifest.
    """

    def __init__(self):
        """
        Initialize the assessment manifest writer.
        """

        self._output_directory = Path("output")

        self._output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def write(self, normalized_data: dict) -> dict:
        """
        Write the assessment manifest.

        Parameters
        ----------
        normalized_data : dict
            Normalized reconnaissance data.

        Returns
        -------
        dict
            Metadata describing the generated artifact.
        """

        output_file = (
            self._output_directory /
            "assessment-manifest.json"
        )

        dns = normalized_data.get("dns", {})

        manifest = {
            "assessment": {
                "target": dns.get(
                    "hostname",
                    "unknown"
                ),
                "generated": (
                    datetime.utcnow()
                    .isoformat(timespec="seconds")
                    + "Z"
                ),
                "engine": "Recon Engine",
                "version": "1.0.0"
            },
            "discovery": {
                "modules": [
                    "DNSDiscovery",
                    "ProbeDiscovery",
                    "ServiceDiscovery",
                    "TLSDiscovery",
                    "VirtualHostDiscovery",
                    "FingerprintDiscovery"
                ]
            },
            "tools": [
                "dig",
                "curl",
                "nmap",
                "openssl",
                "fingerprint"
            ],
            "artifacts": [
                "normalized.json",
                "scope-register.csv",
                "request-ledger.csv",
                "evidence-index.csv"
            ]
        }

        with output_file.open(
            mode="w",
            encoding="utf-8"
        ) as file:

            json.dump(
                manifest,
                file,
                indent=4
            )

        return {
            "success": True,
            "artifact": "assessment-manifest",
            "path": str(output_file)
        }


def main() -> None:
    """
    Run the assessment manifest writer.
    """

    sample = {
        "dns": {
            "hostname": "example.com"
        }
    }

    writer = AssessmentManifestWriter()

    results = writer.write(sample)

    print(results)


if __name__ == "__main__":
    main()