from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 目次を示す可能性のある要素を探す
    toc_indicators = ['table of contents', '目次', 'contents', 'index']
    for indicator in toc_indicators:
        toc_element = soup.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'nav'], 
                                text=lambda text: indicator in text.lower() if text else False)
        if toc_element:
            return True
    
    return False