"""
Probe Discovery Module.
"""

from argparse import ArgumentParser, Namespace

from recon.adapters import CurlAdapter


class ProbeDiscovery:
    """Probe discovery component."""

    def __init__(self):
        self._adapter = CurlAdapter()

    def execute(self, arguments: Namespace) -> dict:
        """
        Execute HTTP/HTTPS probing.
        """
        return self._adapter.execute(arguments.target)


def main() -> None:
    parser = ArgumentParser(description="Probe Discovery Module")

    parser.add_argument(
        "target",
        help="Target hostname or domain"
    )

    arguments = parser.parse_args()

    discovery = ProbeDiscovery()

    results = discovery.execute(arguments)

    print(results)


if __name__ == "__main__":
    main()