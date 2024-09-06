from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # エラーメッセージや提案を含む可能性のある要素を探す
    error_elements = soup.find_all(['div', 'span', 'p'], class_=['error', 'warning', 'suggestion', 'help'])
    
    if error_elements:
        print("エラーメッセージまたは提案を含む可能性のある要素が見つかりました")
        return True
    else:
        print("エラーメッセージまたは提案を含む要素が見つかりません。手動確認が必要です")
        return None