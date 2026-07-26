"""
Evidence Index Writer.

Automatically indexes every generated assessment artifact.
"""

from __future__ import annotations

import csv
from datetime import UTC, datetime
from pathlib import Path


class EvidenceIndexWriter:
    """
    Writes the evidence index.
    """

    def __init__(self) -> None:
        self._output_directory = Path("output")
        self._output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def _artifact_type(
        self,
        path: Path,
    ) -> str:
        """
        Determine an artifact type from its filename.
        """

        mapping = {
            "normalized.json": "Normalized Data",
            "scope-register.csv": "Scope Register",
            "request-ledger.csv": "Request Ledger",
            "assessment-manifest.json": "Assessment Manifest",
            "continuity-record.md": "Continuity Record",
            "integrity-attestation.md": "Integrity Attestation",
            "evidence-index.csv": "Evidence Index",
            "foothold-evidence.txt": "Foothold Evidence",
            "attack-surface-report.pdf": "Assessment Report",
            "manifest.sha256": "SHA-256 Manifest",
            "test-results.xml": "Unit Test Results",
        }

        if "raw-output" in path.parts:
            return "Raw Discovery Output"

        return mapping.get(path.name, "Generated Artifact")

    def write(
        self,
        normalized_data: dict,
    ) -> dict:

        output_file = (
            self._output_directory
            / "evidence-index.csv"
        )

        timestamp = datetime.now(
            UTC
        ).isoformat(
            timespec="seconds"
        ).replace("+00:00", "Z")

        artifacts = sorted(
    p
    for p in self._output_directory.rglob("*")
    if p.is_file()
    and p.name != ".gitkeep"
)

        with output_file.open(
            "w",
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

            evidence_number = 1

            for artifact in artifacts:

                relative = artifact.relative_to(
                    self._output_directory
                )

                writer.writerow(
                    {
                        "evidence_id":
                            f"EV-{evidence_number:03d}",
                        "artifact":
                            relative.name,
                        "type":
                            self._artifact_type(relative),
                        "location":
                            f"output/{relative.as_posix()}",
                        "generated":
                            timestamp,
                    }
                )

                evidence_number += 1

        return {
            "success": True,
            "artifact": "evidence-index",
            "path": str(output_file),
        }


def main() -> None:
    writer = EvidenceIndexWriter()
    print(writer.write({}))


if __name__ == "__main__":
    main()