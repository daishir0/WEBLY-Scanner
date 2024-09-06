from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # フォーム要素を探す
    form_elements = soup.find_all(['input', 'select', 'textarea'])
    
    if not form_elements:
        print("No UI components found that can change settings")
        return False
    
    print("UI components that can change settings found")
    return True