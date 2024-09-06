from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    # ここで変更通知がユーザーエージェントに提供されるかをチェック
    # 例: aria-live 属性の存在を確認
    elements_with_notification = soup.find_all(attrs={"aria-live": True})
    if elements_with_notification:
        print("Notification attributes found")
        return True
    else:
        print("Notification attributes not found")
        return False