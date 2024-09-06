from wcag_checker.utils import fetch_url, parse_html
from html.parser import HTMLParser

class DuplicateAttributeChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.no_duplicates = True

    def handle_starttag(self, tag, attrs):
        attr_set = set()
        for attr, value in attrs:
            if attr in attr_set:
                self.no_duplicates = False
                break
            attr_set.add(attr)

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False

    parser = DuplicateAttributeChecker()
    parser.feed(html_content)
    return parser.no_duplicates