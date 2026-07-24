"""
Discovery Orchestrator.

Coordinates the execution of all discovery modules.
"""

import argparse

from recon.discovery.dns_discovery import DNSDiscovery
from recon.discovery.probe_discovery import ProbeDiscovery
from recon.discovery.service_discovery import ServiceDiscovery
from recon.discovery.tls_discovery import TLSDiscovery
from recon.discovery.virtual_host_discovery import VirtualHostDiscovery
from recon.discovery.fingerprint_discovery import FingerprintDiscovery
from recon.discovery.normalizer import Normalizer


class DiscoveryOrchestrator:
    """Coordinates the discovery workflow."""

    def __init__(self):
        """Initialize discovery modules."""

        self._dns = DNSDiscovery()
        self._probe = ProbeDiscovery()
        self._service = ServiceDiscovery()
        self._tls = TLSDiscovery()
        self._virtual_host = VirtualHostDiscovery()
        self._fingerprint = FingerprintDiscovery()
        self._normalizer = Normalizer()

    def execute(self, arguments: argparse.Namespace) -> dict:
        """
        Execute the complete discovery workflow.

        Parameters
        ----------
        arguments : argparse.Namespace

        Returns
        -------
        dict
            Normalized discovery results.
        """

        results = {}

        # DNS Discovery
        results["dns"] = self._dns.execute(arguments)

        # Target Probing
        results["probe"] = self._probe.execute(arguments)

        # Service Discovery
        results["services"] = self._service.execute(arguments)

        # TLS Discovery
        results["tls"] = self._tls.execute(arguments)

        # Virtual Host Discovery
        results["virtual_hosts"] = self._virtual_host.execute(arguments)

        # Technology Fingerprinting
        results["fingerprint"] = self._fingerprint.execute(arguments)

        # Normalize discovery results
        normalized_results = self._normalizer.execute(results)

        return normalized_results


if __name__ == "__main__":

    sample = argparse.Namespace(
        target="example.com",
        output="reports",
        resume=False,
    )

    orchestrator = DiscoveryOrchestrator()

    discovery_results = orchestrator.execute(sample)

    print(discovery_results)