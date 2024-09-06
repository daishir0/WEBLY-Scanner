from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    sections = soup.find_all(['div', 'section', 'article', 'main', 'aside', 'nav'])
    
    return len(sections) > 1