from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 時間制限を調整するコントロールを探す
    adjust_controls = soup.find_all(['input', 'select'], attrs={'type': 'range', 'min': True, 'max': True})
    
    if adjust_controls:
        for control in adjust_controls:
            min_value = float(control.get('min', 0))
            max_value = float(control.get('max', 0))
            if max_value >= min_value * 10:
                print("時間制限を十分に調整できるコントロールが見つかりました。")
                return True
    
    print("時間制限を十分に調整できるコントロールが見つかりませんでした。手動での確認が必要です。")
    return False