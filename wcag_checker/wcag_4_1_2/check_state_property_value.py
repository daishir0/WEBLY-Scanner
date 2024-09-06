from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    # ここで状態、プロパティ、および値がプログラム的に設定できるかをチェック
    # 例: aria-checked, aria-expanded 属性の存在を確認
    elements_with_state = soup.find_all(attrs={"aria-checked": True, "aria-expanded": True})
    if elements_with_state:
        print("State, property, and value attributes found")
        return True
    else:
        print("State, property, and value attributes not found")
        return False