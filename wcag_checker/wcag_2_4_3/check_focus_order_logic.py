from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    focusable_elements = soup.find_all(['a', 'button', 'input', 'select', 'textarea'])
    
    # フォーカス順序の論理性を簡易的にチェック
    # ここでは、要素のDOM順序が論理的であると仮定
    return all(focusable_elements[i].sourcepos <= focusable_elements[i+1].sourcepos for i in range(len(focusable_elements)-1))