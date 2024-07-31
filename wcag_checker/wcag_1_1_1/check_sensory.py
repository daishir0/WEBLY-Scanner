from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    # Check for sensory content elements (e.g., art)
    sensory_elements = soup.find_all(class_='sensory')
    for sensory in sensory_elements:
        if not sensory.get('aria-label') and not sensory.get('aria-labelledby') and not sensory.get('alt'):
            print(f"Sensory content without descriptive text found: {sensory}")
            return False

    print("All sensory content elements have descriptive text")
    return True
