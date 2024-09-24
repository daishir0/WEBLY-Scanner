from .check_keyboard_focus import check as check_keyboard_focus

class WCAG2_1_2Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_keyboard_focus': False
        }

    def run_checks(self):
        self.results['check_keyboard_focus'] = check_keyboard_focus(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results