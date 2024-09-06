from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    # エラーメッセージが具体的であるかをチェックするロジックを実装
    # 例: エラーメッセージの内容を解析
    error_messages = soup.find_all(attrs={"role": "alert"})
    for message in error_messages:
        if len(message.text.strip()) > 10:  # 具体的なメッセージの例として10文字以上
            return True
    return False