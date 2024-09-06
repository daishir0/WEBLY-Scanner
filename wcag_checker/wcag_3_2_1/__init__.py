from .check_no_auto_submit import check as check_no_auto_submit
from .check_no_new_window import check as check_no_new_window
from .check_no_focus_change import check as check_no_focus_change

class WCAG3_2_1Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_no_auto_submit': False,
            'check_no_new_window': False,
            'check_no_focus_change': False
        }

    def run_checks(self):
        self.results['check_no_auto_submit'] = check_no_auto_submit(self.url)
        self.results['check_no_new_window'] = check_no_new_window(self.url)
        self.results['check_no_focus_change'] = check_no_focus_change(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results