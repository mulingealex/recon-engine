"""
Virtual Host Discovery Module.
"""

from argparse import ArgumentParser, Namespace

from recon.adapters import VHostAdapter


class VirtualHostDiscovery:
    """Virtual host discovery component."""

    def __init__(self):
        self._adapter = VHostAdapter()

    def execute(self, arguments: Namespace) -> dict:
        """
        Execute virtual host discovery.
        """
        return self._adapter.execute(arguments.target)


def main() -> None:
    parser = ArgumentParser(description="Virtual Host Discovery Module")

    parser.add_argument(
        "target",
        help="Target hostname or domain",
    )

    arguments = parser.parse_args()

    discovery = VirtualHostDiscovery()

    results = discovery.execute(arguments)

    print(results)


if __name__ == "__main__":
    main()