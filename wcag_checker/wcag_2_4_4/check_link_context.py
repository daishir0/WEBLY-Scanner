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
        
        context = link.parent.get_text().strip()
        if len(context) > len(link_text):
            return True
    
    return False