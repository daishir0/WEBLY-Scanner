from .check_consistent_identification import check as check_consistent_identification

class WCAG3_2_4Checker:
    def __init__(self, url_set):
        self.url_set = url_set
        self.results = {
            'check_consistent_identification': False
        }

    def run_checks(self):
        self.results['check_consistent_identification'] = check_consistent_identification(self.url_set)

    def evaluate(self):
        overall_pass = self.results['check_consistent_identification']
        return overall_pass, self.results