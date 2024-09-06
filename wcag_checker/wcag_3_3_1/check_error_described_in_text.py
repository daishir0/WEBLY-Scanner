from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    # エラーがテキストで説明されているかをチェックするロジックを実装
    # 例: aria-describedby 属性の存在を確認
    errors_described = soup.find_all(attrs={"aria-describedby": True})
    return len(errors_described) > 0