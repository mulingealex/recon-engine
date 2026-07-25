"""
Line Protocol Adapter.

Performs generic line-oriented TCP protocol discovery.
"""

from __future__ import annotations

import socket


class LineProtocolAdapter:
    """Adapter for generic line-oriented TCP services."""

    def __init__(self):
        """Initialize the adapter."""
        pass

    def _query(
        self,
        host: str,
        port: int,
        command: str | None,
        timeout: float,
    ) -> tuple[str | None, str | None]:
        """
        Connect, optionally send a command, and return the
        banner and response.

        Returns
        -------
        tuple
            (banner, response)
        """

        with socket.create_connection(
            (host, port),
            timeout=timeout,
        ) as connection:

            connection.settimeout(timeout)

            reader = connection.makefile(
                "r",
                encoding="utf-8",
            )

            writer = connection.makefile(
                "w",
                encoding="utf-8",
            )

            #
            # Read server banner.
            #

            banner = reader.readline().strip()

            response = None

            if command is not None:

                writer.write(
                    command + "\n"
                )

                writer.flush()

                response = (
                    reader.readline()
                    .strip()
                )

            return (
                banner,
                response,
            )

    def execute(
        self,
        host: str,
        port: int,
        timeout: float = 5.0,
    ) -> dict:
        """
        Execute line protocol discovery.

        Parameters
        ----------
        host : str
            Target host.

        port : int
            Target TCP port.

        timeout : float
            Socket timeout.

        Returns
        -------
        dict
            Discovery results.
        """

        results = {
            "target": host,
            "port": port,
            "reachable": False,
            "banner": None,
            "commands": {},
        }

        #
        # First connection:
        # Capture the banner only.
        #

        try:

            banner, _ = self._query(
                host,
                port,
                None,
                timeout,
            )

            results["reachable"] = True
            results["banner"] = banner

        except (
            OSError,
            TimeoutError,
        ):

            return results

        #
        # Generic discovery commands.
        #
        # Each command gets its own
        # TCP connection.
        #

        discovery_commands = (
            "HELP",
            "CAPS",
            "ROUTE",
            "QUIT",
        )

        for command in discovery_commands:

            try:

                _, response = self._query(
                    host,
                    port,
                    command,
                    timeout,
                )

                results["commands"][
                    command
                ] = response

            except (
                OSError,
                TimeoutError,
            ):

                results["commands"][
                    command
                ] = None

        return results


if __name__ == "__main__":

    adapter = LineProtocolAdapter()

    print(
        adapter.execute(
            "127.0.0.1",
            23237,
        )
    )