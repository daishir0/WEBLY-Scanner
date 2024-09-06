from .check_keyboard_focus import check as check_keyboard_focus
from .check_focus_removal import check as check_focus_removal
from .check_exit_method_explanation import check as check_exit_method_explanation

class WCAG2_1_2Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_keyboard_focus': False,
            'check_focus_removal': False,
            'check_exit_method_explanation': False
        }

    def run_checks(self):
        self.results['check_keyboard_focus'] = check_keyboard_focus(self.url)
        self.results['check_focus_removal'] = check_focus_removal(self.url)
        self.results['check_exit_method_explanation'] = check_exit_method_explanation(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results