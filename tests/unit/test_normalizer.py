"""
Unit tests for the Discovery Normalizer.
"""

from recon.discovery.normalizer import Normalizer


def test_normalizer_preserves_all_sections():
    """
    The normalizer should preserve every populated section.
    """

    sample = {
        "dns": {"hostname": "example.com"},
        "probe": {"reachable": True},
        "services": {"count": 1},
        "tls": {"enabled": True},
        "line_protocol": {"protocol": "HTTP/1.1"},
        "virtual_hosts": {"host": "example.local"},
        "authentication": {"success": True},
        "authenticated_http": {"status_code": 200},
        "fingerprint": {"technologies": ["ExampleServer"]},
    }

    normalizer = Normalizer()

    result = normalizer.execute(sample)

    assert result == sample


def test_normalizer_adds_missing_sections():
    """
    Missing sections should be returned as empty dictionaries.
    """

    normalizer = Normalizer()

    result = normalizer.execute({})

    expected = {
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

    assert result == expected