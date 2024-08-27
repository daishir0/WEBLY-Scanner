from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # 音声解説トラックの同期をチェック
    video_elements = soup.find_all('video')
    
    if not video_elements:
        print("No video elements found on the page")
        return False
    
    for video in video_elements:
        audio_description_track = video.find('track', {'kind': 'descriptions'})
        if audio_description_track:
            # トラックの存在は確認できるが、同期の正確さは自動的に判断できない
            print("Audio description track found for a video element")
            print("Manual check required: Verify if the audio description is properly synchronized with the video content")
            return None  # 手動チェックが必要
    
    print("No audio description tracks found for video elements")
    return False