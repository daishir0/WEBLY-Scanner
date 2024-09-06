from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # ラベル要素の存在をチェック
    labels = soup.find_all('label')
    if labels:
        return True
    
    # aria-label属性の存在をチェック
    elements_with_aria_label = soup.find_all(attrs={"aria-label": True})
    if elements_with_aria_label:
        return True
    
    return False