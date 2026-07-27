"""
Risk prioritization engine.

Calculates an overall priority score for findings.
"""


def calculate_priority(findings):
    """
    Sort findings from highest risk to lowest.
    """

    severity_weight = {
        "Critical": 4,
        "High": 3,
        "Medium": 2,
        "Low": 1,
    }

    for finding in findings:

        score = severity_weight.get(
            finding["severity"],
            1,
        )

        if finding["service"] in (
            "Telnet",
            "FTP",
            "SMB",
            "RDP",
        ):
            score += 2

        finding["priority_score"] = score

    findings.sort(
        key=lambda x: x["priority_score"],
        reverse=True,
    )

    return findings


def build_priority_summary(findings):
    """
    Generate a human-readable priority section.
    """

    findings = calculate_priority(findings)

    report = (
        "🔥 Priority Remediation Plan\n"
        "====================================\n\n"
    )

    for index, finding in enumerate(findings, start=1):

        report += (
            f"{index}. {finding['service']}\n"
            f"Severity : {finding['severity']}\n"
            f"Priority : {finding['priority_score']}\n\n"
        )

    return report
