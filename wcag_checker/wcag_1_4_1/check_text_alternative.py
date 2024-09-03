from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 色を使用している要素を探す（例：style属性にcolorが含まれる要素）
    color_elements = soup.find_all(lambda tag: tag.has_attr('style') and 'color' in tag['style'])
    
    for element in color_elements:
        # 色を使用している要素に対応するテキスト説明があるか確認
        if not element.string or not element.string.strip():
            return False
    
    return True