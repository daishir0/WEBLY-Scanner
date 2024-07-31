from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    # Check for test elements (e.g., quizzes)
    test_elements = soup.find_all(class_='test')
    for test in test_elements:
        if not test.get('aria-label') and not test.get('aria-labelledby') and not test.get('alt'):
            print(f"Test element without descriptive text found: {test}")
            return False

    print("All test elements have descriptive text")
    return True
