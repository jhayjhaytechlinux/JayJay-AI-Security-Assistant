"""
Parse Nmap XML scan files.
"""

import xml.etree.ElementTree as ET


def parse_nmap_xml(xml_file: str) -> dict:
    """
    Parse an Nmap XML file and return structured scan data.

    Returns:
        {
            "target": "...",
            "services": [
                {
                    "port": "22/tcp",
                    "service": "ssh",
                    "product": "OpenSSH",
                    "version": "8.9p1 Ubuntu"
                }
            ]
        }
    """

    tree = ET.parse(xml_file)
    root = tree.getroot()

    result = {
        "target": "Unknown Host",
        "services": [],
    }

    # Find the target IP address
    host = root.find("host")

    if host is None:
        return result

    address = host.find("address")

    if address is not None:
        result["target"] = address.attrib.get(
            "addr",
            "Unknown Host",
        )

    ports = host.find("ports")

    if ports is None:
        return result

    for port in ports.findall("port"):

        state = port.find("state")

        if state is None:
            continue

        if state.attrib.get("state") != "open":
            continue

        service = port.find("service")

        service_name = ""

        product = ""

        version = ""

        if service is not None:
            service_name = service.attrib.get("name", "")
            product = service.attrib.get("product", "")
            version = service.attrib.get("version", "")

        result["services"].append(
            {
                "port": f"{port.attrib['portid']}/{port.attrib['protocol']}",
                "service": service_name,
                "product": product,
                "version": version,
            }
        )

    return result
