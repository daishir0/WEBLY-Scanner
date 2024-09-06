from .check_keyboard_operable import check as check_keyboard_operable
from .check_focus_visible import check as check_focus_visible
from .check_focus_indicator_prominent import check as check_focus_indicator_prominent

class WCAG2_4_7Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_keyboard_operable': False,
            'check_focus_visible': False,
            'check_focus_indicator_prominent': False
        }

    def run_checks(self):
        self.results['check_keyboard_operable'] = check_keyboard_operable(self.url)
        self.results['check_focus_visible'] = check_focus_visible(self.url)
        self.results['check_focus_indicator_prominent'] = check_focus_indicator_prominent(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results