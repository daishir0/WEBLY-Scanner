from .check_reversible import check as check_reversible
from .check_error_detection import check as check_error_detection
from .check_confirmation import check as check_confirmation

class WCAG3_3_6Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_reversible': False,
            'check_error_detection': False,
            'check_confirmation': False
        }

    def run_checks(self):
        self.results['check_reversible'] = check_reversible(self.url)
        self.results['check_error_detection'] = check_error_detection(self.url)
        self.results['check_confirmation'] = check_confirmation(self.url)

    def evaluate(self):
        overall_pass = any([
            self.results['check_reversible'],
            self.results['check_error_detection'],
            self.results['check_confirmation']
        ])
        return overall_pass, self.results