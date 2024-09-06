from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    labels = soup.find_all('label')
    
    for label in labels:
        if label.string and label.string.strip():
            return True
    
    print("テキストを含むラベルが見つかりませんでした")
    return False