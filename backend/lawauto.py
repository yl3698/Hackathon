'''
Automatic Web Scraper that gets all the newest cases from New York State
'''

import requests
from bs4 import BeautifulSoup

def write_and_print(case_name, full_case_url, case_content):
    file_path = "C:/Users/nairv/Downloads/firstpage.txt"
    with open(file_path, 'a') as file:
        # Write the text to the file
        file.write(case_name + "\n")
        file.write(full_case_url + "\n")
        file.write(case_content + "\n\n")

    print(f'Case Name: {case_name}')
    print(f'Case URL: {full_case_url}')
    print('Case Content:')
    print(case_content)
    print('-' * 80)

def get_case_details(url):
    list = []
    x=0
    # Send a GET request to the URL
    page = requests.get(url)

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find all table rows with case details (assuming they are in a table)
    case_rows = soup.find_all('tr')

    # Iterate over each case row
    for case_row in case_rows:
        # Find all 'td' tags - assuming the first 'td' contains the case name and the hyperlink
        tds = case_row.find_all('td')
        if tds:
            if x==0: 
                x+=1
                continue
            # Get the case name and hyperlink
            case_name = tds[0].get_text(strip=True)
            hyperlink_tag = tds[0].find('a', href=True)
            if hyperlink_tag:
                # Get the URL of the case details
                case_url = hyperlink_tag['href'][2:]
                full_case_url = f'https://www.nycourts.gov/reporter{case_url}'
                # Fetch the case details page
                case_page = requests.get(full_case_url)
                case_soup = BeautifulSoup(case_page.content, 'html.parser')
                # Find all paragraph tags and extract their text
                paragraphs = case_soup.find_all('p')
                case_content = '\n'.join(paragraph.text for paragraph in paragraphs)

                write_and_print(case_name, full_case_url, case_content)

    return [case_name, full_case_url, case_content]

# The base URL containing the cases
base_url = 'https://www.nycourts.gov/reporter/slipidx/aidxtable_1.shtml'

# Start scraping
get_case_details(base_url)