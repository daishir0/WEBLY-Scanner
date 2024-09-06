from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # ステータスメッセージの存在をチェック
    status_messages = soup.find_all(['div', 'span', 'p'], attrs={'role': ['status', 'alert', 'log', 'progressbar']})
    
    return len(status_messages) > 0