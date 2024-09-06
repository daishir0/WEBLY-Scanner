from wcag_checker.utils import fetch_url, parse_html
from urllib.parse import urljoin

def check(url):
    # ホームページのURLを取得
    home_url = '/'.join(url.split('/')[:3])  # スキーム + ドメイン
    
    html_content = fetch_url(home_url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # ホームページ上のすべてのリンクを取得
    links = soup.find_all('a', href=True)
    
    # 内部リンクの数をカウント
    internal_links = set()
    for link in links:
        href = link['href']
        full_url = urljoin(home_url, href)
        if full_url.startswith(home_url):
            internal_links.add(full_url)
    
    # 内部リンクが10個以上あれば、十分な数のページにリンクしていると判断
    return len(internal_links) >= 10