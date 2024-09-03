from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # テキストブロックの幅を確認
    text_blocks = soup.find_all(['p', 'div', 'span'])
    for block in text_blocks:
        text = block.get_text()
        lines = text.split('\n')
        for line in lines:
            if len(line) > 80:
                print(f"Manual check required: Line exceeds 80 characters: {line[:50]}...")
                return None
    
    print("Manual check required: Verify if text blocks are no more than 80 characters wide (40 for CJK).")
    return None