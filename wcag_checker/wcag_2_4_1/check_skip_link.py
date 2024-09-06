from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # ページ上部のリンクを検索
    top_links = soup.find_all('a', href=True, limit=5)
    
    for link in top_links:
        href = link['href']
        link_text = link.get_text().lower()
        
        # スキップリンクの一般的なパターンを確認
        if (href.startswith('#main') or 
            href.startswith('#content') or 
            'skip' in link_text or 
            'jump' in link_text):
            return True
    
    return False