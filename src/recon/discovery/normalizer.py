"""
Discovery Normalizer.

Normalizes discovery results into a consistent schema.
"""


class Normalizer:
    """Normalizes discovery results."""

    def __init__(self):
        """Initialize the normalizer."""
        pass

    def execute(self, results: dict) -> dict:
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
            "dns": results.get("dns", {}),
            "probe": results.get("probe", {}),
            "services": results.get("services", {}),
            "tls": results.get("tls", {}),
            "virtual_hosts": results.get("virtual_hosts", {}),
            "fingerprint": results.get("fingerprint", {}),
        }

        return normalized_results


if __name__ == "__main__":

    sample = {
        "dns": {},
        "probe": {},
        "services": {},
        "tls": {},
        "virtual_hosts": {},
        "fingerprint": {},
    }

    normalizer = Normalizer()

    print(normalizer.execute(sample))