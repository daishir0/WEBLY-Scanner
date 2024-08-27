from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # ビデオ要素を探す
    video_elements = soup.find_all('video')
    
    if not video_elements:
        print("No video elements found on the page.")
        return False
    
    for video in video_elements:
        # ビデオに対応する手話通訳のトラックがあるか確認
        sign_language_tracks = video.find_all('track', {'kind': 'sign'})
        if not sign_language_tracks:
            print(f"Video element found without sign language track: {video}")
            return False
    
    print("All video elements have associated sign language tracks.")
    return True
