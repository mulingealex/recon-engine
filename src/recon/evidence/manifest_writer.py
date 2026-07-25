"""
Manifest Writer.

Generates SHA-256 hashes for assessment artifacts.
"""

from pathlib import Path
from hashlib import sha256


class ManifestWriter:
    """
    Writes the assessment manifest containing SHA-256 hashes.
    """

    def __init__(self):
        """
        Initialize the manifest writer.
        """

        self._output_directory = Path("output")

        self._output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def _calculate_hash(
        self,
        file_path: Path,
    ) -> str:
        """
        Calculate the SHA-256 hash of a file.

        Parameters
        ----------
        file_path : Path
            File to hash.

        Returns
        -------
        str
            SHA-256 hash.
        """

        digest = sha256()

        with file_path.open("rb") as file:

            while True:

                chunk = file.read(8192)

                if not chunk:
                    break

                digest.update(chunk)

        return digest.hexdigest()

    def write(
        self,
        normalized_data: dict,
    ) -> dict:
        """
        Generate the SHA-256 manifest.

        Parameters
        ----------
        normalized_data : dict
            Included for interface consistency.

        Returns
        -------
        dict
            Metadata describing the generated artifact.
        """

        manifest_file = (
            self._output_directory /
            "manifest.sha256"
        )

        artifact_files = [

            "normalized.json",

            "scope-register.csv",

            "request-ledger.csv",

            "evidence-index.csv",

            "assessment-manifest.json",

            "continuity-record.md",

            "integrity-attestation.md",

        ]

        with manifest_file.open(
            mode="w",
            encoding="utf-8",
        ) as manifest:

            for artifact in artifact_files:

                artifact_path = (
                    self._output_directory /
                    artifact
                )

                if artifact_path.exists():

                    file_hash = self._calculate_hash(
                        artifact_path
                    )

                    manifest.write(
                        f"{file_hash}  {artifact}\n"
                    )

        return {
            "success": True,
            "artifact": "manifest",
            "path": str(manifest_file),
        }


def main() -> None:
    """
    Run the manifest writer.
    """

    writer = ManifestWriter()

    results = writer.write({})

    print(results)


if __name__ == "__main__":
    main()