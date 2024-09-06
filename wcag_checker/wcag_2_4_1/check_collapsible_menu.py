from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 展開可能なメニューを示す一般的な属性や要素を検索
    collapsible_elements = soup.find_all(['details', 'summary'])
    aria_expanded = soup.find_all(attrs={"aria-expanded": True})
    
    return len(collapsible_elements) > 0 or len(aria_expanded) > 0