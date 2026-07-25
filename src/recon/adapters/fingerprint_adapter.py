"""
Fingerprint Adapter.

Performs lightweight HTTP technology fingerprinting using
response headers and optional virtual host routing.
"""

from __future__ import annotations

import subprocess


class FingerprintAdapter:
    """Adapter for HTTP technology fingerprinting."""

    def __init__(self):
        """Initialize the adapter."""
        pass

    def execute(
        self,
        target: str,
        virtual_host: str | None = None,
    ) -> dict:
        """
        Execute HTTP fingerprinting.

        Parameters
        ----------
        target : str
            Target hostname or IP.

        virtual_host : str, optional
            Host header to send.

        Returns
        -------
        dict
            Fingerprinting results.
        """

        command = [
            "curl",
            "-I",
            "-L",
            "--max-time",
            "10",
        ]

        #
        # Use Host header if supplied.
        #

        if virtual_host:

            command.extend(
                [
                    "-H",
                    f"Host: {virtual_host}",
                ]
            )

        command.append(f"http://{target}")

        completed_process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
        )

        headers = {}

        technologies = []

        for line in completed_process.stdout.splitlines():

            if ":" not in line:
                continue

            key, value = line.split(
                ":",
                1,
            )

            key = key.strip()

            value = value.strip()

            headers[key] = value

        #
        # Basic technology detection.
        #

        server = headers.get("Server")

        powered_by = headers.get("X-Powered-By")

        runtime = headers.get(
            "X-Runtime-Profile"
        )

        if server:
            technologies.append(server)

        if powered_by:
            technologies.append(powered_by)

        if runtime:
            technologies.append(
                f"Runtime:{runtime}"
            )

        return {
            "target": target,
            "virtual_host": virtual_host,
            "technologies": sorted(
                set(technologies)
            ),
            "headers": headers,
        }


if __name__ == "__main__":

    adapter = FingerprintAdapter()

    print(
        adapter.execute(
            "127.0.0.1:18408",
        )
    )