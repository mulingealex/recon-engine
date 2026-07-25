"""
Virtual Host Adapter.

Performs HTTP requests using custom Host headers to identify
virtual hosts and access protected HTTP resources.
"""

from __future__ import annotations

import http.client


class VHostAdapter:
    """
    Adapter for HTTP virtual host interactions.
    """

    def __init__(self):
        """Initialize the adapter."""
        pass

    def execute(
        self,
        host: str,
        port: int,
        virtual_host: str,
        path: str = "/",
        method: str = "GET",
        timeout: int = 5,
        headers: dict | None = None,
    ) -> dict:
        """
        Execute an HTTP request using a custom Host header.

        Parameters
        ----------
        host : str
            Target IP address or hostname.

        port : int
            Target HTTP port.

        virtual_host : str
            Host header value.

        path : str, default="/"
            HTTP resource path.

        method : str, default="GET"
            HTTP request method.

        timeout : int, default=5
            Socket timeout in seconds.

        headers : dict, optional
            Additional HTTP headers.

        Returns
        -------
        dict
            HTTP response details.
        """

        connection = None

        try:

            connection = http.client.HTTPConnection(
                host=host,
                port=port,
                timeout=timeout,
            )

            request_headers = {
                "Host": virtual_host,
            }

            if headers:
                request_headers.update(headers)

            connection.request(
                method=method,
                url=path,
                headers=request_headers,
            )

            response = connection.getresponse()

            version_map = {
                9: "HTTP/0.9",
                10: "HTTP/1.0",
                11: "HTTP/1.1",
            }

            protocol = version_map.get(
                response.version,
                f"HTTP/{response.version}",
            )

            body = response.read().decode(
                "utf-8",
                errors="replace",
            )

            response_headers = dict(
                response.getheaders()
            )

            return {
                "reachable": True,
                "target": host,
                "port": port,
                "virtual_host": virtual_host,
                "method": method,
                "path": path,
                "status_code": response.status,
                "reason": response.reason,
                "protocol": protocol,
                "headers": response_headers,
                "body": body,
            }

        except Exception as error:

            return {
                "reachable": False,
                "target": host,
                "port": port,
                "virtual_host": virtual_host,
                "method": method,
                "path": path,
                "status_code": None,
                "reason": None,
                "protocol": None,
                "headers": {},
                "body": "",
                "error": str(error),
            }

        finally:

            if connection is not None:
                connection.close()


if __name__ == "__main__":

    adapter = VHostAdapter()

    print(
        adapter.execute(
            host="127.0.0.1",
            port=18408,
            virtual_host="localhost",
            path="/",
        )
    )