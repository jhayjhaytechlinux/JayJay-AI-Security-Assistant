"""
Professional PDF report generator for
JayJay AI Security Assistant.
"""

import os
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


def generate_pdf_report(
    target,
    report_text,
    output_file=None,
):
    """
    Generate a professional PDF report.
    """

    os.makedirs("generated_reports", exist_ok=True)

    if output_file is None:

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        safe_target = (
            target.replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
            .replace(":", "_")
        )

        output_file = (
            f"generated_reports/"
            f"{safe_target}_{timestamp}.pdf"
        )

    doc = SimpleDocTemplate(output_file)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>JayJay AI Security Assessment Report</b>",
            styles["Title"],
        )
    )

    story.append(
        Paragraph(
            f"<b>Target:</b> {target}",
            styles["Heading2"],
        )
    )

    for line in report_text.split("\n"):

        if line.strip():

            story.append(
                Paragraph(
                    line.replace(" ", "&nbsp;"),
                    styles["BodyText"],
                )
            )

    doc.build(story)

    return output_file
