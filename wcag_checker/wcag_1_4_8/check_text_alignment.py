from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # テキストの配置を確認
    justified_elements = soup.find_all(style=lambda value: value and 'text-align: justify' in value)
    if justified_elements:
        print("Failure: Found justified text alignment.")
        return False
    
    style_tags = soup.find_all('style')
    for style in style_tags:
        if 'text-align: justify' in style.string:
            print("Failure: Found justified text alignment in CSS.")
            return False
    
    print("Manual check required: Verify that text is not justified (aligned to both left and right margins).")
    return None