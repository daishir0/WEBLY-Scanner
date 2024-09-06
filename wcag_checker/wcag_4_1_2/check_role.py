from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    # ここで役割がプログラム的に決定できるかをチェック
    # 例: role 属性の存在を確認
    elements_with_role = soup.find_all(attrs={"role": True})
    if elements_with_role:
        print("Role attributes found")
        return True
    else:
        print("Role attributes not found")
        return False