from .check_link_text import check as check_link_text
from .check_link_context import check as check_link_context
from .check_link_ambiguity import check as check_link_ambiguity

class WCAG2_4_4Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_link_text': False,
            'check_link_context': False,
            'check_link_ambiguity': False
        }

    def run_checks(self):
        self.results['check_link_text'] = check_link_text(self.url)
        self.results['check_link_context'] = check_link_context(self.url)
        self.results['check_link_ambiguity'] = check_link_ambiguity(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_link_text'] or
            self.results['check_link_context']
        ) and self.results['check_link_ambiguity']
        return overall_pass, self.results