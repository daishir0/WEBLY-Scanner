from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # カスタマイズ可能な画像テキストの検出
    customizable_images = soup.find_all('img', class_='customizable-text')
    if customizable_images:
        print("カスタマイズ可能な画像テキストが検出されました")
        return True
    
    print("カスタマイズ可能な画像テキストは検出されませんでした")
    print("手動確認が必要: 画像テキストがユーザーの要件に応じてカスタマイズ可能かどうか確認してください")
    return False