from wcag_checker.utils import fetch_url, parse_html
import re

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # データ復元機能を探す
    restore_button = soup.find('button', string=re.compile(r'復元|データ回復', re.I))
    restore_info = soup.find(string=re.compile(r'データは保持されます|自動的に復元されます', re.I))
    
    if restore_button or restore_info:
        print("データ復元機能が見つかりました")
        return True
    else:
        print("データ復元機能が見つかりませんでした。手動確認が必要です。")
        return None  # 手動確認が必要