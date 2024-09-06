from wcag_checker.utils import fetch_url, parse_html
from html.parser import HTMLParser

class UniqueIdChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.all_ids_unique = True

    def handle_starttag(self, tag, attrs):
        for attr, value in attrs:
            if attr == 'id':
                if value in self.ids:
                    self.all_ids_unique = False
                else:
                    self.ids.add(value)

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False

    parser = UniqueIdChecker()
    parser.feed(html_content)
    return parser.all_ids_unique