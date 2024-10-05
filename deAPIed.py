import csv
import xml.etree.ElementTree as ET
import json
import re

def extract_json_from_http_response(response_text):
    # Try to split by double newline 
    parts = response_text.split('\n\n', 1)
    if len(parts) == 2:
        body = parts[1].strip()  # The second part should be the body (JSON part)
        try:
            # Return the parsed JSON from the body if valid
            return json.loads(body)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
    return None

def process_burp_export(input_file, output_csv):
    # Parse the XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Prepare CSV for writing
    with open(output_csv, mode='w', newline='') as csv_file:
        # Adjust these fieldnames to match the JSON keys you want to extract
        fieldnames = ['id', 'email', 'username', 'password', 'hashed_password', 'name', 'vin', 'address', 'ip_address', 'phone', 'obtained_from', 'success']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate through each <response> tag
        for response_tag in root.findall('.//response'):
            # Extract the CDATA section containing the HTTP response
            cdata = response_tag.text

            if cdata:
                # Extract JSON from the HTTP response inside the CDATA
                json_data = extract_json_from_http_response(cdata)

                # Only proceed if valid JSON was extracted
                if json_data and 'entry' in json_data:
                    # Extract the specific entry that contains relevant data
                    entry_data = json_data['entry']

                    # Write the entry data into the CSV file
                    writer.writerow(entry_data)

if __name__ == "__main__":
    input_file = "input.xml"  # Replace with your input file path
    output_csv = "output.csv"       # Replace with your desired output CSV file path
    process_burp_export(input_file, output_csv)
