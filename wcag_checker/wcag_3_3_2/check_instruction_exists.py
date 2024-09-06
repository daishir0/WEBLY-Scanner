from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # フォーム要素の近くにテキストが存在するかチェック
    forms = soup.find_all('form')
    for form in forms:
        if form.find_previous_sibling(text=True) or form.find_next_sibling(text=True):
            return True
    
    # aria-describedby属性の存在をチェック
    elements_with_aria_describedby = soup.find_all(attrs={"aria-describedby": True})
    if elements_with_aria_describedby:
        return True
    
    return False