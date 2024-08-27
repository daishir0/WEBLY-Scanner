from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # Check for video elements with track elements
    videos_with_captions = soup.find_all('video', {'track': {'kind': 'captions'}})
    
    if videos_with_captions:
        print("Captions found for video elements")
        return True
    else:
        print("Manual check required: Verify if all prerecorded audio content in synchronized media has captions")
        return None  # Requires manual verification