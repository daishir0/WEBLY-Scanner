from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    # フラッシュの赤色の変化をチェックするロジックをここに実装
    # 例: 赤色の変化がないことを確認
    # ここでは仮のロジックを使用
    red_flash_change = False  # 仮の値
    if not red_flash_change:
        return True
    else:
        return False