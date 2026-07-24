"""
TLS Discovery Module.
"""

from argparse import ArgumentParser, Namespace

from recon.adapters import OpenSSLAdapter


class TLSDiscovery:
    """TLS discovery component."""

    def __init__(self):
        """Initialize the TLS discovery component."""
        self._adapter = OpenSSLAdapter()

    def execute(self, arguments: Namespace) -> dict:
        """
        Execute TLS discovery.

        Parameters
        ----------
        arguments : Namespace
            Parsed command-line arguments.

        Returns
        -------
        dict
            TLS discovery results.
        """
        return self._adapter.execute(arguments.target)


def main() -> None:
    """Run the TLS discovery module."""

    parser = ArgumentParser(description="TLS Discovery Module")

    parser.add_argument(
        "target",
        help="Target hostname or domain",
    )

    arguments = parser.parse_args()

    discovery = TLSDiscovery()

    results = discovery.execute(arguments)

    print(results)


if __name__ == "__main__":
    main()