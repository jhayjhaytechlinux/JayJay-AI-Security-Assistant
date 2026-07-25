"""
Analyze Nmap scan results with optional CVE intelligence.
"""

import re

from intelligence.cve_lookup import lookup_cves


def analyze_scan(scan_text: str) -> str:
    """
    Analyze an Nmap scan and generate a security report.
    """

    findings = []

    # Preserve the original text for display
    original_text = scan_text

    # Use lowercase only for detection
    scan_text = scan_text.lower()

    port_patterns = [
        {
            "port": "21/tcp",
            "name": "FTP",
            "recommendation": "Replace FTP with SFTP.",
            "description": "FTP transmits data in plaintext.",
        },
        {
            "port": "22/tcp",
            "name": "SSH",
            "recommendation": "Disable password login and use SSH keys.",
            "description": "Used for secure remote administration.",
        },
        {
            "port": "23/tcp",
            "name": "Telnet",
            "recommendation": "Disable Telnet immediately.",
            "description": "Telnet is insecure.",
        },
        {
            "port": "25/tcp",
            "name": "SMTP",
            "recommendation": "Enable SMTP authentication and TLS.",
            "description": "Mail transfer service detected.",
        },
        {
            "port": "53/tcp",
            "name": "DNS",
            "recommendation": (
                "Restrict recursive queries and consider DNSSEC."
            ),
            "description": "DNS service detected.",
        },
        {
            "port": "80/tcp",
            "name": "HTTP",
            "recommendation": "Redirect users to HTTPS.",
            "description": "Web traffic is unencrypted.",
        },
        {
            "port": "110/tcp",
            "name": "POP3",
            "recommendation": (
                "Use POP3S or migrate to more secure protocols."
            ),
            "description": "Email retrieval service detected.",
        },
        {
            "port": "143/tcp",
            "name": "IMAP",
            "recommendation": (
                "Enable IMAPS and require encryption."
            ),
            "description": "Email access service detected.",
        },
        {
            "port": "443/tcp",
            "name": "HTTPS",
            "recommendation": (
                "Keep TLS certificates updated."
            ),
            "description": "Secure encrypted web traffic.",
        },
        {
            "port": "445/tcp",
            "name": "SMB",
            "recommendation": (
                "Restrict access with firewall rules."
            ),
            "description": (
                "SMB can expose file sharing services."
            ),
        },
        {
            "port": "3306/tcp",
            "name": "MySQL",
            "recommendation": (
                "Restrict network access and use strong credentials."
            ),
            "description": "MySQL database detected.",
        },
        {
            "port": "3389/tcp",
            "name": "RDP",
            "recommendation": (
                "Restrict access and enable MFA."
            ),
            "description": "Remote Desktop detected.",
        },
        {
            "port": "5432/tcp",
            "name": "PostgreSQL",
            "recommendation": (
                "Allow access only from trusted hosts."
            ),
            "description": "PostgreSQL database detected.",
        },
        {
            "port": "6379/tcp",
            "name": "Redis",
            "recommendation": (
                "Enable authentication and avoid exposing it publicly."
            ),
            "description": "Redis service detected.",
        },
        {
            "port": "27017/tcp",
            "name": "MongoDB",
            "recommendation": (
                "Enable authentication and restrict network exposure."
            ),
            "description": "MongoDB service detected.",
        },
    ]

    service_count = 0

    for item in port_patterns:

        if item["port"] not in scan_text:
            continue

        service_count += 1

        port_number = item["port"].split("/")[0]

        service_version = None

        pattern = (
            rf"{re.escape(port_number)}/tcp\s+open\s+(.+)"
        )

        match = re.search(
            pattern,
            original_text,
            flags=re.IGNORECASE,
        )

        if match:
            service_version = match.group(1).strip()

        report = (
            f"🔹 Port {port_number} ({item['name']})\n"
        )

        if service_version:
            report += (
                f"- Service Detected: {service_version}\n"
            )

        report += (
            f"- {item['description']}\n"
            f"- Recommendation: {item['recommendation']}"
        )

        # -----------------------------
        # CVE Intelligence
        # -----------------------------
        if service_version:

            first_word = (
                service_version
                .split()[0]
                .lower()
            )

            cves = lookup_cves(first_word)

            if cves:

                report += "\n\n🚨 Known CVEs"

                for cve in cves:

                    report += (
                        f"\n\n• {cve['cve']}"
                        f"\n  Severity: {cve['severity']}"
                        f"\n  CVSS: {cve['cvss']}"
                        f"\n  Description: {cve['description']}"
                        f"\n  Fix: {cve['recommendation']}"
                    )

        findings.append(report)

    if not findings:
        return (
            "⚠️ No recognized ports were found.\n\n"
            "Please provide a valid Nmap scan."
        )

    return (
        "🛡️ JayJay AI Security Analysis\n"
        "====================================\n\n"
        f"📊 Open Services Detected: {service_count}\n\n"
        + "\n\n".join(findings)
        + "\n\n====================================\n"
        "✅ Analysis Complete."
    )
