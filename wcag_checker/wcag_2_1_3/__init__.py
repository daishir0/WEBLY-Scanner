from .check_keyboard_operable import check as check_keyboard_operable
from .check_no_timing_requirement import check as check_no_timing_requirement

class WCAG2_1_3Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_keyboard_operable': False,
            'check_no_timing_requirement': False
        }

    def run_checks(self):
        self.results['check_keyboard_operable'] = check_keyboard_operable(self.url)
        self.results['check_no_timing_requirement'] = check_no_timing_requirement(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results