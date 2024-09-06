from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # キーボードショートカットをオフにするメカニズムを探す
    # 例: 特定のクラスや属性を持つ要素を探す
    off_mechanism = soup.find(class_='shortcut-off') or soup.find(attrs={'data-shortcut-off': True})
    
    if off_mechanism:
        return True
    else:
        print("Manual check required: Verify if there's a mechanism to turn off character key shortcuts.")
        return False