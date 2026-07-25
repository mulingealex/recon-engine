"""
Line Protocol Discovery Module.

Performs generic line-oriented protocol discovery by delegating
communication to the LineProtocolAdapter.
"""

from argparse import (
    ArgumentParser,
    Namespace,
)

from recon.adapters import LineProtocolAdapter


class LineProtocolDiscovery:
    """
    Line protocol discovery component.
    """

    def __init__(self):
        """
        Initialize the line protocol discovery component.
        """

        self._adapter = LineProtocolAdapter()

    def execute(
        self,
        arguments: Namespace,
    ) -> dict:
        """
        Execute line protocol discovery.

        Parameters
        ----------
        arguments : Namespace
            Parsed command-line arguments.

        Returns
        -------
        dict
            Line protocol discovery results.
        """

        #
        # Line protocols operate on hosts and ports,
        # never URLs.
        #

        host = getattr(
            arguments,
            "host",
            None,
        )

        if host is None:
            host = arguments.target

        port = getattr(
            arguments,
            "signal_port",
            None,
        )

        if port is None:

            return {
                "target": host,
                "port": None,
                "reachable": False,
                "banner": None,
                "capabilities": None,
            }

        return self._adapter.execute(
            host,
            port,
        )


def main() -> None:
    """
    Run the line protocol discovery module.
    """

    parser = ArgumentParser(
        description="Line Protocol Discovery Module"
    )

    parser.add_argument(
        "host",
        help="Target hostname or IP address",
    )

    parser.add_argument(
        "port",
        type=int,
        help="Target TCP port",
    )

    arguments = parser.parse_args()

    #
    # Mirror the runtime Namespace used by the engine.
    #

    arguments.target = arguments.host
    arguments.signal_port = arguments.port

    discovery = LineProtocolDiscovery()

    results = discovery.execute(
        arguments,
    )

    print(results)


if __name__ == "__main__":
    main()