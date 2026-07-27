"""
Analyze Nmap scan results and generate a professional report.
"""

import re

from intelligence.cve_lookup import lookup_cves
from commands.report import generate_report


def analyze_scan(scan_text: str) -> str:
    """
    Analyze an Nmap scan and generate a professional report.
    """

    scan_text = scan_text.lower()

    # ---------------------------------
    # Detect target automatically
    # ---------------------------------

    target = "Unknown Host"

    match = re.search(
        r"nmap scan report for\s+([^\n\r]+)",
        scan_text,
        re.IGNORECASE,
    )

    if match:
        target = match.group(1).strip()

    findings = []
    details = []

    services = [

        (
            "21/tcp",
            "FTP",
            "FTP transmits data in plaintext.",
            "Replace FTP with SFTP.",
            "ftp",
        ),

        (
            "22/tcp",
            "SSH",
            "Used for secure remote administration.",
            "Disable password login and use SSH keys.",
            "openssh",
        ),

        (
            "23/tcp",
            "Telnet",
            "Telnet is insecure.",
            "Disable Telnet immediately.",
            "telnet",
        ),

        (
            "25/tcp",
            "SMTP",
            "Mail transfer service detected.",
            "Enable SMTP authentication and TLS.",
            "smtp",
        ),

        (
            "53/tcp",
            "DNS",
            "DNS service detected.",
            "Restrict recursive queries and consider DNSSEC.",
            "dns",
        ),

        (
            "80/tcp",
            "HTTP",
            "Web traffic is unencrypted.",
            "Redirect users to HTTPS.",
            "apache",
        ),

        (
            "110/tcp",
            "POP3",
            "Email retrieval service detected.",
            "Use POP3S or migrate to secure protocols.",
            "pop3",
        ),

        (
            "143/tcp",
            "IMAP",
            "Email access service detected.",
            "Enable IMAPS and require encryption.",
            "imap",
        ),

        (
            "443/tcp",
            "HTTPS",
            "Secure encrypted web traffic.",
            "Keep TLS certificates updated.",
            "nginx",
        ),

        (
            "445/tcp",
            "SMB",
            "SMB file sharing detected.",
            "Restrict SMB with firewall rules.",
            "smb",
        ),

        (
            "3306/tcp",
            "MySQL",
            "MySQL database detected.",
            "Restrict network access and use strong credentials.",
            "mysql",
        ),

        (
            "3389/tcp",
            "RDP",
            "Remote Desktop detected.",
            "Restrict access and enable MFA.",
            "rdp",
        ),

        (
            "5432/tcp",
            "PostgreSQL",
            "PostgreSQL database detected.",
            "Allow access only from trusted hosts.",
            "postgresql",
        ),

        (
            "6379/tcp",
            "Redis",
            "Redis service detected.",
            "Enable authentication and avoid public exposure.",
            "redis",
        ),

        (
            "27017/tcp",
            "MongoDB",
            "MongoDB detected.",
            "Enable authentication and restrict exposure.",
            "mongodb",
        ),
    ]

    for port, name, description, recommendation, keyword in services:

        if port in scan_text:

            severity = "Medium"

            if port in (
                "21/tcp",
                "23/tcp",
                "3389/tcp",
                "445/tcp",
            ):
                severity = "High"

            findings.append(
                {
                    "service": name,
                    "severity": severity,
                }
            )

            block = f"🔹 Port {port.split('/')[0]} ({name})\n"

            pattern = rf"{re.escape(port)}\s+open\s+(.+)"

            match = re.search(pattern, scan_text)

            if match:
                version = match.group(1).strip()
                block += f"- Service Detected: {version}\n"

            block += f"- {description}\n"
            block += f"- Recommendation: {recommendation}\n"

            cves = lookup_cves(keyword)

            if cves:

                block += "\n🚨 Known CVEs\n\n"

                for cve in cves:

                    block += (
                        f"• {cve['cve']}\n"
                        f"  Severity: {cve['severity']}\n"
                        f"  CVSS: {cve['cvss']}\n"
                        f"  Description: {cve['description']}\n"
                        f"  Fix: {cve['recommendation']}\n\n"
                    )

            details.append(block.rstrip())

    if not findings:
        return (
            "⚠️ No recognized ports were found.\n\n"
            "Please provide a valid Nmap scan."
        )

    report = generate_report(
        target=target,
        findings=findings,
    )

    report += "\n\nDetailed Findings\n"
    report += "====================================\n\n"

    report += "\n\n".join(details)

    report += "\n\n===================================="
    report += "\n✅ Analysis Complete."

    return report
