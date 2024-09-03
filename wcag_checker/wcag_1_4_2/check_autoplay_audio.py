from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # 自動再生される可能性のある要素を検索
    autoplay_elements = soup.find_all(['audio', 'video'], autoplay=True)
    
    if autoplay_elements:
        print("Autoplay audio/video elements found. Manual check required.")
        return True
    else:
        print("No autoplay audio/video elements found.")
        return False