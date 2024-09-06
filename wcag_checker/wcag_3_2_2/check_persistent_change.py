from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # フォーム要素を探す
    form_elements = soup.find_all(['input', 'select', 'textarea'])
    
    for element in form_elements:
        if element.get('onchange'):
            print(f"Warning: onchange event found on {element.name}. Manual check required.")
            return False
    
    print("No immediate persistent changes detected. Manual verification may be required.")
    return True