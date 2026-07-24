"""
Analyze Nmap scan results.
"""


def analyze_scan(scan_text: str) -> str:
    """
    Analyze a simple Nmap scan and return
    a human-readable security assessment.
    """

    findings = []

    if "21/tcp" in scan_text:
        findings.append(
            "🔹 Port 21 (FTP)\n"
            "- FTP transmits data in plaintext.\n"
            "- Recommendation: Replace FTP with SFTP."
        )

    if "22/tcp" in scan_text:
        findings.append(
            "🔹 Port 22 (SSH)\n"
            "- Used for secure remote administration.\n"
            "- Recommendation: Disable password login and use SSH keys."
        )

    if "23/tcp" in scan_text:
        findings.append(
            "🔹 Port 23 (Telnet)\n"
            "- Telnet is insecure.\n"
            "- Recommendation: Disable Telnet immediately."
        )

    if "25/tcp" in scan_text:
        findings.append(
            "🔹 Port 25 (SMTP)\n"
            "- Mail transfer service detected.\n"
            "- Recommendation: Enable SMTP authentication and TLS."
        )

    if "53/tcp" in scan_text:
        findings.append(
            "🔹 Port 53 (DNS)\n"
            "- DNS service detected.\n"
            "- Recommendation: Restrict recursive queries and consider DNSSEC."
        )

    if "80/tcp" in scan_text:
        findings.append(
            "🔹 Port 80 (HTTP)\n"
            "- Web traffic is unencrypted.\n"
            "- Recommendation: Redirect users to HTTPS."
        )

    if "110/tcp" in scan_text:
        findings.append(
            "🔹 Port 110 (POP3)\n"
            "- Email retrieval service detected.\n"
            "- Recommendation: Use POP3S or migrate to more secure protocols."
        )

    if "143/tcp" in scan_text:
        findings.append(
            "🔹 Port 143 (IMAP)\n"
            "- Email access service detected.\n"
            "- Recommendation: Enable IMAPS and require encryption."
        )

    if "443/tcp" in scan_text:
        findings.append(
            "🔹 Port 443 (HTTPS)\n"
            "- Secure encrypted web traffic.\n"
            "- Recommendation: Keep TLS certificates up to date."
        )

    if "445/tcp" in scan_text:
        findings.append(
            "🔹 Port 445 (SMB)\n"
            "- SMB can expose file sharing services.\n"
            "- Recommendation: Restrict access with firewall rules."
        )

    if "3306/tcp" in scan_text:
        findings.append(
            "🔹 Port 3306 (MySQL)\n"
            "- MySQL database detected.\n"
            "- Recommendation: Restrict network access and use strong credentials."
        )

    if "3389/tcp" in scan_text:
        findings.append(
            "🔹 Port 3389 (RDP)\n"
            "- Remote Desktop detected.\n"
            "- Recommendation: Restrict access and enable MFA."
        )

    if "5432/tcp" in scan_text:
        findings.append(
            "🔹 Port 5432 (PostgreSQL)\n"
            "- PostgreSQL database detected.\n"
            "- Recommendation: Allow access only from trusted hosts."
        )

    if "6379/tcp" in scan_text:
        findings.append(
            "🔹 Port 6379 (Redis)\n"
            "- Redis service detected.\n"
            "- Recommendation: Enable authentication and avoid exposing it publicly."
        )

    if "27017/tcp" in scan_text:
        findings.append(
            "🔹 Port 27017 (MongoDB)\n"
            "- MongoDB service detected.\n"
            "- Recommendation: Enable authentication and restrict network exposure."
        )

    if not findings:
        return (
            "⚠️ No recognized ports were found.\n\n"
            "Please provide a valid Nmap scan."
        )

    report = (
        "🛡️ JayJay AI Security Analysis\n\n"
        + "\n\n".join(findings)
        + "\n\n✅ Analysis Complete."
    )

    return report
