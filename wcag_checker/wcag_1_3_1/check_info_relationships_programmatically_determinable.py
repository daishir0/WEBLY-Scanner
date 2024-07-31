from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    # Sample check: Verify if headings (h1, h2, etc.) are correctly used
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    if not headings:
        print("No headings found")
        return False

    for heading in headings:
        if not heading.get_text().strip():
            print(f"Empty heading found: {heading}")
            return False

    print("All headings are properly structured and non-empty")
    return True
