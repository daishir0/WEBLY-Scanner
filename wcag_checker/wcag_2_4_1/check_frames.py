from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # フレーム要素を検索
    frames = soup.find_all(['frame', 'iframe'])
    
    for frame in frames:
        if frame.get('title'):
            return True
    
    return False