from .check_help_available import check as check_help_available
from .check_help_visibility import check as check_help_visibility
from .check_help_accessibility import check as check_help_accessibility
from .check_help_context_sensitivity import check as check_help_context_sensitivity

class WCAG3_3_5Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_help_available': False,
            'check_help_visibility': False,
            'check_help_accessibility': False,
            'check_help_context_sensitivity': False
        }

    def run_checks(self):
        self.results['check_help_available'] = check_help_available(self.url)
        self.results['check_help_visibility'] = check_help_visibility(self.url)
        self.results['check_help_accessibility'] = check_help_accessibility(self.url)
        self.results['check_help_context_sensitivity'] = check_help_context_sensitivity(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results