from .check_user_initiated_changes import check as check_user_initiated_changes
from .check_mechanism_to_disable_changes import check as check_mechanism_to_disable_changes

class WCAG3_2_5Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_user_initiated_changes': False,
            'check_mechanism_to_disable_changes': False
        }

    def run_checks(self):
        self.results['check_user_initiated_changes'] = check_user_initiated_changes(self.url)
        self.results['check_mechanism_to_disable_changes'] = check_mechanism_to_disable_changes(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_user_initiated_changes'] or
            self.results['check_mechanism_to_disable_changes']
        )
        return overall_pass, self.results