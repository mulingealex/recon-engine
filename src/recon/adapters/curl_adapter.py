"""
Curl Adapter.

Executes the curl utility and returns structured HTTP probing
information.
"""

import subprocess


class CurlAdapter:
    """Adapter for the curl command."""

    def __init__(self):
        """Initialize the curl adapter."""
        pass

    def execute(self, target: str) -> dict:
        """
        Execute the curl command.

        Parameters
        ----------
        target : str

        Returns
        -------
        dict
            HTTP probing results.
        """

        #
        # Accept:
        #
        # example.com
        # 127.0.0.1
        # 127.0.0.1:18408
        # http://127.0.0.1:18408/
        # https://example.com
        #

        if (
            target.startswith("http://")
            or target.startswith("https://")
        ):
            url = target

        else:
            url = f"http://{target}"

        command = [
            "curl",
            "-I",
            "-L",
            "--max-time",
            "10",
            url,
        ]

        completed_process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
        )

        reachable = (
            completed_process.returncode == 0
        )

        headers = {}

        status_code = None

        protocol = None

        for line in completed_process.stdout.splitlines():

            #
            # HTTP status line
            #

            if line.startswith("HTTP/"):

                parts = line.split()

                if len(parts) >= 2:

                    protocol = parts[0]

                    try:
                        status_code = int(parts[1])

                    except ValueError:
                        status_code = None

                continue

            #
            # HTTP headers
            #

            if ":" in line:

                key, value = line.split(
                    ":",
                    1,
                )

                headers[
                    key.strip()
                ] = value.strip()

        redirect = headers.get(
            "Location"
        )

        return {
            "target": target,
            "url": url,
            "reachable": reachable,
            "http": reachable,
            "https": url.startswith(
                "https://"
            ),
            "redirect": redirect,
            "status_code": status_code,
            "protocol": protocol,
            "headers": headers,
        }


if __name__ == "__main__":

    adapter = CurlAdapter()

    print(
        adapter.execute(
            "example.com"
        )
    )

    print(
        adapter.execute(
            "127.0.0.1:18408"
        )
    )

    print(
        adapter.execute(
            "http://127.0.0.1:18408/"
        )
    )