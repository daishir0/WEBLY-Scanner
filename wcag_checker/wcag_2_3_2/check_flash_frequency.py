from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    # フラッシュの頻度をチェックするロジックをここに実装
    # 例: フラッシュの頻度が1秒間に3回以下であることを確認
    # ここでは仮のロジックを使用
    flash_frequency = 2  # 仮の値
    if flash_frequency <= 3:
        return True
    else:
        return False