from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    links = soup.find_all('a')
    
    for link in links:
        print(f"Manual check required: Verify if the purpose of the link '{link.text.strip()}' is ambiguous to users in general.")
    
    return None  # This check requires manual verification