from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 中断を延期するメカニズムの存在を確認
    postpone_mechanisms = soup.find_all(['button', 'a', 'input'], text=lambda t: t and '延期' in t)
    
    if postpone_mechanisms:
        print("中断を延期するメカニズムが見つかりました。")
        return True
    else:
        print("中断を延期するメカニズムが見つかりませんでした。手動での確認が必要です。")
        return None  # 手動確認が必要