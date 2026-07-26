"""
Manifest Writer.

Generates SHA-256 hashes for all assessment artifacts.
"""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


class ManifestWriter:
    """
    Generates manifest.sha256.
    """

    def __init__(self) -> None:
        self._output_directory = Path("output")
        self._output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def _calculate_hash(
        self,
        file_path: Path,
    ) -> str:

        digest = sha256()

        with file_path.open("rb") as file:

            while chunk := file.read(8192):
                digest.update(chunk)

        return digest.hexdigest()

    def write(
        self,
        normalized_data: dict,
    ) -> dict:

        manifest_file = (
            self._output_directory
            / "manifest.sha256"
        )

        artifacts = sorted(
    p
    for p in self._output_directory.rglob("*")
    if p.is_file()
    and p.name not in {
        ".gitkeep",
        "manifest.sha256",
    }
)

        with manifest_file.open(
            "w",
            encoding="utf-8",
        ) as manifest:

            for artifact in artifacts:

                relative = artifact.relative_to(
                    self._output_directory
                )

                manifest.write(
                    f"{self._calculate_hash(artifact)}  "
                    f"{relative.as_posix()}\n"
                )

        return {
            "success": True,
            "artifact": "manifest",
            "path": str(manifest_file),
        }


def main() -> None:
    writer = ManifestWriter()
    print(writer.write({}))


if __name__ == "__main__":
    main()