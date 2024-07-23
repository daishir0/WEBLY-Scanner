import requests
from bs4 import BeautifulSoup

def fetch_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch URL: {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception occurred while fetching URL: {e}")
        return None

def parse_html(html_content):
    return BeautifulSoup(html_content, 'html.parser')