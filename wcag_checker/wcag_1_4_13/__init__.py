from .check_dismissible import check as check_dismissible
from .check_hoverable import check as check_hoverable
from .check_persistent import check as check_persistent

class WCAG1_4_13Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_dismissible': False,
            'check_hoverable': False,
            'check_persistent': False
        }

    def run_checks(self):
        self.results['check_dismissible'] = check_dismissible(self.url)
        self.results['check_hoverable'] = check_hoverable(self.url)
        self.results['check_persistent'] = check_persistent(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results