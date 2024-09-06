from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    focusable_elements = soup.find_all(['a', 'button', 'input', 'select', 'textarea'])
    
    # 順次ナビゲーション可能かどうかを簡易的にチェック
    return len(focusable_elements) > 0