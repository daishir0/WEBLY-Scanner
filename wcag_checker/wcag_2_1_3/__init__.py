from .check_keyboard_operable import check as check_keyboard_operable

class WCAG2_1_3Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_keyboard_operable': False
        }

    def run_checks(self):
        self.results['check_keyboard_operable'] = check_keyboard_operable(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results