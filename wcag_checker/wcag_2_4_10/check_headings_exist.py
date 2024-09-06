from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    sections = soup.find_all(['div', 'section', 'article', 'main', 'aside', 'nav'])
    
    for section in sections:
        if not section.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            return False
    
    return True