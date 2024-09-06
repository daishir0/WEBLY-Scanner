from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    # ここで名前がプログラム的に決定できるかをチェック
    # 例: aria-label, aria-labelledby 属性の存在を確認
    elements_with_name = soup.find_all(attrs={"aria-label": True, "aria-labelledby": True})
    if elements_with_name:
        print("Name attributes found")
        return True
    else:
        print("Name attributes not found")
        return False