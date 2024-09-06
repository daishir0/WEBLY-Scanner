from wcag_checker.utils import fetch_url, parse_html
import re

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 20時間以上の時間制限を示す文字列を探す
    time_limit_texts = soup.find_all(string=re.compile(r'\d+\s*(時間|hours)'))
    
    for text in time_limit_texts:
        hours = re.search(r'\d+', text)
        if hours and int(hours.group()) >= 20:
            print("20時間以上の時間制限が見つかりました。")
            return True
    
    print("20時間以上の時間制限が見つかりませんでした。")
    return False