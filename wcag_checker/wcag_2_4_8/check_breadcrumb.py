from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # パンくずリストの一般的なクラス名やID名を探す
    breadcrumb_selectors = [
        '.breadcrumb', '#breadcrumb', '[aria-label="breadcrumb"]',
        '[role="navigation"][aria-label="Breadcrumb"]'
    ]
    
    for selector in breadcrumb_selectors:
        breadcrumb = soup.select_one(selector)
        if breadcrumb:
            print("パンくずリストが見つかりました。手動で構造を確認してください。")
            return True
    
    print("パンくずリストが見つかりませんでした。")
    return False