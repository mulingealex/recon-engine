"""
Nmap Adapter.

Executes the Nmap utility and returns structured service
discovery information.
"""

import subprocess
import xml.etree.ElementTree as ET


class NmapAdapter:
    """Adapter for the Nmap command."""

    def __init__(self):
        """Initialize the Nmap adapter."""
        pass

    def execute(self, target: str) -> dict:
        """
        Execute an Nmap scan.

        Parameters
        ----------
        target : str

        Returns
        -------
        dict
            Service discovery results.
        """

        command = [
            "nmap",
            "-oX",
            "-",
            "-sV",
            target,
        ]

        try:

            completed_process = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False,
                timeout=300,
            )

        except subprocess.TimeoutExpired:

            return {
                "target": target,
                "services": [],
            }

        except FileNotFoundError:

            return {
                "target": target,
                "services": [],
            }

        services = []

        if completed_process.returncode == 0:

            try:

                root = ET.fromstring(
                    completed_process.stdout
                )

            except ET.ParseError:

                return {
                    "target": target,
                    "services": [],
                }

            for host in root.findall("host"):

                ports = host.find("ports")

                if ports is None:
                    continue

                for port in ports.findall("port"):

                    state = port.find("state")
                    service = port.find("service")

                    if (
                        state is None
                        or service is None
                        or state.get("state") != "open"
                    ):
                        continue

                    services.append(
                        {
                            "port": int(
                                port.get("portid")
                            ),
                            "protocol": port.get(
                                "protocol"
                            ),
                            "state": state.get(
                                "state"
                            ),
                            "service": service.get(
                                "name"
                            ),
                            "version": service.get(
                                "version",
                                "",
                            ),
                        }
                    )

        return {
            "target": target,
            "services": services,
        }


if __name__ == "__main__":

    adapter = NmapAdapter()

    print(
        adapter.execute(
            "scanme.nmap.org"
        )
    )