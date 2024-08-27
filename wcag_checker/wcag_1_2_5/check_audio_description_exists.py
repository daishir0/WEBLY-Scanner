from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # 音声解説トラックの存在をチェック
    audio_description_exists = soup.find('track', {'kind': 'descriptions'}) is not None
    
    if audio_description_exists:
        print("Audio description track found")
        return True
    else:
        print("Audio description track not found")
        print("Manual check required: Verify if audio descriptions are provided for all prerecorded video content")
        return False