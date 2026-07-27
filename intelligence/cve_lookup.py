"""
Unified CVE lookup engine.

1. Check the local CVE database.
2. If nothing is found, query the live NVD API.
"""

from config import ENABLE_LIVE_CVE_LOOKUP
from intelligence.local_database import lookup_local
from intelligence.live_lookup import lookup_live
from intelligence.nvd import search_nvd


def lookup_cves(service):
    """
    Return CVEs for a service.

    Priority:
        1. Local database
        2. Live lookup
        3. Official NVD
    """

    service = service.lower().strip()

    # -----------------------------
    # Local database
    # -----------------------------

    results = lookup_local(service)

    if results:
        return results

    # -----------------------------
    # Existing live lookup
    # -----------------------------

    results = lookup_live(service)

    if results:
        return results

    # -----------------------------
    # Official NVD lookup
    # -----------------------------

    if ENABLE_LIVE_CVE_LOOKUP:

        results = search_nvd(service)

        if results:
            return results

    return []
