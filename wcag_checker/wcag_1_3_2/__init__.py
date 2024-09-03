from .check_meaningful_sequence import check as check_meaningful_sequence
from .check_programmatically_determinable import check as check_programmatically_determinable

class WCAG1_3_2Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_meaningful_sequence': False,
            'check_programmatically_determinable': False
        }

    def run_checks(self):
        self.results['check_meaningful_sequence'] = check_meaningful_sequence(self.url)
        self.results['check_programmatically_determinable'] = check_programmatically_determinable(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results