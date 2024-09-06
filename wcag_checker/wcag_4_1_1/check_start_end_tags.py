from wcag_checker.utils import fetch_url, parse_html
from html.parser import HTMLParser

class TagChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.open_tags = []
        self.all_tags_closed = True

    def handle_starttag(self, tag, attrs):
        self.open_tags.append(tag)

    def handle_endtag(self, tag):
        if self.open_tags and self.open_tags[-1] == tag:
            self.open_tags.pop()
        else:
            self.all_tags_closed = False

    def check(self):
        return len(self.open_tags) == 0 and self.all_tags_closed

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False

    parser = TagChecker()
    parser.feed(html_content)
    return parser.check()