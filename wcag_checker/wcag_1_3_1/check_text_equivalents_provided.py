from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    # Sample check: Verify if images have alt text
    images = soup.find_all('img')
    for img in images:
        if not img.get('alt') or not img['alt'].strip():
            print(f"Image without alt text found: {img}")
            return False

    print("All images have alt text")
    return True
