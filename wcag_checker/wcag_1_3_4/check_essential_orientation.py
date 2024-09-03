from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False, "Failed to fetch URL content"
    
    soup = parse_html(html_content)
    
    # キーワードや特定の要素を探して、特定の方向が必要かどうかを推測
    keywords = ['piano', 'check deposit', 'landscape only', 'portrait only']
    for keyword in keywords:
        if keyword.lower() in soup.get_text().lower():
            return False, f"Possible essential orientation detected: '{keyword}' found in content"
    
    # canvas要素の存在を確認（ゲームやグラフィカルなアプリケーションの可能性）
    if soup.find('canvas'):
        return False, "Canvas element found, may require specific orientation"
    
    return True, "No clear indication of essential orientation requirement"