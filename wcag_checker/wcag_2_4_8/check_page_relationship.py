from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # link要素の確認
    link_elements = soup.find_all('link', rel=['prev', 'next', 'up', 'home'])
    
    if link_elements:
        print("ページ間の関係を示すlink要素が見つかりました。")
        return True
    else:
        print("ページ間の関係を示すlink要素が見つかりませんでした。他のナビゲーションツールを手動で確認してください。")
        return False