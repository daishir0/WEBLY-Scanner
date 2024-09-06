from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
    if len(headings) == 0:
        return False
    
    print("手動確認が必要: 見出しがトピックまたは目的を適切に説明しているか確認してください。")
    for heading in headings[:5]:  # 最初の5つの見出しのみを表示
        print(f"- {heading.name}: {heading.get_text().strip()}")
    
    return None  # 手動確認が必要なため、結果は不確定