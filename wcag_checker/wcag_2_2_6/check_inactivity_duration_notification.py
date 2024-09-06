from wcag_checker.utils import fetch_url, parse_html
import re

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # 非アクティブ状態の継続時間に関する通知を探す
    inactivity_patterns = [
        r'inactive for (\d+) (minutes|hours)',
        r'session will expire after (\d+) (minutes|hours) of inactivity',
        r'自動的にログアウトされます。(\d+)(分|時間)',
        r'(\d+)(分|時間)間操作がない場合、セッションが終了します'
    ]
    
    for pattern in inactivity_patterns:
        matches = re.findall(pattern, soup.get_text(), re.IGNORECASE)
        if matches:
            print(f"非アクティブ状態の継続時間に関する通知が見つかりました: {matches[0]}")
            return True
    
    print("非アクティブ状態の継続時間に関する通知が見つかりませんでした。手動での確認が必要です。")
    return False