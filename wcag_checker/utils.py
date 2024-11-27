import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import warnings
from urllib3.exceptions import InsecureRequestWarning

# 警告を無視する
warnings.simplefilter('ignore', InsecureRequestWarning)

def fetch_url(url):
    try:
        response = requests.get(url, verify=False)
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
def get_webdriver():
    options = Options()
    options.headless = True
    options.binary_location = "/usr/bin/google-chrome"
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--enable-logging')
    options.add_argument('--log-level=1')
    options.add_argument("--headless")

    service = Service(executable_path="/usr/bin/chromedriver")

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1920, 2160)
    
    return driver
