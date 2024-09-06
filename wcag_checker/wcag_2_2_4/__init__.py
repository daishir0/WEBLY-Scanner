from .check_interruption_postpone import check as check_interruption_postpone
from .check_interruption_suppress import check as check_interruption_suppress
from .check_emergency_exception import check as check_emergency_exception

class WCAG2_2_4Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_interruption_postpone': False,
            'check_interruption_suppress': False,
            'check_emergency_exception': False
        }

    def run_checks(self):
        self.results['check_interruption_postpone'] = check_interruption_postpone(self.url)
        self.results['check_interruption_suppress'] = check_interruption_suppress(self.url)
        self.results['check_emergency_exception'] = check_emergency_exception(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results