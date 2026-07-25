"""
Executive Summary Writer.

Generates the executive summary section of the
attack surface assessment report.
"""

from datetime import datetime


class ExecutiveSummaryWriter:
    """
    Generates the executive summary.
    """

    def __init__(self):
        """
        Initialize the executive summary writer.
        """

        pass

    def write(
        self,
        normalized_data: dict,
    ) -> str:
        """
        Generate the executive summary.

        Parameters
        ----------
        normalized_data : dict
            Normalized reconnaissance results.

        Returns
        -------
        str
            Rendered markdown section.
        """

        dns = normalized_data.get(
            "dns",
            {},
        )

        probe = normalized_data.get(
            "probe",
            {},
        )

        services = normalized_data.get(
            "services",
            {},
        )

        tls = normalized_data.get(
            "tls",
            {},
        )

        fingerprint = normalized_data.get(
            "fingerprint",
            {},
        )

        hostname = dns.get(
            "hostname",
            "Unknown",
        )

        addresses = dns.get(
            "addresses",
            [],
        )

        technologies = fingerprint.get(
            "technologies",
            [],
        )

        service_count = len(
            services.get(
                "services",
                [],
            )
        )

        timestamp = (
            datetime.utcnow()
            .isoformat(timespec="seconds")
            + "Z"
        )

        summary = f"""# Executive Summary

## Assessment Overview

This report presents the results of an automated
reconnaissance assessment performed against the
specified target. The objective of the assessment
was to identify publicly accessible infrastructure,
discover exposed services, enumerate available
technologies, and collect evidence to support
subsequent security analysis.

---

## Target Information

| Field | Value |
|-------|-------|
| Target | {hostname} |
| Assessment Date | {timestamp} |
| Reachable | {"Yes" if probe.get("reachable") else "No"} |
| IP Addresses | {", ".join(addresses) if addresses else "None"} |

---

## Assessment Summary

The reconnaissance engine successfully completed
the discovery workflow and generated the required
assessment artifacts.

Summary of observations:

- {len(addresses)} IP address(es) identified.
- {service_count} network service(s) discovered.
- {"TLS services detected." if tls.get("tls_enabled") else "No TLS services detected."}
- {len(technologies)} technology fingerprint(s) identified.

---

## Scope

The assessment focused exclusively on publicly
accessible assets associated with the specified
target. No exploitation or intrusive testing was
performed during the discovery process.

---

## Report Structure

The remaining sections of this report provide:

- Technical Findings
- Security Recommendations
- Supporting Evidence
- Assessment Appendix
"""

        return summary


def main() -> None:
    """
    Execute the writer independently.
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
            ]
        },
        "tls": {
            "tls_enabled": True,
        },
        "fingerprint": {
            "technologies": [
                "Apache",
                "PHP",
            ]
        },
    }

    writer = ExecutiveSummaryWriter()

    print(
        writer.write(sample)
    )


if __name__ == "__main__":
    main()