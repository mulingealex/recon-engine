"""
Environment checker.

Responsible for verifying that the execution environment
is ready before reconnaissance begins.
"""

import argparse
import shutil
import sys


class EnvironmentChecker:
    """Validates the execution environment."""

    REQUIRED_TOOLS = [
    "nmap",
    "curl",
    "dig",
]

    MINIMUM_PYTHON = (3, 10)

    def __init__(self):
        """Initialize the environment checker."""
        pass

    def check(self, arguments: argparse.Namespace) -> argparse.Namespace:
        """
        Validate the execution environment.
        """

        if sys.version_info < self.MINIMUM_PYTHON:
            raise RuntimeError(
                "Python 3.10 or newer is required."
            )

        missing_tools = []

        for tool in self.REQUIRED_TOOLS:

            if shutil.which(tool) is None:
                missing_tools.append(tool)

        if missing_tools:

            raise RuntimeError(
                "Missing required tools: "
                + ", ".join(missing_tools)
            )

        return arguments


if __name__ == "__main__":

    sample = argparse.Namespace(
        target="example.com",
        scope=None,
        output="reports/",
        config=None,
        resume=False,
    )

    checker = EnvironmentChecker()

    validated = checker.check(sample)

    print(validated)