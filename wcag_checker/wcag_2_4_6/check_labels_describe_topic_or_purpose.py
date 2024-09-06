from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    labels = soup.find_all('label')
    
    if len(labels) == 0:
        return False
    
    print("手動確認が必要: ラベルがトピックまたは目的を適切に説明しているか確認してください。")
    for label in labels[:5]:  # 最初の5つのラベルのみを表示
        print(f"- Label: {label.get_text().strip()}")
    
    return None  # 手動確認が必要なため、結果は不確定