from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    input_fields = soup.find_all('input')
    for field in input_fields:
        if not field.get('id') and not field.get('name') and not field.get('aria-label'):
            return False
    
    return True