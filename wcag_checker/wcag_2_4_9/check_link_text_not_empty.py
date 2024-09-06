from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    links = soup.find_all('a')
    
    for link in links:
        if not link.text.strip():
            return False
    
    return True