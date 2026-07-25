"""
Discovery Orchestrator.

Coordinates execution of all discovery modules and returns
normalized discovery results.
"""

from argparse import Namespace

from recon.discovery.authentication_discovery import (
    AuthenticationDiscovery,
)
from recon.discovery.authenticated_http_discovery import (
    AuthenticatedHTTPDiscovery,
)
from recon.discovery.dns_discovery import DNSDiscovery
from recon.discovery.fingerprint_discovery import FingerprintDiscovery
from recon.discovery.line_protocol_discovery import (
    LineProtocolDiscovery,
)
from recon.discovery.normalizer import Normalizer
from recon.discovery.probe_discovery import ProbeDiscovery
from recon.discovery.service_discovery import ServiceDiscovery
from recon.discovery.tls_discovery import TLSDiscovery
from recon.discovery.virtual_host_discovery import (
    VirtualHostDiscovery,
)


class DiscoveryOrchestrator:
    """
    Coordinates execution of all discovery modules.
    """

    def __init__(self):
        """Initialize the discovery orchestrator."""

        self._dns = DNSDiscovery()
        self._probe = ProbeDiscovery()
        self._service = ServiceDiscovery()
        self._tls = TLSDiscovery()
        self._line_protocol = LineProtocolDiscovery()
        self._vhost = VirtualHostDiscovery()
        self._authentication = AuthenticationDiscovery()
        self._authenticated_http = AuthenticatedHTTPDiscovery()
        self._fingerprint = FingerprintDiscovery()
        self._normalizer = Normalizer()

    def execute(
        self,
        arguments: Namespace,
    ) -> dict:
        """
        Execute all discovery modules.

        Parameters
        ----------
        arguments : Namespace
            Parsed command-line arguments.

        Returns
        -------
        dict
            Normalized discovery results.
        """

        #
        # DNS Discovery
        #

        dns_results = self._dns.execute(
            arguments
        )

        #
        # Probe Discovery
        #

        probe_results = self._probe.execute(
            arguments
        )

        #
        # Service Discovery
        #

        service_results = self._service.execute(
            arguments
        )

        #
        # TLS Discovery
        #

        tls_results = self._tls.execute(
            arguments
        )

        #
        # Line Protocol Discovery
        #

        line_protocol_results = (
            self._line_protocol.execute(
                arguments
            )
        )

        #
        # Virtual Host Discovery
        #

        virtual_host_results = (
            self._vhost.execute(
                arguments,
                line_protocol_results,
            )
        )

        #
        # Authentication Discovery
        #

        authentication_results = (
            self._authentication.execute(
                arguments,
                virtual_host_results,
                line_protocol_results,
            )
        )

        #
        # Authenticated HTTP Discovery
        #

        authenticated_http_results = (
            self._authenticated_http.execute(
                arguments,
                authentication_results,
            )
        )

        #
        # Fingerprinting
        #

        fingerprint_results = (
    self._fingerprint.execute(
        arguments,
        virtual_host_results,
    )
)

        #
        # Aggregate results.
        #

        discovery_results = {
            "dns": dns_results,
            "probe": probe_results,
            "services": service_results,
            "tls": tls_results,
            "line_protocol": line_protocol_results,
            "virtual_hosts": virtual_host_results,
            "authentication": authentication_results,
            "authenticated_http": authenticated_http_results,
            "fingerprint": fingerprint_results,
        }

        #
        # Normalize.
        #

        normalized_results = (
            self._normalizer.execute(
                discovery_results
            )
        )

        return normalized_results


def main() -> None:
    """
    Run the discovery orchestrator.
    """

    from argparse import ArgumentParser

    parser = ArgumentParser(
        description="Discovery Orchestrator"
    )

    parser.add_argument(
        "target",
        help="Target hostname or IP address",
    )

    parser.add_argument(
        "--port",
        type=int,
        default=80,
    )

    arguments = parser.parse_args()

    #
    # Maintain compatibility with discovery modules.
    #

    arguments.host = arguments.target
    arguments.web_port = arguments.port

    orchestrator = DiscoveryOrchestrator()

    results = orchestrator.execute(
        arguments
    )

    print(results)


if __name__ == "__main__":
    main()