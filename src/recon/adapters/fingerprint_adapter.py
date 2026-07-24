"""
Fingerprint Adapter.

Performs lightweight technology fingerprinting using
HTTP response headers.
"""

import subprocess


class FingerprintAdapter:
    """Adapter for HTTP technology fingerprinting."""

    def __init__(self):
        """Initialize the fingerprint adapter."""
        pass

    def execute(self, target: str) -> dict:
        """
        Execute HTTP fingerprinting.

        Parameters
        ----------
        target : str

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
            f"http://{target}",
        ]

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

            key, value = line.split(":", 1)

            key = key.strip()
            value = value.strip()

            headers[key] = value

        #
        # Basic fingerprinting rules
        #

        server = headers.get("Server", "")
        powered_by = headers.get("X-Powered-By", "")

        if server:
            technologies.append(server)

        if powered_by:
            technologies.append(powered_by)

        return {
            "target": target,
            "technologies": technologies,
            "headers": headers,
        }


if __name__ == "__main__":

    adapter = FingerprintAdapter()

    print(adapter.execute("example.com"))