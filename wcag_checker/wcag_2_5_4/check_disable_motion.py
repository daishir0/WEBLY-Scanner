from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    # ここにモーション無効化のチェックロジックを実装
    # 例: 設定オプションが存在するかどうかを確認
    soup = parse_html(html_content)
    settings = soup.find_all(['input', 'select', 'option'])
    if any("disable motion" in setting.get_text().lower() for setting in settings):
        print("Disable motion option found")
        return True
    else:
        print("No disable motion option found")
        return False