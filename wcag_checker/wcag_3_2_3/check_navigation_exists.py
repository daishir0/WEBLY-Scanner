from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    nav_elements = soup.find_all('nav')
    
    if nav_elements:
        print(f"{len(nav_elements)}個のナビゲーション要素が見つかりました")
        return True
    else:
        print("ナビゲーション要素が見つかりませんでした")
        return False