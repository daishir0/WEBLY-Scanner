from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # フォーカス時のみ有効なショートカットを探す
    # 注: この自動チェックは限定的で、多くの場合手動確認が必要
    focus_shortcuts = soup.find_all(attrs={'data-shortcut-focus': True})
    
    if focus_shortcuts:
        print("Found potential focus-only shortcuts. Manual verification required.")
        return True
    else:
        print("Manual check required: Verify if character key shortcuts are only active when the component has focus.")
        return False