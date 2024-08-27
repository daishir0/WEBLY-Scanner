# ./wcag_1_2_8/check_synchronized_media.py

from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # 同期したメディアを検出する（例：video要素）
    synchronized_media = soup.find_all('video')
    
    if not synchronized_media:
        print("No synchronized media found")
        return True  # メディアがない場合は基準を満たしていると見なす
    
    # 時間依存メディアの代替コンテンツを確認
    for media in synchronized_media:
        if not has_alternative(media):
            print("Synchronized media without alternative found")
            return False
    
    print("All synchronized media have alternatives")
    return True

def has_alternative(media):
    # トランスクリプトや詳細な説明へのリンクを探す
    if media.find_next('a', text=lambda t: 'transcript' in t.lower() or 'description' in t.lower()):
        return True
    
    # aria-describedby属性を確認
    if media.get('aria-describedby'):
        return True
    
    return False