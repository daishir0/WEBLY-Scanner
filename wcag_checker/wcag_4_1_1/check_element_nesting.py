from wcag_checker.utils import fetch_url, parse_html
from html.parser import HTMLParser

class NestingChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag_stack = []
        self.nesting_correct = True

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)

    def handle_endtag(self, tag):
        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()
        else:
            self.nesting_correct = False

    def check(self):
        return len(self.tag_stack) == 0 and self.nesting_correct

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False

    parser = NestingChecker()
    parser.feed(html_content)
    return parser.check()