from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # キーボード操作の説明を探す
    keyboard_instructions = soup.find_all(text=lambda text: 'keyboard' in text.lower() and 'exit' in text.lower())
    
    if keyboard_instructions:
        print("Manual check required: Verify if the following instructions explain how to exit from keyboard traps:")
        for instruction in keyboard_instructions:
            print(f"- {instruction.strip()}")
        return None  # 手動確認が必要
    else:
        return True  # 特別な説明が必要ない標準的な終了方法と仮定