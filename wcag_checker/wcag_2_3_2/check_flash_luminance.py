from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    # フラッシュの相対輝度をチェックするロジックをここに実装
    # 例: 相対輝度の変化が10%以上でないことを確認
    # ここでは仮のロジックを使用
    luminance_change = 0.05  # 仮の値
    if luminance_change < 0.1:
        return True
    else:
        return False