from wcag_checker.utils import fetch_url, parse_html

def check(url):
    # この関数は自動化が難しいため、手動チェックを促すメッセージを表示します
    print(f"Manual check required for {url}: Verify if the audio content meets the following criteria:")
    print("1. Contains primarily speech in the foreground")
    print("2. Is not an audio CAPTCHA or audio logo")
    print("3. Is not vocalization intended to be primarily musical expression such as singing or rapping")
    
    # 常にFalseを返し、手動チェックを促します
    return False