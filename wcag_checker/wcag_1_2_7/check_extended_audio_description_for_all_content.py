from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # Find all video elements
    video_elements = soup.find_all('video')
    
    if not video_elements:
        print("No video elements found")
        return True  # Pass if no videos are present
    
    # Check if all video elements have associated audio description
    for video in video_elements:
        if not has_audio_description(video):
            print(f"Video without extended audio description found: {video.get('src', 'Unknown source')}")
            return False
    
    print("All videos have associated extended audio description")
    return True

def has_audio_description(video_element):
    # Check for audio description track
    description_track = video_element.find('track', {'kind': 'description'})
    if description_track:
        return True
    
    # Check for separate audio description source
    description_source = video_element.find('source', {'type': 'audio/description'})
    if description_source:
        return True
    
    return False