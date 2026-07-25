"""
Normalized Writer.

Writes normalized reconnaissance data.
"""

from pathlib import Path
import json


class NormalizedWriter:
    """
    Writes normalized reconnaissance data.
    """

    def __init__(self):
        """
        Initialize the normalized writer.
        """

        self._output_directory = Path("output")

        self._output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def write(self, normalized_data: dict) -> dict:
        """
        Write normalized data.

        Parameters
        ----------
        normalized_data : dict

        Returns
        -------
        dict
            Metadata describing the generated file.
        """

        output_file = self._output_directory / "normalized.json"

        with output_file.open(
            mode="w",
            encoding="utf-8",
        ) as file:

            json.dump(
                normalized_data,
                file,
                indent=4,
                sort_keys=True,
            )

        return {
            "success": True,
            "artifact": "normalized",
            "path": str(output_file),
        }


def main():

    sample = {
        "dns": {
            "hostname": "example.com"
        }
    }

    writer = NormalizedWriter()

    print(writer.write(sample))


if __name__ == "__main__":
    main()