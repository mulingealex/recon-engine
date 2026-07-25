"""
Integrity Writer.

Writes the integrity attestation.
"""

from pathlib import Path
from datetime import datetime


class IntegrityWriter:
    """
    Writes the integrity attestation.
    """

    def __init__(self):
        """
        Initialize the integrity writer.
        """

        self._output_directory = Path("output")

        self._output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def write(self, normalized_data: dict) -> dict:
        """
        Write the integrity attestation.

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
            "integrity-attestation.md"
        )

        dns = normalized_data.get("dns", {})

        target = dns.get(
            "hostname",
            "unknown"
        )

        generated = (
            datetime.utcnow()
            .isoformat(timespec="seconds")
            + "Z"
        )

        content = f"""# Integrity Attestation

## Assessment

| Field | Value |
|-------|-------|
| Target | {target} |
| Generated | {generated} |
| Status | Complete |

---

## Integrity Statement

The reconnaissance evidence generated during this
assessment has been preserved without intentional
modification after creation.

Artifact integrity is verified using SHA-256 hashes
contained in the accompanying **manifest.sha256**
file.

---

## Evidence Included

- normalized.json
- scope-register.csv
- request-ledger.csv
- evidence-index.csv
- assessment-manifest.json
- continuity-record.md

---

## Verification Procedure

1. Open the `manifest.sha256` file.
2. Compute the SHA-256 hash of each listed artifact.
3. Compare the computed hashes against the recorded values.
4. Matching values indicate the artifacts have not changed.

---

## Attestation

This integrity attestation was generated automatically
by the reconnaissance engine as part of the evidence
preservation process.
"""

        with output_file.open(
            mode="w",
            encoding="utf-8",
        ) as file:

            file.write(content)

        return {
            "success": True,
            "artifact": "integrity-attestation",
            "path": str(output_file),
        }


def main() -> None:
    """
    Run the integrity writer.
    """

    sample = {
        "dns": {
            "hostname": "example.com"
        }
    }

    writer = IntegrityWriter()

    results = writer.write(sample)

    print(results)


if __name__ == "__main__":
    main()