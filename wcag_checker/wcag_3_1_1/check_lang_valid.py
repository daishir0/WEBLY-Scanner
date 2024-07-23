from wcag_checker.utils import fetch_url, parse_html
import langcodes

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    lang = soup.html.get('lang') if soup.html else None
    if not lang:
        return False
    
    try:
        langcodes.get(lang)
        return True
    except ValueError:
        return False