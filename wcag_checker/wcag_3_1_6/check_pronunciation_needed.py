from wcag_checker.utils import fetch_url, parse_html
import re

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    text = soup.get_text()
    
    # 同音異義語や発音が重要な単語のパターンを探す
    patterns = [
        r'\b(read|lead|wind|bass|dove|tear|bow|row|sow)\b',  # 英語の同音異義語の例
        r'\b(kanji|hanzi|hanja)\b',  # 漢字に関する単語
        r'\b(heteronym|homograph)\b'  # 発音が重要な単語
    ]
    
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            print(f"Words that may need pronunciation information found: {re.findall(pattern, text, re.IGNORECASE)}")
            print("Manual check required: Verify if these words need pronunciation information in the given context.")
            return False
    
    return True