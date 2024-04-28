import os
import json
import re
from flask import Flask, render_template, request


app = Flask(__name__)

# Function to extract CVE data from JSON file


def extract_cve_data(cve_file):
    with open(cve_file, 'r') as file:
        cve_data = json.load(file)
    return cve_data

# Function to list all CVE files


def list_all_cves(base_path):
    all_cves = []
    for year_folder in os.listdir(base_path):
        year_folder_path = os.path.join(base_path, year_folder)
        if os.path.isdir(year_folder_path):
            for cve_number_folder in os.listdir(year_folder_path):
                cve_number_folder_path = os.path.join(
                    year_folder_path, cve_number_folder)
                if os.path.isdir(cve_number_folder_path):
                    for filename in os.listdir(cve_number_folder_path):
                        if filename.endswith('.json'):
                            cve_path = os.path.join(
                                cve_number_folder_path, filename)
                            all_cves.append(cve_path)
    return all_cves

# Function to extract versions from description


def extract_versions_from_description(description):
    version_pattern = r'(\d+(\.\d+)+)\s*(?:(?:and)?\s+earlier)?'

    matches = re.findall(version_pattern, description, re.IGNORECASE)
    versions = []
    for match in matches:
        version = ' '.join(match).strip()
        version = re.sub(r'\.\d+$', '', version)
        versions.append(version)
    return versions

# Function to filter CVEs by vendor, product, and version


def filter_cves_by_vendor_product_and_version(vendors, products, versions):
    filtered_cves = []
    for cve_file in all_cve_files:
        cve_data = extract_cve_data(cve_file)
        affected = cve_data.get('containers', {}).get(
            'cna', {}).get('affected', [{}])[0]
        description = cve_data.get('containers', {}).get(
            'cna', {}).get('descriptions', [{}])[0].get('value', 'N/A')
        extracted_versions = extract_versions_from_description(description)
        for vendor in vendors:
            for product in products:
                for version in versions:
                    if affected.get('vendor', '').lower() == vendor.lower():
                        if not product or affected.get('product', '').lower() == product.lower():
                            if not version or any(version.lower() in extracted.lower() for extracted in extracted_versions):
                                filtered_cves.append({
                                    'cve_id': cve_data['cveMetadata']['cveId'],
                                    'vendor': affected.get('vendor', 'N/A'),
                                    'product_name': affected.get('product', 'N/A'),
                                    'version': ', '.join(extracted_versions) if extracted_versions else 'N/A',
                                    'severity_level': cve_data.get('cveMetadata', {}).get('severity', 'N/A'),
                                    'description': description,
                                    'cve_link': f"https://nvd.nist.gov/vuln/detail/{cve_data['cveMetadata']['cveId']}"
                                })
    return filtered_cves


# Base path for CVE files
base_path = '/Users/zoilaloja/Documents/GitHub/cvelistV5/cves'
all_cve_files = list_all_cves(base_path)

# Route for home page


@app.route('/', methods=['GET', 'POST'])
def index():
    cve_info = []
    if request.method == 'POST':
        vendors = request.form.getlist('vendor')
        products = request.form.getlist('product_name')
        versions = request.form.getlist('version')
        cve_info = filter_cves_by_vendor_product_and_version(
            vendors, products, versions)
    return render_template('index.html', cve_info=cve_info)

# Route for setup page


@app.route('/setup')
def setup():
    return render_template('setup.html')


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
