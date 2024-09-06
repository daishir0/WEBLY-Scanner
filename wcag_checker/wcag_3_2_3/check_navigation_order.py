from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    nav_elements = soup.find_all('nav')
    
    if not nav_elements:
        print("ナビゲーション要素が見つかりませんでした")
        return False
    
    print("ナビゲーション要素の順序を手動で確認する必要があります")
    print("複数のページで同じ相対的順序でナビゲーション要素が表示されているか確認してください")
    return None  # 手動確認が必要なため、Noneを返す