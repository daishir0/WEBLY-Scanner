from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
    current_level = 0
    for heading in headings:
        level = int(heading.name[1])
        if level > current_level + 1:
            print(f"警告: 見出しレベルが飛んでいます。{heading.name}: {heading.text}")
        current_level = level
    
    print("手動確認が必要: 見出しの階層構造が適切かどうか確認してください。")
    return None  # 手動確認が必要なため、自動判定は不可能