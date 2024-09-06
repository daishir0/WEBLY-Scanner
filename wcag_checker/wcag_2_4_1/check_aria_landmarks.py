from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # ARIAランドマークを検索
    landmarks = soup.find_all(attrs={"role": ["banner", "navigation", "main", "complementary", "contentinfo"]})
    
    return len(landmarks) > 0