"""
Evidence Index Writer.

Writes the evidence index.
"""

from pathlib import Path
import csv
from datetime import datetime


class EvidenceIndexWriter:
    """
    Writes the evidence index.
    """

    def __init__(self):
        """
        Initialize the evidence index writer.
        """

        self._output_directory = Path("output")

        self._output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def write(self, normalized_data: dict) -> dict:
        """
        Write the evidence index.

        Parameters
        ----------
        normalized_data : dict
            Normalized reconnaissance data.

        Returns
        -------
        dict
            Metadata describing the generated artifact.
        """

        output_file = self._output_directory / "evidence-index.csv"

        timestamp = (
            datetime.utcnow()
            .isoformat(timespec="seconds") + "Z"
        )

        rows = [
            {
                "evidence_id": "EV-001",
                "artifact": "normalized.json",
                "type": "Normalized Data",
                "location": "output/normalized.json",
                "generated": timestamp,
            },
            {
                "evidence_id": "EV-002",
                "artifact": "scope-register.csv",
                "type": "Scope Register",
                "location": "output/scope-register.csv",
                "generated": timestamp,
            },
            {
                "evidence_id": "EV-003",
                "artifact": "request-ledger.csv",
                "type": "Request Ledger",
                "location": "output/request-ledger.csv",
                "generated": timestamp,
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
                    "evidence_id",
                    "artifact",
                    "type",
                    "location",
                    "generated",
                ],
            )

            writer.writeheader()

            writer.writerows(rows)

        return {
            "success": True,
            "artifact": "evidence-index",
            "path": str(output_file),
        }


def main() -> None:
    """
    Run the evidence index writer.
    """

    writer = EvidenceIndexWriter()

    sample = {}

    results = writer.write(sample)

    print(results)


if __name__ == "__main__":
    main()