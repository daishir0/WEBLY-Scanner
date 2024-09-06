from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 自動チェック: マルチポイントジェスチャーを使用する要素を探す
    multipoint_elements = soup.find_all(attrs={"data-gesture": "multipoint"})
    
    if not multipoint_elements:
        return True  # マルチポイントジェスチャーを使用する要素が見つからない場合、パス
    
    # 各マルチポイントジェスチャー要素に対して代替手段があるかチェック
    for element in multipoint_elements:
        if not has_single_pointer_alternative(element):
            print(f"Manual check required: Verify if multipoint gesture for element {element.name} with id '{element.get('id', '')}' is essential or has a single-pointer alternative.")
            return False
    
    return True

def has_single_pointer_alternative(element):
    # シングルポインタの代替手段があるかどうかを確認するロジック
    # 例: aria-controls属性や関連するボタンの存在をチェック
    return bool(element.get('aria-controls')) or bool(element.find_next('button'))