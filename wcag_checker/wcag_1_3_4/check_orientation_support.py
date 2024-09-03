from wcag_checker.utils import fetch_url, parse_html
import re

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # メタタグのviewportの設定を確認
    viewport_meta = soup.find('meta', attrs={'name': 'viewport'})
    if viewport_meta:
        content = viewport_meta.get('content', '')
        if 'user-scalable=no' in content or re.search(r'maximum-scale=[0-9.]+', content):
            print("Viewport meta tag restricts scaling")
            return False
    
    # CSSメディアクエリの使用を確認
    style_tags = soup.find_all('style')
    for style in style_tags:
        if '@media (orientation:' in style.string:
            print("CSS media queries for orientation found")
            return True
    
    # 外部CSSファイルの確認（完全な確認には実際にCSSファイルを取得して解析する必要があります）
    link_tags = soup.find_all('link', rel='stylesheet')
    if link_tags:
        print("External CSS files found. Manual check required for orientation support.")
        return True
    
    print("No clear indication of orientation support found. Manual check recommended.")
    return False