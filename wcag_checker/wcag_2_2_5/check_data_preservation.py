from wcag_checker.utils import fetch_url, parse_html
import re

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # データ保存機能を探す
    save_button = soup.find('button', string=re.compile(r'保存|一時保存', re.I))
    auto_save_info = soup.find(string=re.compile(r'自動保存', re.I))
    
    if save_button or auto_save_info:
        print("データ保存機能が見つかりました")
        return True
    else:
        print("データ保存機能が見つかりませんでした。手動確認が必要です。")
        return None  # 手動確認が必要