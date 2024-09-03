from .check_normal_text_contrast import check as check_normal_text_contrast
from .check_large_text_contrast import check as check_large_text_contrast
from .check_exceptions import check as check_exceptions

class WCAG1_4_6Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_normal_text_contrast': False,
            'check_large_text_contrast': False,
            'check_exceptions': False
        }

    def run_checks(self):
        self.results['check_normal_text_contrast'] = check_normal_text_contrast(self.url)
        self.results['check_large_text_contrast'] = check_large_text_contrast(self.url)
        self.results['check_exceptions'] = check_exceptions(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_normal_text_contrast'] and
            self.results['check_large_text_contrast'] and
            self.results['check_exceptions']
        )
        return overall_pass, self.results