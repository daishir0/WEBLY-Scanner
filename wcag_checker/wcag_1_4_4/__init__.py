from .check_text_resizable import check as check_text_resizable
from .check_content_preserved import check as check_content_preserved
from .check_functionality_preserved import check as check_functionality_preserved
from .check_exceptions import check as check_exceptions

class WCAG1_4_4Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_text_resizable': False,
            'check_content_preserved': False,
            'check_functionality_preserved': False,
            'check_exceptions': False
        }

    def run_checks(self):
        self.results['check_text_resizable'] = check_text_resizable(self.url)
        self.results['check_content_preserved'] = check_content_preserved(self.url)
        self.results['check_functionality_preserved'] = check_functionality_preserved(self.url)
        self.results['check_exceptions'] = check_exceptions(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results