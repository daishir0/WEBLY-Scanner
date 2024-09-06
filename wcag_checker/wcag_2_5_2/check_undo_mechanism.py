from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 取り消しメカニズムの存在を確認（例：元に戻すボタン）
    undo_keywords = ['undo', 'revert', '元に戻す', '取り消し']
    for keyword in undo_keywords:
        if soup.find(text=lambda text: keyword.lower() in text.lower() if text else False):
            return True
    
    return False