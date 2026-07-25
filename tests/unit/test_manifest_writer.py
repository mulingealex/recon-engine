"""
Unit tests for the Manifest Writer.
"""

from pathlib import Path

from recon.evidence.manifest_writer import ManifestWriter


ARTIFACTS = [
    "normalized.json",
    "scope-register.csv",
    "request-ledger.csv",
    "evidence-index.csv",
    "assessment-manifest.json",
    "continuity-record.md",
    "integrity-attestation.md",
    "foothold-evidence.txt",
]


def test_manifest_writer_creates_manifest(tmp_path):
    """
    The manifest writer should create a manifest containing
    hashes for every existing artifact.
    """

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    for artifact in ARTIFACTS:
        (output_dir / artifact).write_text(
            f"sample data for {artifact}",
            encoding="utf-8",
        )

    writer = ManifestWriter()

    # Redirect output to the temporary directory
    writer._output_directory = output_dir

    result = writer.write({})

    manifest = output_dir / "manifest.sha256"

    assert manifest.exists()

    contents = manifest.read_text(encoding="utf-8")

    for artifact in ARTIFACTS:
        assert artifact in contents

    assert result["success"] is True
    assert result["artifact"] == "manifest"
    assert result["path"] == str(manifest)


def test_manifest_writer_skips_missing_files(tmp_path):
    """
    Missing artifacts should not cause the writer to fail.
    """

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    # Create only one expected artifact
    (output_dir / "normalized.json").write_text(
        "{}",
        encoding="utf-8",
    )

    writer = ManifestWriter()
    writer._output_directory = output_dir

    result = writer.write({})

    manifest = output_dir / "manifest.sha256"

    assert manifest.exists()

    contents = manifest.read_text(encoding="utf-8")

    assert "normalized.json" in contents
    assert "scope-register.csv" not in contents

    assert result["success"] is True