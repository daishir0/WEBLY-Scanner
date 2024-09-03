from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # HTMLの場合、autocomplete属性のサポートを確認
    if soup.find('input', attrs={'autocomplete': True}):
        return True
    
    # 他の技術（例：WAI-ARIA）のサポートも確認可能
    # ここでは簡略化のため、HTMLのautocomplete属性のみをチェック
    
    return False