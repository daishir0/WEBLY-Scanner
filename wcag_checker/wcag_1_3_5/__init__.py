from .check_input_purpose import check as check_input_purpose
from .check_technology_support import check as check_technology_support

class WCAG1_3_5Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_input_purpose': False,
            'check_technology_support': False
        }

    def run_checks(self):
        self.results['check_input_purpose'] = check_input_purpose(self.url)
        self.results['check_technology_support'] = check_technology_support(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results