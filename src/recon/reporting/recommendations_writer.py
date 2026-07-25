"""
Recommendations Writer.

Generates security recommendations for the
attack surface assessment report.
"""


class RecommendationsWriter:
    """
    Generates the recommendations section.
    """

    def __init__(self):
        """
        Initialize the recommendations writer.
        """

        pass

    def write(
        self,
        normalized_data: dict,
    ) -> str:
        """
        Generate the recommendations section.

        Parameters
        ----------
        normalized_data : dict
            Normalized reconnaissance data.

        Returns
        -------
        str
            Rendered markdown section.
        """

        services = normalized_data.get(
            "services",
            {},
        )

        tls = normalized_data.get(
            "tls",
            {},
        )

        fingerprint = normalized_data.get(
            "fingerprint",
            {},
        )

        recommendations = """# Recommendations

The following recommendations are based on the
externally observable attack surface identified
during reconnaissance.

---

## Service Exposure

"""

        discovered = services.get(
            "services",
            [],
        )

        if discovered:

            recommendations += (
                "Review all exposed network services "
                "to ensure that each service is "
                "required for normal business "
                "operations. Remove or restrict "
                "unnecessary services wherever "
                "possible.\n"
            )

        else:

            recommendations += (
                "No externally accessible services "
                "were identified during the "
                "assessment.\n"
            )

        recommendations += """

---

## Transport Security

"""

        if tls.get("tls_enabled"):

            recommendations += (
                "Review TLS configuration to ensure "
                "only modern protocol versions and "
                "strong cipher suites are enabled. "
                "Replace expired or weak certificates "
                "where applicable.\n"
            )

        else:

            recommendations += (
                "Consider enabling TLS for services "
                "that transmit sensitive information "
                "across untrusted networks.\n"
            )

        recommendations += """

---

## Technology Management

"""

        technologies = fingerprint.get(
            "technologies",
            [],
        )

        if technologies:

            recommendations += (
                "Regularly update publicly exposed "
                "software components to supported "
                "versions and apply security patches "
                "promptly.\n"
            )

        else:

            recommendations += (
                "Continue monitoring externally "
                "accessible technologies to maintain "
                "visibility of the attack surface.\n"
            )

        recommendations += """

---

## Continuous Monitoring

- Perform routine attack surface assessments.
- Monitor DNS changes and newly exposed assets.
- Maintain an accurate asset inventory.
- Review firewall and network access rules regularly.
- Log and review externally accessible services.

---

## General Security Practices

- Apply the principle of least privilege.
- Disable unused services and applications.
- Keep operating systems and software up to date.
- Use strong authentication for administrative access.
- Perform regular vulnerability assessments.
- Maintain tested backup and recovery procedures.

---

## Conclusion

Implementing the above recommendations will
reduce the externally exposed attack surface
and improve the organization's overall security
posture.
"""

        return recommendations


def main() -> None:
    """
    Execute the writer independently.
    """

    sample = {
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
        "fingerprint": {
            "technologies": [
                "Apache",
                "PHP",
            ],
        },
    }

    writer = RecommendationsWriter()

    print(
        writer.write(sample)
    )


if __name__ == "__main__":
    main()