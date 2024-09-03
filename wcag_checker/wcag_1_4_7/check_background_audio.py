from wcag_checker.utils import fetch_url, parse_html

def check(url):
    # この関数も自動化が難しいため、手動チェックを促すメッセージを表示します
    print(f"Manual check required for {url}: Verify if the audio content meets one of the following criteria:")
    print("1. No background sounds")
    print("2. Background sounds can be turned off")
    print("3. Background sounds are at least 20 decibels lower than the foreground speech content")
    print("   (with the exception of occasional sounds that last for only one or two seconds)")
    
    # 常にFalseを返し、手動チェックを促します
    return False