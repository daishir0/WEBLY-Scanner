from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 時間制限を延長するコントロールを探す
    extend_controls = soup.find_all(['button', 'input'], text=lambda t: t and '時間を延長' in t)
    
    if extend_controls:
        print("時間制限を延長するコントロールが見つかりました。")
        print("警告表示と延長回数の確認が必要です。手動での確認をお願いします。")
        return None
    else:
        print("時間制限を延長するコントロールが見つかりませんでした。手動での確認が必要です。")
        return False