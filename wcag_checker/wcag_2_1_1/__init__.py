from .check_keyboard_operable import check as check_keyboard_operable
from .check_no_specific_timing import check as check_no_specific_timing
from .check_path_dependent_exception import check as check_path_dependent_exception

class WCAG2_1_1Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_keyboard_operable': False,
            'check_no_specific_timing': False,
            'check_path_dependent_exception': False
        }

    def run_checks(self):
        self.results['check_keyboard_operable'] = check_keyboard_operable(self.url)
        self.results['check_no_specific_timing'] = check_no_specific_timing(self.url)
        self.results['check_path_dependent_exception'] = check_path_dependent_exception(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results