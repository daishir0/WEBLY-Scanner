from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # アニメーション無効化機能の存在をチェック
    disable_controls = soup.find_all(['button', 'input', 'select'], text=lambda t: t and 'アニメーション' in t and ('無効' in t or '停止' in t or 'オフ' in t))
    
    if disable_controls:
        print("アニメーション無効化機能が見つかりました")
        return True
    else:
        print("アニメーション無効化機能が見つかりませんでした。手動で確認してください。")
        return False