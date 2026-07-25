"""
Discovery Normalizer.

Normalizes discovery results into a consistent schema.
"""


class Normalizer:
    """Normalizes discovery results."""

    def __init__(self):
        """Initialize the normalizer."""
        pass

    def execute(
        self,
        results: dict,
    ) -> dict:
        """
        Normalize discovery results.

        Parameters
        ----------
        results : dict
            Combined discovery results.

        Returns
        -------
        dict
            Normalized discovery results.
        """

        normalized_results = {
            "dns": results.get(
                "dns",
                {},
            ),
            "probe": results.get(
                "probe",
                {},
            ),
            "services": results.get(
                "services",
                {},
            ),
            "tls": results.get(
                "tls",
                {},
            ),
            "line_protocol": results.get(
                "line_protocol",
                {},
            ),
            "virtual_hosts": results.get(
                "virtual_hosts",
                {},
            ),
            "authentication": results.get(
                "authentication",
                {},
            ),
            "authenticated_http": results.get(
                "authenticated_http",
                {},
            ),
            "fingerprint": results.get(
                "fingerprint",
                {},
            ),
        }

        return normalized_results


if __name__ == "__main__":

    sample = {
        "dns": {},
        "probe": {},
        "services": {},
        "tls": {},
        "line_protocol": {},
        "virtual_hosts": {},
        "authentication": {},
        "authenticated_http": {},
        "fingerprint": {},
    }

    normalizer = Normalizer()

    print(
        normalizer.execute(
            sample
        )
    )