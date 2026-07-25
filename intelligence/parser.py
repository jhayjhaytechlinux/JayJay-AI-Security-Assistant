"""
Parses service banners from Nmap output.
"""


def extract_services(scan_text: str) -> list:
    """
    Extract service names from an Nmap scan.
    Returns a list such as:
    ["openssh", "apache", "nginx", "mysql"]
    """

    services = []

    text = scan_text.lower()

    if "openssh" in text:
        services.append("openssh")

    if "apache" in text:
        services.append("apache")

    if "nginx" in text:
        services.append("nginx")

    if "mysql" in text:
        services.append("mysql")

    if "postgres" in text:
        services.append("postgresql")

    if "redis" in text:
        services.append("redis")

    if "mongodb" in text:
        services.append("mongodb")

    return services
