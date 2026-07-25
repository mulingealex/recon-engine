"""
Fingerprint Discovery Module.
"""

from argparse import (
    ArgumentParser,
    Namespace,
)

from recon.adapters import FingerprintAdapter


class FingerprintDiscovery:
    """
    Fingerprint discovery component.
    """

    def __init__(self):
        self._adapter = FingerprintAdapter()

    def execute(
        self,
        arguments: Namespace,
        virtual_host_results: dict | None = None,
    ) -> dict:
        """
        Execute technology fingerprinting.

        Parameters
        ----------
        arguments : Namespace

        virtual_host_results : dict, optional

        Returns
        -------
        dict
            Fingerprinting results.
        """

        virtual_host = None

        if virtual_host_results:

            hosts = virtual_host_results.get(
                "virtual_hosts",
                [],
            )

            if hosts:

                virtual_host = hosts[0].get(
                    "virtual_host"
                )

        return self._adapter.execute(
            target=arguments.target,
            virtual_host=virtual_host,
        )


def main() -> None:

    parser = ArgumentParser()

    parser.add_argument(
        "target",
    )

    arguments = parser.parse_args()

    discovery = FingerprintDiscovery()

    print(
        discovery.execute(
            arguments,
        )
    )


if __name__ == "__main__":
    main()