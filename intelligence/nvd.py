"""
National Vulnerability Database (NVD) client
for JayJay AI Security Assistant.
"""

import requests

NVD_API = "https://services.nvd.nist.gov/rest/json/cves/2.0"


def search_nvd(keyword, results=5):
    """
    Search the National Vulnerability Database.

    Returns a list of normalized CVE dictionaries.
    """

    params = {
        "keywordSearch": keyword,
        "resultsPerPage": results,
    }

    try:

        response = requests.get(
            NVD_API,
            params=params,
            timeout=20,
        )

        response.raise_for_status()

        data = response.json()

        output = []

        vulnerabilities = data.get(
            "vulnerabilities",
            [],
        )

        for item in vulnerabilities:

            cve = item.get("cve", {})

            cve_id = cve.get("id", "Unknown")

            descriptions = cve.get(
                "descriptions",
                [],
            )

            description = "No description available."

            for d in descriptions:

                if d.get("lang") == "en":

                    description = d.get(
                        "value",
                        description,
                    )

                    break

            severity = "Unknown"
            cvss = "N/A"

            metrics = cve.get("metrics", {})

            if metrics.get("cvssMetricV31"):

                metric = metrics["cvssMetricV31"][0]

                severity = metric["cvssData"]["baseSeverity"]
                cvss = str(
                    metric["cvssData"]["baseScore"]
                )

            elif metrics.get("cvssMetricV30"):

                metric = metrics["cvssMetricV30"][0]

                severity = metric["cvssData"]["baseSeverity"]
                cvss = str(
                    metric["cvssData"]["baseScore"]
                )

            elif metrics.get("cvssMetricV2"):

                metric = metrics["cvssMetricV2"][0]

                severity = metric["baseSeverity"]
                cvss = str(metric["cvssData"]["baseScore"])

            output.append(
                {
                    "cve": cve_id,
                    "severity": severity,
                    "cvss": cvss,
                    "description": description,
                    "recommendation": (
                        "Review the official NVD advisory "
                        "and apply the latest vendor patches."
                    ),
                }
            )

        return output

    except Exception as e:

        print(f"NVD lookup failed: {e}")

        return []
