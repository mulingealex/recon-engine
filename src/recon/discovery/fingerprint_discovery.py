"""
Fingerprint Discovery Module.
"""

from argparse import ArgumentParser, Namespace

from recon.adapters import FingerprintAdapter


class FingerprintDiscovery:
    """Fingerprint discovery component."""

    def __init__(self):
        """Initialize the fingerprint discovery component."""
        self._adapter = FingerprintAdapter()

    def execute(self, arguments: Namespace) -> dict:
        """
        Execute technology fingerprinting.

        Parameters
        ----------
        arguments : Namespace
            Parsed command-line arguments.

        Returns
        -------
        dict
            Fingerprinting results.
        """
        return self._adapter.execute(arguments.target)


def main() -> None:
    """Run the fingerprint discovery module."""

    parser = ArgumentParser(description="Fingerprint Discovery Module")

    parser.add_argument(
        "target",
        help="Target hostname or domain",
    )

    arguments = parser.parse_args()

    discovery = FingerprintDiscovery()

    results = discovery.execute(arguments)

    print(results)


if __name__ == "__main__":
    main()