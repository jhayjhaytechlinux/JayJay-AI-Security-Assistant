"""
Analyze Nmap scan results.
"""


def analyze_scan(scan_text: str) -> str:
    """
    Analyze a simple Nmap scan and return
    a human-readable security assessment.
    """

    findings = []

    if "22/tcp" in scan_text:
        findings.append(
            "🔹 Port 22 (SSH)\n"
            "- Used for secure remote administration.\n"
            "- Recommendation: Disable password login and use SSH keys."
        )

    if "21/tcp" in scan_text:
        findings.append(
            "🔹 Port 21 (FTP)\n"
            "- FTP transmits data in plaintext.\n"
            "- Recommendation: Replace FTP with SFTP."
        )

    if "23/tcp" in scan_text:
        findings.append(
            "🔹 Port 23 (Telnet)\n"
            "- Telnet is insecure.\n"
            "- Recommendation: Disable Telnet immediately."
        )

    if "80/tcp" in scan_text:
        findings.append(
            "🔹 Port 80 (HTTP)\n"
            "- Web traffic is unencrypted.\n"
            "- Recommendation: Redirect users to HTTPS."
        )

    if "443/tcp" in scan_text:
        findings.append(
            "🔹 Port 443 (HTTPS)\n"
            "- Secure encrypted web traffic."
        )

    if "445/tcp" in scan_text:
        findings.append(
            "🔹 Port 445 (SMB)\n"
            "- SMB can expose file sharing services.\n"
            "- Recommendation: Restrict access with firewall rules."
        )

    if "3389/tcp" in scan_text:
        findings.append(
            "🔹 Port 3389 (RDP)\n"
            "- Remote Desktop detected.\n"
            "- Recommendation: Restrict access and enable MFA."
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
