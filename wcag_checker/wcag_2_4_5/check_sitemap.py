from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # サイトマップへのリンクを探す
    sitemap_links = soup.find_all('a', href=True, text=lambda text: 'sitemap' in text.lower() if text else False)
    if sitemap_links:
        return True
    
    # robots.txtでサイトマップを探す
    robots_url = f"{url.rstrip('/')}/robots.txt"
    robots_content = fetch_url(robots_url)
    if robots_content and 'Sitemap:' in robots_content:
        return True
    
    return False