from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
    print("手動確認が必要: 各見出しがセクションの内容を適切に表現しているか確認してください。")
    for heading in headings:
        print(f"見出し: {heading.text}")
    
    return None  # 手動確認が必要なため、自動判定は不可能