from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # 補足コンテンツの存在を確認（簡易的な実装）
    # 実際にはより高度な解析が必要
    supplemental_indicators = ['summary', 'explanation', 'simplified version']
    
    for indicator in supplemental_indicators:
        if soup.find(text=lambda text: indicator in text.lower()):
            print(f"Supplemental content found: {indicator}")
            return True
    
    print("No supplemental content found")
    return False