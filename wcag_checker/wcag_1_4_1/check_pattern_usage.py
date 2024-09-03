from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # パターンを使用している要素を探す（例：background-imageプロパティを持つ要素）
    pattern_elements = soup.find_all(lambda tag: tag.has_attr('style') and 'background-image' in tag['style'])
    
    return len(pattern_elements) > 0