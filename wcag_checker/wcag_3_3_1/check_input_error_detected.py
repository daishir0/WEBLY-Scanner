from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    # 自動的に検出されたエラーをチェックするロジックを実装
    # 例: aria-invalid 属性の存在を確認
    errors_detected = soup.find_all(attrs={"aria-invalid": "true"})
    return len(errors_detected) > 0