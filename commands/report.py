"""
Professional report generator.
"""


def generate_report(target: str, findings: list) -> str:
    """
    Generate a professional security assessment report.
    """

    total = len(findings)

    critical = sum(
        1 for finding in findings
        if finding.get("severity", "").lower() == "critical"
    )

    high = sum(
        1 for finding in findings
        if finding.get("severity", "").lower() == "high"
    )

    medium = sum(
        1 for finding in findings
        if finding.get("severity", "").lower() == "medium"
    )

    low = sum(
        1 for finding in findings
        if finding.get("severity", "").lower() == "low"
    )

    # Calculate a simple overall risk score
    score = (
        critical * 25 +
        high * 15 +
        medium * 8 +
        low * 3
    )

    if score > 100:
        score = 100

    if score >= 80:
        risk = "🔴 CRITICAL"
    elif score >= 60:
        risk = "🟠 HIGH"
    elif score >= 30:
        risk = "🟡 MEDIUM"
    else:
        risk = "🟢 LOW"

    report = (
        "🛡️ JayJay AI Security Assessment Report\n"
        "====================================\n\n"
        f"🎯 Target: {target}\n\n"
        "📊 Summary\n\n"
        f"Open Services : {total}\n"
        f"Critical      : {critical}\n"
        f"High          : {high}\n"
        f"Medium        : {medium}\n"
        f"Low           : {low}\n\n"
        f"Overall Risk Score : {score}/100\n"
        f"Risk Level         : {risk}\n"
    )

    # Executive Summary
    summary = "\n\nExecutive Summary\n\n"

    if critical:
        summary += (
            "Critical vulnerabilities were identified and require immediate remediation.\n"
        )

    if high:
        summary += (
            "High-risk services should be patched and hardened as soon as possible.\n"
        )

    if medium:
        summary += (
            "Several services require additional security hardening.\n"
        )

    if low:
        summary += (
            "Continue following security best practices for lower-risk services.\n"
        )

    summary += (
        f"\nOverall system risk is {risk}."
    )

    report += summary

    return report
