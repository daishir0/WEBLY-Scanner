from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    # プログラム情報と組み合わせてエラーが説明されているかをチェックするロジックを実装
    # 例: aria-live 属性の存在を確認
    programmatic_info = soup.find_all(attrs={"aria-live": "assertive"})
    return len(programmatic_info) > 0