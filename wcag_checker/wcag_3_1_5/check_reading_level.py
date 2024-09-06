from wcag_checker.utils import fetch_url, parse_html
import textstat

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    text = soup.get_text()
    
    # 固有名詞と題名を除去する処理（簡易的な実装）
    # 実際にはより高度な自然言語処理が必要
    words = text.split()
    filtered_words = [word for word in words if not word[0].isupper()]
    filtered_text = ' '.join(filtered_words)
    
    # 読解レベルの計算（英語を想定）
    reading_level = textstat.flesch_kincaid_grade(filtered_text)
    
    if reading_level <= 9:  # 中等教育前期レベル（9年間の教育）
        print(f"Reading level: {reading_level} - Passes")
        return True
    else:
        print(f"Reading level: {reading_level} - Fails")
        return False