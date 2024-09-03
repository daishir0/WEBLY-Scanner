from wcag_checker.utils import fetch_url, parse_html
from bs4 import BeautifulSoup

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # アイコンの目的を示す属性をチェック
    icons = soup.find_all(['i', 'span', 'img'], class_=lambda x: x and 'icon' in x)
    
    for icon in icons:
        if not (icon.get('aria-label') or icon.get('title') or icon.get('alt')):
            print(f"アイコンの目的が明確でない: {icon}")
            return False
    
    return True