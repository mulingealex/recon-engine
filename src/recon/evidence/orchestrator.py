"""
Evidence Orchestrator.

Coordinates generation of all assessment evidence artifacts.
"""

from __future__ import annotations

from typing import Any

from recon.evidence.normalized_writer import NormalizedWriter
from recon.evidence.scope_register_writer import ScopeRegisterWriter
from recon.evidence.request_ledger_writer import RequestLedgerWriter
from recon.evidence.evidence_index_writer import EvidenceIndexWriter
from recon.evidence.assessment_manifest_writer import (
    AssessmentManifestWriter,
)
from recon.evidence.continuity_writer import ContinuityWriter
from recon.evidence.integrity_writer import IntegrityWriter
from recon.evidence.foothold_evidence_writer import (
    FootholdEvidenceWriter,
)
from recon.evidence.manifest_writer import ManifestWriter


class EvidenceOrchestrator:
    """
    Coordinates the generation of evidence artifacts.
    """

    def __init__(self) -> None:
        """
        Initialize all evidence writers.
        """

        self._normalized_writer = NormalizedWriter()

        self._scope_register_writer = (
            ScopeRegisterWriter()
        )

        self._request_ledger_writer = (
            RequestLedgerWriter()
        )

        self._evidence_index_writer = (
            EvidenceIndexWriter()
        )

        self._assessment_manifest_writer = (
            AssessmentManifestWriter()
        )

        self._continuity_writer = (
            ContinuityWriter()
        )

        self._integrity_writer = (
            IntegrityWriter()
        )

        self._foothold_evidence_writer = (
            FootholdEvidenceWriter()
        )

        #
        # Must execute last because it hashes
        # previously generated artifacts.
        #

        self._manifest_writer = (
            ManifestWriter()
        )

    def execute(
        self,
        normalized_data: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Generate every evidence artifact.

        Parameters
        ----------
        normalized_data : dict
            Normalized reconnaissance results.

        Returns
        -------
        dict
            Metadata describing generated artifacts.
        """

        evidence = {}

        evidence["normalized"] = (
            self._normalized_writer.write(
                normalized_data
            )
        )

        evidence["scope_register"] = (
            self._scope_register_writer.write(
                normalized_data
            )
        )

        evidence["request_ledger"] = (
            self._request_ledger_writer.write(
                normalized_data
            )
        )

        evidence["evidence_index"] = (
            self._evidence_index_writer.write(
                normalized_data
            )
        )

        evidence["assessment_manifest"] = (
            self._assessment_manifest_writer.write(
                normalized_data
            )
        )

        evidence["continuity_record"] = (
            self._continuity_writer.write(
                normalized_data
            )
        )

        evidence["integrity_attestation"] = (
            self._integrity_writer.write(
                normalized_data
            )
        )

        evidence["foothold_evidence"] = (
            self._foothold_evidence_writer.write(
                normalized_data
            )
        )

        #
        # Must execute last because it hashes
        # previously generated artifacts.
        #

        evidence["manifest"] = (
            self._manifest_writer.write(
                normalized_data
            )
        )

        return evidence


def main() -> None:
    """
    Execute the evidence subsystem independently.
    """

    sample = {
        "dns": {
            "hostname": "example.com",
            "addresses": [
                "93.184.216.34",
            ],
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
                "cloudflare",
            ]
        },
        "authenticated_http": {
            "success": True,
            "status_code": 200,
            "resource": "/user.txt",
            "body": "EXAMPLE-FLAG",
            "virtual_host": "example.local",
            "headers": {
                "Server": "Example",
                "Content-Type": "text/plain",
                "Content-Length": "12",
                "X-Runtime-Profile": "P5",
            },
            "response": {
                "target": "127.0.0.1",
                "method": "GET",
            },
        },
    }

    orchestrator = EvidenceOrchestrator()

    results = orchestrator.execute(
        sample
    )

    print(results)


if __name__ == "__main__":
    main()