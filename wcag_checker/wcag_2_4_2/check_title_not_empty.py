from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return None
    
    soup = parse_html(html_content)
    return soup.title is not None and len(soup.title.string.strip()) > 0
