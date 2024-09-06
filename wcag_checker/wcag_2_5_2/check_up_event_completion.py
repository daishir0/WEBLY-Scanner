from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # アップイベントを使用しているかどうかを確認
    up_events = ['onmouseup', 'ontouchend', 'onclick']
    for event in up_events:
        if soup.find(attrs={event: True}):
            return True
    
    return False