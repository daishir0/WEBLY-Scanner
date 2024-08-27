# ./wcag_1_2_8/check_video_only_media.py

from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # 映像のみのメディアを検出する（例：video要素でaudio要素を持たないもの）
    video_only_media = [video for video in soup.find_all('video') if not video.find('audio')]
    
    if not video_only_media:
        print("No video-only media found")
        return True  # メディアがない場合は基準を満たしていると見なす
    
    # 時間依存メディアの代替コンテンツを確認
    for media in video_only_media:
        if not has_alternative(media):
            print("Video-only media without alternative found")
            return False
    
    print("All video-only media have alternatives")
    return True

def has_alternative(media):
    # トランスクリプトや詳細な説明へのリンクを探す
    if media.find_next('a', text=lambda t: 'transcript' in t.lower() or 'description' in t.lower()):
        return True
    
    # aria-describedby属性を確認
    if media.get('aria-describedby'):
        return True
    
    return False