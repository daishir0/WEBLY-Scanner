from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    links = soup.find_all('a')
    
    ambiguous_links = ['click here', 'read more', 'more', 'continue']
    for link in links:
        link_text = link.get_text().strip().lower()
        if link_text in ambiguous_links:
            return False
    
    return True