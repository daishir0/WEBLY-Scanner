from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # 音声のみのライブコンテンツの存在を確認
    audio_elements = soup.find_all(['audio', 'embed', 'object'], {'src': True})
    
    if not audio_elements:
        print("No live audio-only content found")
        return True  # 音声コンテンツがない場合は基準を満たしていると見なす
    
    # 代替コンテンツの存在を確認
    for audio in audio_elements:
        if not has_alternative_content(audio, soup):
            print(f"No alternative content found for audio element: {audio}")
            return False
    
    print("Alternative content found for all audio elements")
    return True

def has_alternative_content(audio_element, soup):
    # キャプションや代替テキストの存在を確認
    if audio_element.find_next('track', {'kind': 'captions'}):
        return True
    if audio_element.find_next('a', text=lambda t: t and 'transcript' in t.lower()):
        return True
    
    # NOTE: この実装は簡略化されています。実際には、より複雑なチェックが必要になる場合があります。
    
    return False