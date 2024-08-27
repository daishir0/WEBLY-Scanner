from .check_alternative_content import check as check_alternative_content
from .check_equivalent_information import check as check_equivalent_information
from .check_timely_provision import check as check_timely_provision

class WCAG1_2_9Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_alternative_content': False,
            'check_equivalent_information': False,
            'check_timely_provision': False
        }

    def run_checks(self):
        self.results['check_alternative_content'] = check_alternative_content(self.url)
        self.results['check_equivalent_information'] = check_equivalent_information(self.url)
        self.results['check_timely_provision'] = check_timely_provision(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results