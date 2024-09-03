from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # 音量制御機能を持つ可能性のある要素を検索
    volume_controls = soup.find_all(['input'], type='range')
    
    if volume_controls:
        print("Potential volume control mechanisms found. Manual check required for functionality and independence from system volume.")
        return None  # 手動チェックが必要
    else:
        print("No obvious volume control mechanisms found.")
        return False