from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    
    # 音声入力関連の要素やAPIが使用されているかチェック
    voice_input_elements = ['input[type="speech"]', '[x-webkit-speech]']
    for selector in voice_input_elements:
        if soup.select(selector):
            return True

    # Web Speech APIの使用をチェック
    scripts = soup.find_all('script')
    for script in scripts:
        if script.string and 'SpeechRecognition' in script.string:
            return True

    print("手動確認が必要: 音声入力が許可されているか確認してください。")
    return None