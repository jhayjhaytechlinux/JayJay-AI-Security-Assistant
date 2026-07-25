"""
CVE lookup module.

This module will eventually retrieve live CVE information.
For now, it contains a small local database for testing.
"""

CVE_DATABASE = {
    "openssh": [
        {
            "cve": "CVE-2024-6387",
            "severity": "High",
            "cvss": "8.1",
            "description": (
                "Possible remote code execution vulnerability "
                "in certain OpenSSH server configurations."
            ),
            "recommendation": (
                "Update OpenSSH to the latest patched version."
            ),
        }
    ],

    "apache": [
        {
            "cve": "CVE-2024-38475",
            "severity": "High",
            "cvss": "8.8",
            "description": (
                "Improper handling of URL rewriting may allow attacks."
            ),
            "recommendation": (
                "Upgrade Apache HTTP Server to the latest release."
            ),
        }
    ],

    "nginx": [
        {
            "cve": "CVE-2023-44487",
            "severity": "High",
            "cvss": "7.5",
            "description": (
                "HTTP/2 Rapid Reset attack may cause denial of service."
            ),
            "recommendation": (
                "Update Nginx and apply HTTP/2 mitigations."
            ),
        }
    ],

    "mysql": [
        {
            "cve": "CVE-2024-21096",
            "severity": "Medium",
            "cvss": "6.5",
            "description": (
                "MySQL vulnerability that may allow privilege escalation."
            ),
            "recommendation": (
                "Apply Oracle's latest MySQL security updates."
            ),
        }
    ],
}


def lookup_cves(service_name: str):
    """
    Return known CVEs for a detected service.
    """

    service_name = service_name.lower()

    return CVE_DATABASE.get(service_name, [])
