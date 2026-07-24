"""
Dig Adapter.

Executes the dig utility and returns structured DNS information.
"""

import subprocess


class DigAdapter:
    """Adapter for the dig command."""

    def __init__(self):
        """Initialize the dig adapter."""
        pass

    def execute(self, target: str) -> dict:
        """
        Execute the dig command.

        Parameters
        ----------
        target : str
            Target hostname.

        Returns
        -------
        dict
            Parsed DNS information.
        """

        command = [
            "dig",
            "+short",
            target,
        ]

        completed_process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
        )

        addresses = []

        for line in completed_process.stdout.splitlines():

            line = line.strip()

            if line:

                addresses.append(line)

        return {
            "hostname": target,
            "addresses": addresses,
            "records": {},
            "wildcard": False,
        }


if __name__ == "__main__":

    adapter = DigAdapter()

    print(adapter.execute("example.com"))