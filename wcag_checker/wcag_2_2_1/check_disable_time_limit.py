from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 時間制限を無効化するコントロールを探す
    disable_controls = soup.find_all(['button', 'input', 'select'], text=lambda t: t and '時間制限を無効化' in t)
    
    if disable_controls:
        print("時間制限を無効化するコントロールが見つかりました。")
        return True
    else:
        print("時間制限を無効化するコントロールが見つかりませんでした。手動での確認が必要です。")
        return False