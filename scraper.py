import requests
from bs4 import BeautifulSoup
import time

def fetch_data_from_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"Error fetching {url}. Reason: {e}")
        return None

def extract_data(content):
    soup = BeautifulSoup(content, 'html.parser')
    data = soup.find('div', class_='target-class').text
    return data

def scrape_website(base_url, num_pages=10):
    all_data = []
    for page in range(1, num_pages + 1):
        content = fetch_data_from_page(base_url + str(page))
        if content:
            data = extract_data(content)
            all_data.append(data)
            time.sleep(5)
    return all_data
