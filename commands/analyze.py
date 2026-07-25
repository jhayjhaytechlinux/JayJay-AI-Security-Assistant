"""
Analyze Nmap scan results.
"""

import re


def get_service_version(scan_text: str, port: str):
    """
    Extract the service/version information
    from an Nmap scan line.
    """

    pattern = rf"^{port}/tcp\s+open\s+(.+)$"

    for line in scan_text.splitlines():
        line = line.strip()

        match = re.match(pattern, line, re.IGNORECASE)

        if match:
            return match.group(1)

    return None


def analyze_scan(scan_text: str) -> str:
    """
    Analyze a simple Nmap scan and return
    a human-readable security assessment.
    """

    findings = []

    scan_text = scan_text.lower()

    ports = {
        "21": (
            "FTP",
            "FTP transmits data in plaintext.",
            "Replace FTP with SFTP."
        ),
        "22": (
            "SSH",
            "Used for secure remote administration.",
            "Disable password login and use SSH keys."
        ),
        "23": (
            "Telnet",
            "Telnet is insecure.",
            "Disable Telnet immediately."
        ),
        "25": (
            "SMTP",
            "Mail transfer service detected.",
            "Enable SMTP authentication and TLS."
        ),
        "53": (
            "DNS",
            "DNS service detected.",
            "Restrict recursive queries and consider DNSSEC."
        ),
        "80": (
            "HTTP",
            "Web traffic is unencrypted.",
            "Redirect users to HTTPS."
        ),
        "110": (
            "POP3",
            "Email retrieval service detected.",
            "Use POP3S or migrate to secure protocols."
        ),
        "143": (
            "IMAP",
            "Email access service detected.",
            "Enable IMAPS and require encryption."
        ),
        "443": (
            "HTTPS",
            "Secure encrypted web traffic.",
            "Keep TLS certificates updated."
        ),
        "445": (
            "SMB",
            "SMB file sharing service detected.",
            "Restrict SMB access with firewall rules."
        ),
        "3306": (
            "MySQL",
            "MySQL database detected.",
            "Restrict network access and use strong credentials."
        ),
        "3389": (
            "RDP",
            "Remote Desktop detected.",
            "Restrict access and enable MFA."
        ),
        "5432": (
            "PostgreSQL",
            "PostgreSQL database detected.",
            "Allow access only from trusted hosts."
        ),
        "6379": (
            "Redis",
            "Redis service detected.",
            "Enable authentication and avoid public exposure."
        ),
        "27017": (
            "MongoDB",
            "MongoDB database detected.",
            "Enable authentication and restrict exposure."
        ),
    }

    for port, details in ports.items():

        if f"{port}/tcp" in scan_text:

            name, description, recommendation = details

            service = get_service_version(scan_text, port)

            if service:

                findings.append(
                    f"🔹 Port {port} ({name})\n"
                    f"- Service Detected: {service}\n"
                    f"- {description}\n"
                    f"- Recommendation: {recommendation}"
                )

            else:

                findings.append(
                    f"🔹 Port {port} ({name})\n"
                    f"- {description}\n"
                    f"- Recommendation: {recommendation}"
                )

    if not findings:

        return (
            "⚠️ No recognized ports were found.\n\n"
            "Please provide a valid Nmap scan."
        )

    report = (
        "🛡️ JayJay AI Security Analysis\n"
        "====================================\n\n"
        f"📊 Open Services Detected: {len(findings)}\n\n"
        + "\n\n".join(findings)
        + "\n\n===================================="
        "\n✅ Analysis Complete."
    )

    return report
