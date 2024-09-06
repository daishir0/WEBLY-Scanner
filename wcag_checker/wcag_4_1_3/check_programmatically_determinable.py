from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # role属性とaria-*属性の使用をチェック
    status_messages = soup.find_all(['div', 'span', 'p'], attrs={'role': ['status', 'alert', 'log', 'progressbar']})
    
    for message in status_messages:
        if message.has_attr('role') or any(attr.startswith('aria-') for attr in message.attrs):
            return True
    
    return False