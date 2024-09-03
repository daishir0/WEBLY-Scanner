from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    input_fields = soup.find_all('input')
    
    valid_purposes = [
        'name', 'email', 'tel', 'address', 'bday', 'username', 'new-password',
        'current-password', 'organization', 'street-address', 'postal-code',
        'country', 'cc-name', 'cc-number', 'cc-exp', 'cc-csc'
    ]
    
    for input_field in input_fields:
        autocomplete = input_field.get('autocomplete')
        if autocomplete and autocomplete in valid_purposes:
            return True
    
    return False