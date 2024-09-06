from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLのコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # フォームの存在を確認
    forms = soup.find_all('form')
    if not forms:
        print("フォームが見つかりません")
        return False
    
    # エラー検出とユーザーへの修正機会の提供を自動的に判断することは困難なため、手動チェックが必要
    print(f"手動チェックが必要です: {url}のフォームでエラー検出と修正機会が提供されていることを確認してください。")
    return None  # 手動チェックが必要なため、Noneを返す