from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    links = soup.find_all('a')
    
    for link in links:
        link_text = link.get_text().strip()
        if not link_text:
            continue
        
        if len(link_text) > 1 and not link_text.lower() in ['click here', 'read more', 'more', 'continue']:
            return True
    
    return False