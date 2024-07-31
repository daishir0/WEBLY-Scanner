from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    # Check for time-based media elements
    media_elements = soup.find_all(['audio', 'video'])
    for media in media_elements:
        if not media.get('aria-label') and not media.get('aria-labelledby') and not media.get('alt'):
            print(f"Time-based media without descriptive text found: {media}")
            return False

    print("All time-based media elements have descriptive text")
    return True
