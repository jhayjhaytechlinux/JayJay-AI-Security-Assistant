"""
Live CVE lookup module.
Falls back to the local database if live lookup fails.
"""

import requests

from intelligence.local_database import lookup_local


def lookup_live(service: str):
    """
    Attempt to retrieve live CVEs.
    Currently falls back to the local database.
    """

    try:
        # Placeholder for future NVD/API integration.
        # For now, simply verify internet connectivity.
        requests.get(
            "https://www.google.com",
            timeout=3,
        )

        # Future implementation:
        # Query NVD API here.

        return lookup_local(service)

    except Exception:
        # No internet or request failed.
        return lookup_local(service)
