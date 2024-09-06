from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # ヘルプリンクや要素を探す
    help_elements = soup.find_all(['a', 'button', 'div'], text=lambda text: text and 'ヘルプ' in text.lower())
    help_elements += soup.find_all(['a', 'button', 'div'], title=lambda title: title and 'ヘルプ' in title.lower())
    
    if help_elements:
        print("ヘルプ要素が見つかりました")
        return True
    else:
        print("ヘルプ要素が見つかりませんでした")
        return False