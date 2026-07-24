"""
OpenSSL Adapter.

Executes the OpenSSL utility and returns structured TLS
certificate information.
"""

import subprocess


class OpenSSLAdapter:
    """Adapter for the OpenSSL command."""

    def __init__(self):
        """Initialize the OpenSSL adapter."""
        pass

    def execute(self, target: str, port: int = 443) -> dict:
        """
        Execute the OpenSSL command.

        Parameters
        ----------
        target : str
            Target hostname.

        port : int
            TLS service port.

        Returns
        -------
        dict
            TLS information.
        """

        command = [
            "openssl",
            "s_client",
            "-connect",
            f"{target}:{port}",
            "-servername",
            target,
        ]

        completed_process = subprocess.run(
            command,
            input="Q\n",
            capture_output=True,
            text=True,
            check=False,
        )

        tls_enabled = completed_process.returncode == 0

        certificate = {
            "subject": None,
            "issuer": None,
        }

        protocols = []

        for line in completed_process.stdout.splitlines():

            line = line.strip()

            if line.startswith("subject="):
                certificate["subject"] = line.replace("subject=", "").strip()

            elif line.startswith("issuer="):
                certificate["issuer"] = line.replace("issuer=", "").strip()

            elif "Protocol" in line:

                parts = line.split(":", 1)

                if len(parts) == 2:

                    protocols.append(parts[1].strip())

        return {
            "target": target,
            "tls_enabled": tls_enabled,
            "protocols": protocols,
            "certificate": certificate,
        }


if __name__ == "__main__":

    adapter = OpenSSLAdapter()

    print(adapter.execute("google.com"))