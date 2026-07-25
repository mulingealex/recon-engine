"""
Authenticated HTTP Discovery Module.

Uses the credentials and route key discovered during reconnaissance
to access protected HTTP resources.
"""

from __future__ import annotations

import base64
from argparse import Namespace

from recon.adapters import VHostAdapter


class AuthenticatedHTTPDiscovery:
    """
    Authenticated HTTP discovery component.
    """

    def __init__(self):
        """Initialize the component."""

        self._adapter = VHostAdapter()

    def execute(
        self,
        arguments: Namespace,
        authentication_results: dict,
    ) -> dict:
        """
        Retrieve protected HTTP resources.

        Parameters
        ----------
        arguments : Namespace
            Parsed command-line arguments.

        authentication_results : dict
            Output from AuthenticationDiscovery.

        Returns
        -------
        dict
            Authenticated HTTP discovery results.
        """

        host = getattr(arguments, "host", None)

        if host is None:
            host = arguments.target

        port = getattr(arguments, "web_port", None)

        if port is None:
            port = getattr(arguments, "port", 80)

        #
        # Ensure authentication succeeded.
        #

        if not authentication_results.get("success", False):

            return {
                "success": False,
                "reason": "Authentication discovery failed.",
            }

        virtual_host = authentication_results.get(
            "virtual_host"
        )

        username = authentication_results.get(
            "support_user"
        )

        password = authentication_results.get(
            "support_password"
        )

        route_key = authentication_results.get(
            "route_key"
        )

        #
        # Validate required information.
        #

        missing = []

        if not virtual_host:
            missing.append("virtual_host")

        if not username:
            missing.append("support_user")

        if not password:
            missing.append("support_password")

        if not route_key:
            missing.append("route_key")

        if missing:

            return {
                "success": False,
                "reason": (
                    "Missing required authentication "
                    f"data: {', '.join(missing)}"
                ),
            }

        #
        # Build HTTP Basic Authorization header.
        #

        token = base64.b64encode(
            f"{username}:{password}".encode("utf-8")
        ).decode("ascii")

        headers = {
            "Authorization": f"Basic {token}",
            "X-Route-Key": route_key,
        }

        #
        # Request protected resource.
        #

        response = self._adapter.execute(
            host=host,
            port=port,
            virtual_host=virtual_host,
            path="/user.txt",
            headers=headers,
        )

        if not response.get("reachable", False):

            return {
                "success": False,
                "reason": "Protected resource unreachable.",
                "response": response,
            }

        return {
            "success": response.get("status_code") == 200,
            "virtual_host": virtual_host,
            "resource": "/user.txt",
            "status_code": response.get("status_code"),
            "reason": response.get("reason"),
            "headers": response.get("headers"),
            "body": response.get("body"),
            "response": response,
        }


def main() -> None:
    """
    Standalone testing.

    Normally invoked through the DiscoveryOrchestrator.
    """

    print(
        "AuthenticatedHTTPDiscovery should be executed "
        "through the DiscoveryOrchestrator."
    )


if __name__ == "__main__":
    main()