from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # Check for the presence of extended audio description
    # This is a simplified check and may need to be adapted based on specific implementations
    audio_description_elements = soup.find_all(['track', 'audio'], {'kind': 'description'})
    
    if audio_description_elements:
        print("Extended audio description found")
        return True
    else:
        print("No extended audio description found")
        return False