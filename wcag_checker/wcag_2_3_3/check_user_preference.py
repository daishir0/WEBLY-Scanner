from wcag_checker.utils import fetch_url, parse_html
import re

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    # CSSファイルのURLを抽出
    soup = parse_html(html_content)
    css_links = soup.find_all('link', rel='stylesheet')
    
    for link in css_links:
        css_url = link.get('href')
        if css_url:
            css_content = fetch_url(css_url)
            if css_content and '@media (prefers-reduced-motion)' in css_content:
                print("prefers-reduced-motionメディアクエリが見つかりました")
                return True
    
    print("prefers-reduced-motionメディアクエリが見つかりませんでした。手動で確認してください。")
    return False