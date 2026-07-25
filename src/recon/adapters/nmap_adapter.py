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

    def execute(
        self,
        host: str,
        port: int | None = None,
    ) -> dict:
        """
        Execute an Nmap scan.

        Parameters
        ----------
        host : str
            Target hostname or IP address.

        port : int | None
            Optional port to scan.

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
        ]

        #
        # Scan the supplied port if available.
        #

        if port is not None:

            command.extend(
                [
                    "-p",
                    str(port),
                ]
            )

        command.append(host)

        try:

            completed_process = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False,
                timeout=300,
            )

        except (
            subprocess.TimeoutExpired,
            FileNotFoundError,
        ):

            return {
                "target": host,
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
                    "target": host,
                    "services": [],
                }

            for host_element in root.findall(
                "host"
            ):

                ports = host_element.find(
                    "ports"
                )

                if ports is None:
                    continue

                for port_element in ports.findall(
                    "port"
                ):

                    state = port_element.find(
                        "state"
                    )

                    service = port_element.find(
                        "service"
                    )

                    if (
                        state is None
                        or state.get("state") != "open"
                    ):
                        continue

                    services.append(
                        {
                            "port": int(
                                port_element.get(
                                    "portid"
                                )
                            ),
                            "protocol": port_element.get(
                                "protocol"
                            ),
                            "state": state.get(
                                "state"
                            ),
                            "service": (
                                service.get("name")
                                if service is not None
                                else "unknown"
                            ),
                            "product": (
                                service.get(
                                    "product",
                                    "",
                                )
                                if service is not None
                                else ""
                            ),
                            "version": (
                                service.get(
                                    "version",
                                    "",
                                )
                                if service is not None
                                else ""
                            ),
                        }
                    )

        return {
            "target": host,
            "services": services,
        }


if __name__ == "__main__":

    adapter = NmapAdapter()

    print(
        adapter.execute(
            "127.0.0.1",
            18408,
        )
    )