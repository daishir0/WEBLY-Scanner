from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # This is a simplified check and would require manual verification
    video_elements = soup.find_all('video')
    for video in video_elements:
        if video.find_next('a', text=lambda text: 'transcript' in text.lower() if text else False):
            print("Potential media alternative (transcript) found for a video element")
            return True
    
    print("No potential media alternative found. Manual check required.")
    return False