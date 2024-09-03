from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # ロゴや必須の画像テキストの検出
    essential_images = soup.find_all('img', class_=['logo', 'essential-text'])
    if essential_images:
        print("ロゴまたは必須の画像テキストが検出されました")
        return True
    
    print("ロゴまたは必須の画像テキストは検出されませんでした")
    print("手動確認が必要: 画像テキストが情報伝達に不可欠かどうか確認してください")
    return False