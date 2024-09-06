from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # ナビゲーションバーの一般的なセレクタを探す
    nav_selectors = ['nav', '[role="navigation"]', '.navigation', '#navigation']
    
    for selector in nav_selectors:
        nav = soup.select_one(selector)
        if nav:
            print("ナビゲーションバーが見つかりました。手動で現在のページの強調表示を確認してください。")
            return True
    
    print("ナビゲーションバーが見つかりませんでした。")
    return False