from wcag_checker.utils import fetch_url, parse_html
import re

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # データ保持に関する情報を探す
    preservation_patterns = [
        r'data (is|will be) preserved for (\d+) hours',
        r'information (is|will be) saved for (\d+) hours',
        r'データは(\d+)時間保持されます',
        r'情報は(\d+)時間保存されます'
    ]
    
    for pattern in preservation_patterns:
        matches = re.findall(pattern, soup.get_text(), re.IGNORECASE)
        if matches:
            hours = int(matches[0][1])
            if hours >= 20:
                print(f"20時間以上のデータ保持が確認されました: {hours}時間")
                return True
            else:
                print(f"データ保持時間が20時間未満です: {hours}時間")
                return False
    
    print("データ保持に関する情報が見つかりませんでした。手動での確認が必要です。")
    return False