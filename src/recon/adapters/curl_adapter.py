"""
Curl Adapter.

Executes the curl utility and returns structured HTTP probing
information.
"""

import subprocess


class CurlAdapter:
    """Adapter for the curl command."""

    def __init__(self):
        """Initialize the curl adapter."""
        pass

    def execute(self, target: str) -> dict:
        """
        Execute the curl command.

        Parameters
        ----------
        target : str

        Returns
        -------
        dict
            HTTP probing results.
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

        reachable = completed_process.returncode == 0

        headers = {}

        for line in completed_process.stdout.splitlines():

            if ":" in line:

                key, value = line.split(":", 1)

                headers[key.strip()] = value.strip()

        return {
            "target": target,
            "reachable": reachable,
            "http": reachable,
            "https": False,
            "redirect": None,
            "headers": headers,
        }


if __name__ == "__main__":

    adapter = CurlAdapter()

    print(adapter.execute("example.com"))