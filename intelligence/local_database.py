"""
Offline CVE intelligence database.

Provides cybersecurity vulnerability context
for detected services.
"""


LOCAL_CVE_DATABASE = {

    "openssh": [
        {
            "cve": "CVE-2024-6387",
            "severity": "High",
            "cvss": "8.1",
            "category": "Remote Code Execution",
            "impact": (
                "An attacker may execute code remotely "
                "against vulnerable OpenSSH systems."
            ),
            "description": (
                "Possible remote code execution vulnerability "
                "affecting OpenSSH."
            ),
            "recommendation": (
                "Update OpenSSH to the latest version "
                "and disable password authentication."
            ),
        }
    ],


    "apache": [
        {
            "cve": "CVE-2024-38475",
            "severity": "High",
            "cvss": "8.8",
            "category": "Web Server Vulnerability",
            "impact": (
                "Attackers may exploit vulnerable Apache "
                "configurations to access unintended resources."
            ),
            "description": (
                "Apache HTTP Server URL rewriting vulnerability."
            ),
            "recommendation": (
                "Upgrade Apache HTTP Server and review "
                "rewrite configurations."
            ),
        }
    ],


    "nginx": [
        {
            "cve": "CVE-2023-44487",
            "severity": "High",
            "cvss": "7.5",
            "category": "Denial of Service",
            "impact": (
                "Attackers may exhaust server resources "
                "through HTTP/2 Rapid Reset attacks."
            ),
            "description": (
                "HTTP/2 Rapid Reset attack vulnerability."
            ),
            "recommendation": (
                "Update Nginx and apply vendor security patches."
            ),
        }
    ],


    "mysql": [
        {
            "cve": "CVE-2024-21096",
            "severity": "Medium",
            "cvss": "6.5",
            "category": "Privilege Escalation",
            "impact": (
                "An attacker may gain elevated database privileges."
            ),
            "description": (
                "MySQL privilege escalation security issue."
            ),
            "recommendation": (
                "Install the latest MySQL security updates."
            ),
        }
    ],


    "postgresql": [
        {
            "cve": "CVE-2024-4317",
            "severity": "Medium",
            "cvss": "6.7",
            "category": "Database Security Issue",
            "impact": (
                "Potential compromise of database security."
            ),
            "description": (
                "PostgreSQL security vulnerability."
            ),
            "recommendation": (
                "Upgrade PostgreSQL to the latest version."
            ),
        }
    ],


    "redis": [
        {
            "cve": "CVE-2023-45145",
            "severity": "High",
            "cvss": "7.8",
            "category": "Remote Exploitation",
            "impact": (
                "Attackers may compromise exposed Redis services."
            ),
            "description": (
                "Redis security vulnerability."
            ),
            "recommendation": (
                "Upgrade Redis and enable authentication."
            ),
        }
    ],


    "mongodb": [
        {
            "cve": "CVE-2024-1351",
            "severity": "Medium",
            "cvss": "6.4",
            "category": "Database Security Issue",
            "impact": (
                "Potential exposure of MongoDB data."
            ),
            "description": (
                "MongoDB security vulnerability."
            ),
            "recommendation": (
                "Update MongoDB and restrict database exposure."
            ),
        }
    ],
}


def lookup_local(service: str):
    """
    Return local CVE intelligence for a service.
    """

    return LOCAL_CVE_DATABASE.get(
        service.lower(),
        [],
    )
