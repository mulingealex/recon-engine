"""
DNS Discovery Module.

Performs DNS discovery by delegating DNS lookups
to the DigAdapter.
"""

from argparse import (
    ArgumentParser,
    Namespace,
)

from recon.adapters import DigAdapter


class DNSDiscovery:
    """
    DNS discovery component.
    """

    def __init__(self):
        """
        Initialize the DNS discovery component.
        """

        self._adapter = DigAdapter()

    def execute(
        self,
        arguments: Namespace,
    ) -> dict:
        """
        Execute DNS discovery.

        Parameters
        ----------
        arguments : Namespace
            Parsed command-line arguments.

        Returns
        -------
        dict
            DNS discovery results.
        """

        #
        # DNS operates on hostnames,
        # never URLs.
        #

        target = getattr(
            arguments,
            "host",
            None,
        )

        if target is None:
            target = arguments.target

        return self._adapter.execute(
            target
        )


def main() -> None:
    """
    Run the DNS discovery module.
    """

    parser = ArgumentParser(
        description="DNS Discovery Module"
    )

    parser.add_argument(
        "target",
        help="Target hostname or domain",
    )

    arguments = parser.parse_args()

    discovery = DNSDiscovery()

    results = discovery.execute(
        arguments
    )

    print(results)


if __name__ == "__main__":
    main()