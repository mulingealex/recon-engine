"""
Service Discovery Module.
"""

from argparse import ArgumentParser, Namespace

from recon.adapters import NmapAdapter


class ServiceDiscovery:
    """Service discovery component."""

    def __init__(self):
        """Initialize the service discovery component."""
        self._adapter = NmapAdapter()

    def execute(self, arguments: Namespace) -> dict:
        """
        Execute service discovery.

        Parameters
        ----------
        arguments : Namespace
            Parsed command-line arguments.

        Returns
        -------
        dict
            Service discovery results.
        """
        return self._adapter.execute(arguments.target)


def main() -> None:
    """Run the service discovery module."""

    parser = ArgumentParser(description="Service Discovery Module")

    parser.add_argument(
        "target",
        help="Target hostname or domain",
    )

    arguments = parser.parse_args()

    discovery = ServiceDiscovery()

    results = discovery.execute(arguments)

    print(results)


if __name__ == "__main__":
    main()