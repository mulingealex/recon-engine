"""
Recon Engine.

Coordinates the complete reconnaissance workflow.
"""

from argparse import (
    ArgumentParser,
    Namespace,
)

from recon.configuration import (
    ConfigLoader,
)

from recon.discovery import (
    DiscoveryOrchestrator,
)

from recon.evidence import (
    EvidenceOrchestrator,
)

from recon.reporting import (
    ReportingOrchestrator,
)


class ReconEngine:
    """
    Coordinates the complete reconnaissance workflow.
    """

    def __init__(self):
        """
        Initialize the reconnaissance engine.
        """

        self._discovery_orchestrator = (
            DiscoveryOrchestrator()
        )

        self._evidence_orchestrator = (
            EvidenceOrchestrator()
        )

        self._reporting_orchestrator = (
            ReportingOrchestrator()
        )

    def execute(
        self,
        arguments: Namespace,
    ) -> dict:
        """
        Execute the complete reconnaissance workflow.
        """

        print("\n========================================")
        print("Recon Engine")
        print("========================================")
        print(f"Target: {arguments.target}\n")

        #
        # Discovery
        #

        print("[1/3] Running discovery...")

        normalized_data = (
            self._discovery_orchestrator.execute(
                arguments
            )
        )

        print("✓ Discovery completed.\n")

        #
        # Evidence
        #

        print("[2/3] Generating evidence...")

        evidence = (
            self._evidence_orchestrator.execute(
                normalized_data
            )
        )

        print("✓ Evidence generated.\n")

        #
        # Reporting
        #

        print("[3/3] Generating report...")

        report = (
            self._reporting_orchestrator.execute(
                normalized_data
            )
        )

        print("✓ Report generated.\n")

        return {
            "success": True,
            "target": arguments.target,
            "artifacts": {
                "normalized": evidence["normalized"]["path"],
                "scope_register": evidence["scope_register"]["path"],
                "request_ledger": evidence["request_ledger"]["path"],
                "evidence_index": evidence["evidence_index"]["path"],
                "assessment_manifest": evidence["assessment_manifest"]["path"],
                "continuity_record": evidence["continuity_record"]["path"],
                "integrity_attestation": evidence["integrity_attestation"]["path"],
                "manifest": evidence["manifest"]["path"],
                "report": report["path"],
            },
        }


def main() -> None:
    """
    Execute the reconnaissance engine.
    """

    parser = ArgumentParser(
        description="Recon Engine"
    )

    parser.add_argument(
        "target",
        help="Target hostname, host:port or URL",
    )

    arguments = parser.parse_args()

    #
    # Load configuration.
    #

    loader = ConfigLoader()

    arguments = loader.load(
        arguments
    )

    #
    # DEBUG
    #

    print(arguments)

    #
    # Execute engine.
    #

    engine = ReconEngine()

    results = engine.execute(
        arguments
    )

    print("========================================")
    print("Assessment completed successfully.")
    print("========================================\n")

    print(f"Target: {results['target']}\n")

    print("Artifacts:")

    for artifact, path in (
        results["artifacts"].items()
    ):
        print(
            f"  ✓ {artifact}: {path}"
        )

    print()


if __name__ == "__main__":
    main()