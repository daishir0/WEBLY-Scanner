from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 自動チェック: パス型ジェスチャーを使用する要素を探す
    path_based_elements = soup.find_all(attrs={"data-gesture": "path-based"})
    
    if not path_based_elements:
        return True  # パス型ジェスチャーを使用する要素が見つからない場合、パス
    
    # 各パス型ジェスチャー要素に対して代替手段があるかチェック
    for element in path_based_elements:
        if not has_single_pointer_alternative(element):
            print(f"Manual check required: Verify if path-based gesture for element {element.name} with id '{element.get('id', '')}' is essential or has a single-pointer alternative.")
            return False
    
    return True

def has_single_pointer_alternative(element):
    # シングルポインタの代替手段があるかどうかを確認するロジック
    # 例: aria-controls属性や関連するボタンの存在をチェック
    return bool(element.get('aria-controls')) or bool(element.find_next('button'))