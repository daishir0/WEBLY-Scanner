from wcag_checker.utils import fetch_url, parse_html
import re

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # セッション期限切れに関する情報を探す
    session_info = soup.find(string=re.compile(r'セッション|タイムアウト|ログアウト', re.I))
    
    if session_info:
        print("セッション期限切れの検出メカニズムが見つかりました")
        return True
    else:
        print("セッション期限切れの検出メカニズムが見つかりませんでした。手動確認が必要です。")
        return None  # 手動確認が必要