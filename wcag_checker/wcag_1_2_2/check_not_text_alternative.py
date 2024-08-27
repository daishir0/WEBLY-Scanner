from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # Check for media elements with aria-label indicating they are alternatives
    media_alternatives = soup.find_all(['video', 'audio'], {'aria-label': lambda x: 'alternative' in x.lower() if x else False})
    
    if media_alternatives:
        print("Manual check required: Verify if media labeled as alternatives are clearly labeled and do not require captions")
        return None  # Requires manual verification
    else:
        print("No media elements found labeled as alternatives")
        return True