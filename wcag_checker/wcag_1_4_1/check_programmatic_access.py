from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # aria-labelやaria-describedbyなどの属性を持つ要素を探す
    aria_elements = soup.find_all(lambda tag: tag.has_attr('aria-label') or tag.has_attr('aria-describedby'))
    
    # alt属性を持つimg要素を探す
    img_elements = soup.find_all('img', alt=True)
    
    return len(aria_elements) > 0 or len(img_elements) > 0