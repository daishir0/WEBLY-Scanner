from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # Check for video or audio elements
    media_elements = soup.find_all(['video', 'audio'])
    
    if media_elements:
        print("Synchronized media found")
        return True
    else:
        print("No synchronized media found, criterion may not apply")
        return None  # Criterion may not apply