"""
Reporting Orchestrator.

Coordinates generation of the attack surface
assessment report.
"""

from __future__ import annotations

from typing import Any

from recon.reporting.executive_summary_writer import (
    ExecutiveSummaryWriter,
)
from recon.reporting.findings_writer import (
    FindingsWriter,
)
from recon.reporting.recommendations_writer import (
    RecommendationsWriter,
)
from recon.reporting.appendix_writer import (
    AppendixWriter,
)
from recon.reporting.pdf_generator import (
    PDFGenerator,
)


class ReportingOrchestrator:
    """
    Coordinates report generation.
    """

    def __init__(self) -> None:
        """
        Initialize reporting components.
        """

        self._executive_summary_writer = (
            ExecutiveSummaryWriter()
        )

        self._findings_writer = (
            FindingsWriter()
        )

        self._recommendations_writer = (
            RecommendationsWriter()
        )

        self._appendix_writer = (
            AppendixWriter()
        )

        self._pdf_generator = (
            PDFGenerator()
        )

    def execute(
        self,
        normalized_data: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Execute the reporting workflow.

        Parameters
        ----------
        normalized_data : dict
            Normalized reconnaissance results.

        Returns
        -------
        dict
            Metadata describing the generated report.
        """

        executive_summary = (
            self._executive_summary_writer.write(
                normalized_data
            )
        )

        findings = (
            self._findings_writer.write(
                normalized_data
            )
        )

        recommendations = (
            self._recommendations_writer.write(
                normalized_data
            )
        )

        appendix = (
            self._appendix_writer.write(
                normalized_data
            )
        )

        report = (
            self._pdf_generator.generate(
                executive_summary,
                findings,
                recommendations,
                appendix,
            )
        )

        return report


def main() -> None:
    """
    Execute the reporting subsystem
    independently.
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
                },
                {
                    "port": 443,
                    "service": "https",
                },
            ],
        },
        "tls": {
            "tls_enabled": True,
        },
        "virtual_hosts": {
            "hosts": [
                "www.example.com",
                "api.example.com",
            ],
        },
        "fingerprint": {
            "technologies": [
                "Apache",
                "PHP",
            ],
        },
    }

    orchestrator = ReportingOrchestrator()

    results = orchestrator.execute(
        sample
    )

    print(results)


if __name__ == "__main__":
    main()