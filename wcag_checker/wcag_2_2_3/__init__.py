from .check_no_timing import check as check_no_timing
from .check_exceptions import check as check_exceptions

class WCAG2_2_3Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_no_timing': False,
            'check_exceptions': False
        }

    def run_checks(self):
        self.results['check_no_timing'] = check_no_timing(self.url)
        self.results['check_exceptions'] = check_exceptions(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_no_timing'] and
            self.results['check_exceptions']
        )
        return overall_pass, self.results