from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 関連リンクセクションを探す
    related_sections = soup.find_all(['div', 'nav', 'section'], 
                                     text=lambda text: 'related' in text.lower() if text else False)
    if related_sections:
        return True
    
    # ナビゲーションメニューを探す
    nav_elements = soup.find_all('nav')
    if len(nav_elements) > 1:  # メインナビゲーション以外のナビゲーションがある場合
        return True
    
    return False