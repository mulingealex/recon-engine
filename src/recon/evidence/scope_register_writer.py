"""
Scope Register Writer.

Writes the assessment scope register.
"""

from pathlib import Path
import csv


class ScopeRegisterWriter:
    """
    Writes the scope register.
    """

    def __init__(self):
        """
        Initialize the scope register writer.
        """

        self._output_directory = Path("output")

        self._output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def write(self, normalized_data: dict) -> dict:
        """
        Write the scope register.

        Parameters
        ----------
        normalized_data : dict

        Returns
        -------
        dict
            Metadata describing the generated artifact.
        """

        output_file = self._output_directory / "scope-register.csv"

        dns = normalized_data.get("dns", {})

        hostname = dns.get("hostname", "")
        addresses = ";".join(
            dns.get("addresses", [])
        )

        with output_file.open(
            mode="w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "Target",
                    "Addresses",
                    "Status",
                ]
            )

            writer.writerow(
                [
                    hostname,
                    addresses,
                    "In Scope",
                ]
            )

        return {
            "success": True,
            "artifact": "scope-register",
            "path": str(output_file),
        }


def main():
    """
    Run the writer independently.
    """

    sample = {
        "dns": {
            "hostname": "example.com",
            "addresses": [
                "93.184.216.34"
            ]
        }
    }

    writer = ScopeRegisterWriter()

    print(writer.write(sample))


if __name__ == "__main__":
    main()