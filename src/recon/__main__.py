"""
Recon package entry point.

Invoke as::

    python -m recon [--assignment FILE] [target]
"""

from __future__ import annotations

from argparse import ArgumentParser

from recon.configuration import ConfigLoader
from recon.engine import ReconEngine


def main() -> None:
    """
    Parse arguments, load configuration, and execute the engine.
    """

    parser = ArgumentParser(
        description="Recon Engine"
    )

    #
    # Target
    #

    parser.add_argument(
        "target",
        nargs="?",
        default=None,
        help=(
            "Target hostname, host:port, "
            "or full URL"
        ),
    )

    #
    # Runtime assignment
    #

    parser.add_argument(
        "--assignment",
        default=None,
        help=(
            "Path to the runtime assignment "
            "JSON file."
        ),
    )

    #
    # YAML configuration
    #

    parser.add_argument(
        "--config",
        default=None,
        help=(
            "Path to a YAML configuration "
            "file."
        ),
    )

    #
    # Output directory
    #

    parser.add_argument(
        "--output",
        default="output",
        help=(
            "Directory used for generated "
            "artifacts."
        ),
    )

    #
    # Resume mode
    #

    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume a previous assessment.",
    )

    arguments = parser.parse_args()

    #
    # Load configuration.
    #

    loader = ConfigLoader()

    arguments = loader.load(
        arguments
    )

    #
    # Execute engine.
    #

    engine = ReconEngine()

    results = engine.execute(
        arguments
    )

    print("\n========================================")
    print("Assessment completed successfully.")
    print("========================================\n")

    print(f"Target: {results['target']}\n")

    print("Artifacts:")

    for artifact, path in (
        results["artifacts"].items()
    ):
        print(
            f"  ✓ {artifact}: {path}"
        )

    print()


if __name__ == "__main__":
    main()