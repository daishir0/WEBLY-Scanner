from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # This is a simplified check and would require manual verification
    media_elements = soup.find_all(['video', 'audio'])
    for media in media_elements:
        if media.get('aria-label') and 'alternative for text' in media.get('aria-label').lower():
            print("Media element labeled as alternative for text found")
            return True
    
    print("No media element labeled as alternative for text found. Exception condition not met.")
    return False