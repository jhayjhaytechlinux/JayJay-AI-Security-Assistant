"""
Convert parsed Nmap XML data into text that
the existing analyzer already understands.
"""


def parsed_to_scan_text(parsed_data: dict) -> str:
    """
    Convert parsed XML data into Nmap text output.
    """

    target = parsed_data.get("target", "Unknown Host")

    lines = [
        f"Nmap scan report for {target}",
        "",
    ]

    for service in parsed_data.get("services", []):

        line = (
            f"{service['port']} open "
            f"{service['product']} "
            f"{service['version']}"
        )

        lines.append(line.strip())

    return "\n".join(lines)
