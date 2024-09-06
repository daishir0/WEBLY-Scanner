from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 中止メカニズムの存在を確認（例：キャンセルボタン）
    abort_keywords = ['cancel', 'abort', 'キャンセル', '中止']
    for keyword in abort_keywords:
        if soup.find(text=lambda text: keyword.lower() in text.lower() if text else False):
            return True
    
    return False