from wcag_checker.utils import fetch_url, parse_html
from bs4 import BeautifulSoup

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # UIコンポーネントの目的を示す属性をチェック
    ui_components = soup.find_all(['button', 'input', 'select', 'textarea'])
    
    for component in ui_components:
        if not (component.get('aria-label') or component.get('title') or component.get('alt')):
            print(f"UIコンポーネントの目的が明確でない: {component}")
            return False
    
    return True