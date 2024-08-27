from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # Check for synchronized media elements
    synchronized_media = soup.find_all(['video', 'audio'])
    
    if not synchronized_media:
        print("No synchronized media found")
        return True  # Pass if no synchronized media is present
    
    # Check if all synchronized media elements have associated extended audio description
    for media in synchronized_media:
        if not has_extended_audio_description(media):
            print(f"Synchronized media without extended audio description found: {media.get('src', 'Unknown source')}")
            return False
    
    print("All synchronized media have associated extended audio description")
    return True

def has_extended_audio_description(media_element):
    # Check for extended audio description track or source
    description_track = media_element.find('track', {'kind': 'description'})
    description_source = media_element.find('source', {'type': 'audio/description'})
    
    if description_track or description_source:
        return True
    
    return False