from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # 非インタラクティブな同期メディアやリアルタイムイベントを検出
    media_elements = soup.find_all(['video', 'audio'])
    real_time_elements = soup.find_all(['iframe'], attrs={'src': lambda x: x and ('live' in x or 'stream' in x)})
    
    if media_elements or real_time_elements:
        print("非インタラクティブな同期メディアまたはリアルタイムイベントが検出されました。例外として扱われる可能性があります。")
        return True
    
    print("例外となる要素は検出されませんでした。")
    return True