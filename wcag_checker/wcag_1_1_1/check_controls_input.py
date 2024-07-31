from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    # Control and input elements should have descriptive names
    controls = soup.find_all(['input', 'button', 'select', 'textarea'])
    for control in controls:
        if not control.get('aria-label') and not control.get('aria-labelledby') and not control.get('alt'):
            print(f"Control without descriptive name found: {control}")
            return False
    
    print("All controls and input elements have descriptive names")
    return True
