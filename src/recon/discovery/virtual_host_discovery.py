"""
Virtual Host Discovery Module.

Performs HTTP virtual host discovery by probing candidate
Host headers discovered during reconnaissance.
"""

from argparse import (
    ArgumentParser,
    Namespace,
)

from recon.adapters import VHostAdapter


class VirtualHostDiscovery:
    """
    Virtual host discovery component.
    """

    def __init__(self):
        """Initialize the virtual host discovery component."""

        self._adapter = VHostAdapter()

    def execute(
        self,
        arguments: Namespace,
        line_protocol_results: dict | None = None,
    ) -> dict:
        """
        Execute virtual host discovery.

        Parameters
        ----------
        arguments : Namespace
            Parsed command-line arguments.

        line_protocol_results : dict, optional
            Results produced by LineProtocolDiscovery.

        Returns
        -------
        dict
            Virtual host discovery results.
        """

        host = getattr(arguments, "host", None)

        if host is None:
            host = arguments.target

        port = getattr(arguments, "web_port", None)

        if port is None:
            port = getattr(arguments, "port", 80)

        #
        # Establish baseline.
        #

        baseline = self._adapter.execute(
            host=host,
            port=port,
            virtual_host=host,
        )

        baseline_body = baseline.get("body", "")
        baseline_status = baseline.get("status_code")

        #
        # Build candidate virtual hosts.
        #

        candidates = [
            host,
            "localhost",
            "www",
            "admin",
            "portal",
        ]

        #
        # Add hostname discovered from ROUTE.
        #

        if line_protocol_results:

            commands = line_protocol_results.get(
                "commands",
                {},
            )

            route_response = commands.get(
                "ROUTE"
            )

            if route_response:

                #
                # Expected format:
                #
                # route=gateway-xxxx.local; proof=abcdef
                #

                for item in route_response.split(";"):

                    item = item.strip()

                    if item.startswith("route="):

                        route = item.split(
                            "=",
                            1,
                        )[1].strip()

                        if route:
                            candidates.append(route)

        #
        # Remove duplicates.
        #

        seen = set()

        unique_candidates = []

        for candidate in candidates:

            if candidate not in seen:

                seen.add(candidate)

                unique_candidates.append(
                    candidate
                )

        discovered = []

        #
        # Probe each candidate.
        #

        for candidate in unique_candidates:

            result = self._adapter.execute(
                host=host,
                port=port,
                virtual_host=candidate,
            )

            if not result.get(
                "reachable",
                False,
            ):
                continue

            #
            # Record hosts that behave differently.
            #

            if (
                result.get("status_code")
                != baseline_status
                or result.get("body", "")
                != baseline_body
            ):

                discovered.append(result)

        return {
            "target": host,
            "port": port,
            "baseline": baseline,
            "candidates": unique_candidates,
            "virtual_hosts": discovered,
        }


def main() -> None:
    """
    Standalone execution.
    """

    parser = ArgumentParser()

    parser.add_argument("target")

    parser.add_argument(
        "--port",
        type=int,
        default=80,
    )

    arguments = parser.parse_args()

    arguments.host = arguments.target
    arguments.web_port = arguments.port

    discovery = VirtualHostDiscovery()

    print(
        discovery.execute(arguments)
    )


if __name__ == "__main__":
    main()
    