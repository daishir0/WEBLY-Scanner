# ./wcag_1_2_1/check_video_only.py

from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return None
    
    soup = parse_html(html_content)
    video_elements = soup.find_all('video')
    
    if not video_elements:
        print("No video-only content found")
        return True
    
    for video in video_elements:
        if not video.find('audio') and not video.find_next('a', href=True) and not video.find_next('p'):
            print("Video-only content without alternative or audio track found")
            return False
    
    print("All video-only content has alternatives or audio tracks")
    return True