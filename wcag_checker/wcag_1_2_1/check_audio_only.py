# ./wcag_1_2_1/check_audio_only.py

from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return None
    
    soup = parse_html(html_content)
    audio_elements = soup.find_all('audio')
    
    if not audio_elements:
        print("No audio-only content found")
        return True
    
    for audio in audio_elements:
        if not audio.find_next('a', href=True) and not audio.find_next('p'):
            print("Audio-only content without alternative found")
            return False
    
    print("All audio-only content has alternatives")
    return True