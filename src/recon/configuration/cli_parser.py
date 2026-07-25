"""
Command-line argument parser.
"""

from argparse import (
    ArgumentDefaultsHelpFormatter,
    ArgumentParser,
    Namespace,
)


class CLIParser:
    """
    Parses command-line arguments.
    """

    def __init__(self):
        """
        Initialize the CLI parser.
        """

        self._parser = ArgumentParser(
            prog="recon",
            description=(
                "Reconnaissance Engine"
            ),
            formatter_class=(
                ArgumentDefaultsHelpFormatter
            ),
        )

        #
        # Target
        #

        self._parser.add_argument(
            "target",
            nargs="?",
            default=None,
            help=(
                "Target hostname, "
                "host:port, or URL."
            ),
        )

        #
        # Runtime assignment
        #

        self._parser.add_argument(
            "--assignment",
            metavar="FILE",
            default=None,
            help=(
                "Runtime assignment JSON "
                "(Stage 5 local lab)."
            ),
        )

        #
        # Scope
        #

        self._parser.add_argument(
            "--scope",
            metavar="FILE",
            default=None,
            help=(
                "Scope definition."
            ),
        )

        #
        # Output
        #

        self._parser.add_argument(
            "--output",
            default="output",
            help=(
                "Output directory."
            ),
        )

        #
        # Configuration
        #

        self._parser.add_argument(
            "--config",
            metavar="FILE",
            default=None,
            help=(
                "YAML configuration file."
            ),
        )

        #
        # Resume
        #

        self._parser.add_argument(
            "--resume",
            action="store_true",
            help=(
                "Resume a previous assessment."
            ),
        )

    def parse(self) -> Namespace:
        """
        Parse command-line arguments.

        Returns
        -------
        Namespace
            Parsed arguments.
        """

        arguments = (
            self._parser.parse_args()
        )

        #
        # Require either a target
        # or an assignment.
        #

        if (
            arguments.target is None
            and arguments.assignment is None
        ):
            self._parser.error(
                "Either a target or "
                "--assignment must be supplied."
            )

        return arguments


if __name__ == "__main__":

    parser = CLIParser()

    print(
        parser.parse()
    )