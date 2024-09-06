from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    abbreviations = soup.find_all('abbr')
    for abbr in abbreviations:
        if abbr.has_attr('title'):
            return True
    return False