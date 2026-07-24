"""
Output manager.

Responsible for preparing the output directory for
reconnaissance results.
"""

import argparse
from pathlib import Path


class OutputManager:
    """Prepares output directories."""

    DEFAULT_OUTPUT = "reports"

    def __init__(self):
        """Initialize the output manager."""
        pass

    def prepare(self, arguments: argparse.Namespace) -> argparse.Namespace:
        """
        Prepare the output directory.
        """

        output = arguments.output or self.DEFAULT_OUTPUT

        output_path = Path(output)

        output_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        arguments.output = str(output_path)

        return arguments


if __name__ == "__main__":

    sample = argparse.Namespace(
        target="example.com",
        scope=None,
        output="reports",
        config=None,
        resume=False,
    )

    manager = OutputManager()

    prepared = manager.prepare(sample)

    print(prepared)