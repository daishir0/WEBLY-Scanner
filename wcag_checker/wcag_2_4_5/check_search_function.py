from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 検索フォームを探す
    search_form = soup.find('form', attrs={'role': 'search'})
    if search_form:
        return True
    
    # 検索入力フィールドを探す
    search_input = soup.find('input', attrs={'type': 'search'})
    if search_input:
        return True
    
    # 検索ボタンを探す
    search_button = soup.find(['button', 'input'], text=lambda text: 'search' in text.lower() if text else False)
    if search_button:
        return True
    
    return False