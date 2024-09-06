from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 'All Pages'や'サイト内のすべてのページ'などのリンクを探す
    all_pages_link = soup.find('a', text=lambda text: 'all pages' in text.lower() if text else False)
    if all_pages_link:
        return True
    
    # フッターに多数のリンクがある場合、それを全ページリストとみなす
    footer = soup.find('footer')
    if footer and len(footer.find_all('a')) > 10:
        return True
    
    return False