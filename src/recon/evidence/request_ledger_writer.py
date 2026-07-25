"""
Request Ledger Writer.

Writes the request ledger for reconnaissance activity.
"""

from pathlib import Path
import csv
from datetime import datetime


class RequestLedgerWriter:
    """
    Writes the request ledger.
    """

    def __init__(self):
        """
        Initialize the request ledger writer.
        """

        self._output_directory = Path("output")

        self._output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def _timestamp(self) -> str:
        """
        Return a UTC timestamp.

        Returns
        -------
        str
            ISO-8601 timestamp.
        """

        return (
            datetime.utcnow()
            .isoformat(timespec="seconds")
            + "Z"
        )

    def write(
        self,
        normalized_data: dict,
    ) -> dict:
        """
        Write the request ledger.

        Parameters
        ----------
        normalized_data : dict
            Normalized reconnaissance results.

        Returns
        -------
        dict
            Metadata describing the generated artifact.
        """

        output_file = (
            self._output_directory
            / "request-ledger.csv"
        )

        dns = normalized_data.get("dns", {})
        probe = normalized_data.get("probe", {})
        services = normalized_data.get("services", {})
        tls = normalized_data.get("tls", {})
        fingerprint = normalized_data.get("fingerprint", {})
        line_protocol = normalized_data.get(
            "line_protocol",
            {},
        )
        virtual_hosts = normalized_data.get(
            "virtual_hosts",
            {},
        )
        authentication = normalized_data.get(
            "authentication",
            {},
        )
        authenticated_http = normalized_data.get(
            "authenticated_http",
            {},
        )

        target = dns.get(
            "hostname",
            "unknown",
        )

        rows = []

        #
        # DNS
        #

        rows.append(
            {
                "timestamp": self._timestamp(),
                "tool": "dig",
                "target": target,
                "protocol": "DNS",
                "method": "Lookup",
                "status": "Success",
                "artifact": "normalized.json",
            }
        )

        #
        # HTTP probe
        #

        rows.append(
            {
                "timestamp": self._timestamp(),
                "tool": "curl",
                "target": target,
                "protocol": "HTTP",
                "method": "HEAD",
                "status": (
                    "Success"
                    if probe.get("reachable")
                    else "Failed"
                ),
                "artifact": "normalized.json",
            }
        )

        #
        # Service discovery
        #

        rows.append(
            {
                "timestamp": self._timestamp(),
                "tool": "nmap",
                "target": target,
                "protocol": "TCP",
                "method": "Service Scan",
                "status": (
                    "Success"
                    if services.get("services")
                    else "Failed"
                ),
                "artifact": "normalized.json",
            }
        )

        #
        # TLS
        #

        rows.append(
            {
                "timestamp": self._timestamp(),
                "tool": "openssl",
                "target": target,
                "protocol": "TLS",
                "method": "Certificate Inspection",
                "status": (
                    "Success"
                    if tls.get("tls_enabled")
                    else "Failed"
                ),
                "artifact": "normalized.json",
            }
        )

        #
        # Line protocol
        #

        rows.append(
            {
                "timestamp": self._timestamp(),
                "tool": "line-protocol",
                "target": target,
                "protocol": "TCP",
                "method": "CONNECT",
                "status": (
                    "Success"
                    if line_protocol.get("reachable")
                    else "Failed"
                ),
                "artifact": "normalized.json",
            }
        )

        #
        # Virtual host discovery
        #

        rows.append(
            {
                "timestamp": self._timestamp(),
                "tool": "vhost",
                "target": target,
                "protocol": "HTTP",
                "method": "GET /",
                "status": (
                    "Success"
                    if virtual_hosts.get(
                        "virtual_hosts"
                    )
                    else "Failed"
                ),
                "artifact": "normalized.json",
            }
        )

        #
        # Authentication discovery
        #

        rows.append(
            {
                "timestamp": self._timestamp(),
                "tool": "authentication",
                "target": target,
                "protocol": "HTTP",
                "method": "GET /ops-diagnostics",
                "status": (
                    "Success"
                    if authentication.get("success")
                    else "Failed"
                ),
                "artifact": "normalized.json",
            }
        )

        #
        # Authenticated HTTP
        #

        rows.append(
            {
                "timestamp": self._timestamp(),
                "tool": "authenticated-http",
                "target": target,
                "protocol": "HTTP",
                "method": "GET /user.txt",
                "status": (
                    "Success"
                    if authenticated_http.get("success")
                    else "Failed"
                ),
                "artifact": "normalized.json",
            }
        )

        #
        # Fingerprinting
        #

        rows.append(
            {
                "timestamp": self._timestamp(),
                "tool": "fingerprint",
                "target": target,
                "protocol": "HTTP",
                "method": "Technology Fingerprinting",
                "status": (
                    "Success"
                    if fingerprint.get(
                        "technologies"
                    )
                    else "Failed"
                ),
                "artifact": "normalized.json",
            }
        )

        with output_file.open(
            mode="w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "timestamp",
                    "tool",
                    "target",
                    "protocol",
                    "method",
                    "status",
                    "artifact",
                ],
            )

            writer.writeheader()

            writer.writerows(rows)

        return {
            "success": True,
            "artifact": "request-ledger",
            "path": str(output_file),
        }


def main() -> None:
    """
    Standalone execution.
    """

    sample = {
        "dns": {
            "hostname": "127.0.0.1",
        },
        "probe": {
            "reachable": True,
        },
        "services": {
            "services": [
                {
                    "port": 80,
                }
            ]
        },
        "tls": {
            "tls_enabled": False,
        },
        "line_protocol": {
            "reachable": True,
        },
        "virtual_hosts": {
            "virtual_hosts": [
                {}
            ]
        },
        "authentication": {
            "success": True,
        },
        "authenticated_http": {
            "success": True,
        },
        "fingerprint": {
            "technologies": [
                "TransitGateway",
            ]
        },
    }

    writer = RequestLedgerWriter()

    print(
        writer.write(sample)
    )


if __name__ == "__main__":
    main()