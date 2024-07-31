from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    # Check for decorative elements
    decorative_elements = soup.find_all(class_='decoration')
    for decoration in decorative_elements:
        if decoration.get('alt') is not None:
            print(f"Decorative element with alt text found: {decoration}")
            return False

    print("All decorative elements are marked properly")
    return True
