"""
Service Discovery Module.
"""

from argparse import (
    ArgumentParser,
    Namespace,
)

from recon.adapters import NmapAdapter


class ServiceDiscovery:
    """Service discovery component."""

    def __init__(self):
        """Initialize the service discovery component."""
        self._adapter = NmapAdapter()

    def execute(
        self,
        arguments: Namespace,
    ) -> dict:
        """
        Execute service discovery.

        Parameters
        ----------
        arguments : Namespace

        Returns
        -------
        dict
        """

        host = getattr(
            arguments,
            "host",
            None,
        )

        if host is None:
            host = arguments.target

        port = getattr(
            arguments,
            "port",
            None,
        )

        return self._adapter.execute(
            host,
            port,
        )


def main() -> None:

    parser = ArgumentParser(
        description="Service Discovery Module"
    )

    parser.add_argument(
        "target",
        help="Target hostname or domain",
    )

    arguments = parser.parse_args()

    discovery = ServiceDiscovery()

    print(
        discovery.execute(
            arguments
        )
    )


if __name__ == "__main__":
    main()