"""
Command-line interface parser.

Responsible for parsing user-supplied command-line arguments.

This module does not validate arguments or perform any
reconnaissance. It only converts command-line input into a
structured representation for the Configuration component.
"""

import argparse


class CLIParser:
    """Parses command-line arguments."""

    def __init__(self):
        """Initialize the argument parser."""

        self.parser = argparse.ArgumentParser(
            prog="recon-engine",
            description="A resumable, scope-safe reconnaissance engine."
        )

        # Assessment target
        self.parser.add_argument(
            "--target",
            help="Target hostname or IP address."
        )

        # Scope definition
        self.parser.add_argument(
            "--scope",
            help="Path to the scope definition file."
        )

        # Output directory
        self.parser.add_argument(
            "--output",
            help="Directory for generated artifacts."
        )

        # Configuration file
        self.parser.add_argument(
            "--config",
            help="Path to the configuration file."
        )

        # Resume an interrupted assessment
        self.parser.add_argument(
            "--resume",
            action="store_true",
            help="Resume a previous assessment."
        )

    def parse(self):
        """Parse and return command-line arguments."""
        return self.parser.parse_args()


if __name__ == "__main__":
    parser = CLIParser()
    arguments = parser.parse()
    print(arguments)