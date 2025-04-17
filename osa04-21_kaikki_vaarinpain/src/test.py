import requests
import xml.etree.ElementTree as ET

# XML data URL from Suomen Pankki
url = "https://reports.suomenpankki.fi/WebForms/ReportViewerPage.aspx?report=/tilastot/markkina-_ja_hallinnolliset_korot/euribor_korot_today_xml_en&output=xml"

# Fetch the XML data
response = requests.get(url)

if response.status_code == 200:
    # Parse the XML content
    root = ET.fromstring(response.content)

    # Namespace handling (because the XML uses a default namespace)
    ns = {"ns": "euribor_korot_today_xml_en"}  # Update with correct namespace if needed

    # Find the correct period (yesterday's date)
    period = root.find(".//ns:period", namespaces=ns)
    if period is not None:
        rates = period.findall(".//ns:rate", namespaces=ns)

        for rate in rates:
            if rate.attrib.get("name") == "12 month (act/360)":
                euribor_12m = rate.find("./ns:intr", namespaces=ns)
                if euribor_12m is not None:
                    print(f"Yesterday's 12-month Euribor rate: {euribor_12m.attrib['value']}%")
                else:
                    print("Interest rate value not found.")
                break
        else:
            print("12-month Euribor rate not found.")
    else:
        print("No period data found in XML.")
else:
    print(f"Failed to retrieve XML data. HTTP Status Code: {response.status_code}")
