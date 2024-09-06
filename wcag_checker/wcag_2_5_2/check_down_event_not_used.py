from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # ダウンイベントを使用しているかどうかを確認
    down_events = ['onmousedown', 'ontouchstart']
    for event in down_events:
        if soup.find(attrs={event: True}):
            return False
    
    return True