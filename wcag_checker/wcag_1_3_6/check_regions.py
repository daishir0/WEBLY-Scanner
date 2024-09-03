from wcag_checker.utils import fetch_url, parse_html
from bs4 import BeautifulSoup

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 領域の目的を示す属性をチェック
    regions = soup.find_all(['header', 'nav', 'main', 'footer', 'aside', 'section'])
    
    for region in regions:
        if not (region.get('aria-label') or region.get('role')):
            print(f"領域の目的が明確でない: {region}")
            return False
    
    return True