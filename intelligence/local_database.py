"""
Offline CVE database.
"""


LOCAL_CVE_DATABASE = {
    "openssh": [
        {
            "cve": "CVE-2024-6387",
            "severity": "High",
            "cvss": "8.1",
            "description": "Possible remote code execution vulnerability.",
            "recommendation": "Update OpenSSH to the latest version."
        }
    ],

    "apache": [
        {
            "cve": "CVE-2024-38475",
            "severity": "High",
            "cvss": "8.8",
            "description": "URL rewriting vulnerability.",
            "recommendation": "Upgrade Apache HTTP Server."
        }
    ],

    "nginx": [
        {
            "cve": "CVE-2023-44487",
            "severity": "High",
            "cvss": "7.5",
            "description": "HTTP/2 Rapid Reset attack.",
            "recommendation": "Update Nginx."
        }
    ],

    "mysql": [
        {
            "cve": "CVE-2024-21096",
            "severity": "Medium",
            "cvss": "6.5",
            "description": "Privilege escalation vulnerability.",
            "recommendation": "Install the latest MySQL security updates."
        }
    ],

    "postgresql": [
        {
            "cve": "CVE-2024-4317",
            "severity": "Medium",
            "cvss": "6.7",
            "description": "Security issue affecting PostgreSQL.",
            "recommendation": "Update PostgreSQL."
        }
    ],

    "redis": [
        {
            "cve": "CVE-2023-45145",
            "severity": "High",
            "cvss": "7.8",
            "description": "Redis vulnerability.",
            "recommendation": "Upgrade Redis."
        }
    ],

    "mongodb": [
        {
            "cve": "CVE-2024-1351",
            "severity": "Medium",
            "cvss": "6.4",
            "description": "MongoDB security issue.",
            "recommendation": "Update MongoDB."
        }
    ]
}


def lookup_local(service: str):
    """
    Return local CVEs for a service.
    """

    return LOCAL_CVE_DATABASE.get(service.lower(), [])
