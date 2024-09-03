from .check_vertical_scroll import check as check_vertical_scroll
from .check_horizontal_scroll import check as check_horizontal_scroll
from .check_exceptions import check as check_exceptions

class WCAG1_4_10Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_vertical_scroll': False,
            'check_horizontal_scroll': False,
            'check_exceptions': False
        }

    def run_checks(self):
        self.results['check_vertical_scroll'] = check_vertical_scroll(self.url)
        self.results['check_horizontal_scroll'] = check_horizontal_scroll(self.url)
        self.results['check_exceptions'] = check_exceptions(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_vertical_scroll'] and
            self.results['check_horizontal_scroll'] and
            self.results['check_exceptions']
        )
        return overall_pass, self.results