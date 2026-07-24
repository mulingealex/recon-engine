"""
Discovery Orchestrator.

Coordinates all discovery modules and returns normalized
discovery results.
"""

from argparse import Namespace

from recon.discovery.dns_discovery import DNSDiscovery
from recon.discovery.probe_discovery import ProbeDiscovery
from recon.discovery.service_discovery import ServiceDiscovery
from recon.discovery.tls_discovery import TLSDiscovery
from recon.discovery.virtual_host_discovery import VirtualHostDiscovery
from recon.discovery.fingerprint_discovery import FingerprintDiscovery
from recon.discovery.normalizer import Normalizer


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
        self._vhost = VirtualHostDiscovery()
        self._fingerprint = FingerprintDiscovery()
        self._normalizer = Normalizer()

    def execute(self, arguments: Namespace) -> dict:
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

        discovery_results = {
            "dns": self._dns.execute(arguments),
            "probe": self._probe.execute(arguments),
            "services": self._service.execute(arguments),
            "tls": self._tls.execute(arguments),
            "virtual_hosts": self._vhost.execute(arguments),
            "fingerprint": self._fingerprint.execute(arguments),
        }

        normalized_results = self._normalizer.execute(
            discovery_results
        )

        return normalized_results


def main() -> None:
    """
    Run the discovery orchestrator as a standalone program.
    """

    from argparse import ArgumentParser

    parser = ArgumentParser(
        description="Discovery Orchestrator"
    )

    parser.add_argument(
        "target",
        help="Target hostname or domain",
    )

    arguments = parser.parse_args()

    orchestrator = DiscoveryOrchestrator()

    results = orchestrator.execute(arguments)

    print(results)


if __name__ == "__main__":
    main()