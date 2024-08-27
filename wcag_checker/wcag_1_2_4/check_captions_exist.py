from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # Check for video elements with captions
    video_elements = soup.find_all('video')
    for video in video_elements:
        if video.find('track', attrs={'kind': 'captions'}):
            print("Captions found for live video content")
            return True
    
    print("No captions found for live video content")
    return False