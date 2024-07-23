from wcag_checker.utils import fetch_url, parse_html

GENERIC_TITLES = ['Untitled', 'Page Title', 'New Page']

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return None
    
    soup = parse_html(html_content)
    if soup.title and soup.title.string:
        return soup.title.string.strip() not in GENERIC_TITLES
    return False