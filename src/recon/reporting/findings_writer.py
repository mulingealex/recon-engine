"""
Findings Writer.

Generates the technical findings section of the
attack surface assessment report.
"""


class FindingsWriter:
    """
    Generates the technical findings section.
    """

    def __init__(self):
        """
        Initialize the findings writer.
        """

        pass

    def write(
        self,
        normalized_data: dict,
    ) -> str:
        """
        Generate the findings section.

        Parameters
        ----------
        normalized_data : dict
            Normalized reconnaissance data.

        Returns
        -------
        str
            Rendered markdown section.
        """

        dns = normalized_data.get(
            "dns",
            {},
        )

        probe = normalized_data.get(
            "probe",
            {},
        )

        services = normalized_data.get(
            "services",
            {},
        )

        tls = normalized_data.get(
            "tls",
            {},
        )

        virtual_hosts = normalized_data.get(
            "virtual_hosts",
            {},
        )

        fingerprint = normalized_data.get(
            "fingerprint",
            {},
        )

        hostname = dns.get(
            "hostname",
            "Unknown",
        )

        addresses = dns.get(
            "addresses",
            [],
        )

        findings = f"""# Technical Findings

## Target

**{hostname}**

---

## DNS Enumeration

The reconnaissance process identified the
following IP addresses associated with the
target.

"""

        if addresses:

            for address in addresses:

                findings += f"- {address}\n"

        else:

            findings += "- No addresses discovered.\n"

        findings += """

---

## Reachability

"""

        if probe.get("reachable"):

            findings += (
                "The target successfully responded "
                "to network probes.\n"
            )

        else:

            findings += (
                "The target did not respond "
                "to network probes.\n"
            )

        findings += """

---

## Discovered Services

"""

        discovered = services.get(
            "services",
            [],
        )

        if discovered:

            for service in discovered:

                findings += (
                    f"- Port "
                    f"{service.get('port')} "
                    f"({service.get('service')})\n"
                )

        else:

            findings += (
                "- No services identified.\n"
            )

        findings += """

---

## TLS Assessment

"""

        if tls.get("tls_enabled"):

            findings += (
                "TLS services were identified "
                "during reconnaissance.\n"
            )

        else:

            findings += (
                "No TLS-enabled services "
                "were identified.\n"
            )

        findings += """

---

## Virtual Hosts

"""

        hosts = virtual_hosts.get(
            "hosts",
            [],
        )

        if hosts:

            for host in hosts:

                findings += f"- {host}\n"

        else:

            findings += (
                "- No virtual hosts identified.\n"
            )

        findings += """

---

## Technology Fingerprinting

"""

        technologies = fingerprint.get(
            "technologies",
            [],
        )

        if technologies:

            for technology in technologies:

                findings += (
                    f"- {technology}\n"
                )

        else:

            findings += (
                "- No technologies identified.\n"
            )

        findings += """

---

## Summary

The above findings represent the
externally observable attack surface
identified during automated reconnaissance.
"""

        return findings


def main() -> None:
    """
    Execute the writer independently.
    """

    sample = {
        "dns": {
            "hostname": "example.com",
            "addresses": [
                "93.184.216.34",
            ],
        },
        "probe": {
            "reachable": True,
        },
        "services": {
            "services": [
                {
                    "port": 80,
                    "service": "http",
                },
                {
                    "port": 443,
                    "service": "https",
                },
            ],
        },
        "tls": {
            "tls_enabled": True,
        },
        "virtual_hosts": {
            "hosts": [
                "www.example.com",
                "api.example.com",
            ],
        },
        "fingerprint": {
            "technologies": [
                "Apache",
                "PHP",
            ],
        },
    }

    writer = FindingsWriter()

    print(
        writer.write(sample)
    )


if __name__ == "__main__":
    main()