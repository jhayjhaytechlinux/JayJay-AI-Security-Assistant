"""
Analyze Nmap XML scan files.
"""

from parser.nmap_xml import parse_nmap_xml
from parser.converter import parsed_to_scan_text
from commands.analyze import analyze_scan


def analyze_xml(xml_file: str) -> str:
    """
    Parse an XML file and generate the normal
    JayJay AI security report.
    """

    parsed = parse_nmap_xml(xml_file)

    scan_text = parsed_to_scan_text(parsed)

    return analyze_scan(scan_text)
