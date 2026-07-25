"""
Fingerprint Adapter.

Performs lightweight HTTP technology fingerprinting using
HTTP response headers and optional virtual host routing.
"""

from __future__ import annotations

import subprocess
from urllib.parse import urlparse


class FingerprintAdapter:
    """Adapter for HTTP technology fingerprinting."""

    def __init__(self):
        """Initialize the fingerprint adapter."""
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

        #
        # Accept either a host:port or a full URL.
        #

        parsed = urlparse(target)

        if parsed.scheme:
            target_url = target
        else:
            target_url = f"http://{target}"

        #
        # Build curl command.
        #

        command = [
            "curl",
            "-s",
            "-L",
            "-D",
            "-",
            "-o",
            "/dev/null",
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

        command.append(target_url)

        completed_process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
        )

        headers = {}
        technologies = []

        #
        # Parse response headers.
        #

        for line in completed_process.stdout.splitlines():

            line = line.strip()

            if not line:
                continue

            if ":" not in line:
                continue

            key, value = line.split(
                ":",
                1,
            )

            headers[key.strip()] = value.strip()

        #
        # Basic fingerprinting rules.
        #

        server = headers.get("Server")
        powered_by = headers.get("X-Powered-By")
        runtime = headers.get("X-Runtime-Profile")
        content_type = headers.get("Content-Type")

        if server:
            technologies.append(server)

        if powered_by:
            technologies.append(powered_by)

        if runtime:
            technologies.append(f"Runtime:{runtime}")

        if content_type:
            technologies.append(content_type)

        return {
            "target": target,
            "virtual_host": virtual_host,
            "technologies": sorted(set(technologies)),
            "headers": headers,
            "stderr": completed_process.stderr,
            "exit_code": completed_process.returncode,
        }


if __name__ == "__main__":

    adapter = FingerprintAdapter()

    print(
        adapter.execute(
            target="127.0.0.1:18408",
            virtual_host="localhost",
        )
    )