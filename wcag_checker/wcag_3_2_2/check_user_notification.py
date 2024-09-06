from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # フォーム要素を探す
    form_elements = soup.find_all(['input', 'select', 'textarea'])
    
    for element in form_elements:
        if element.get('aria-describedby'):
            description_id = element.get('aria-describedby')
            description_element = soup.find(id=description_id)
            if description_element and "変更" in description_element.text:
                print(f"User notification found for {element.name}")
                return True
    
    print("No explicit user notifications found. Manual check required.")
    return False