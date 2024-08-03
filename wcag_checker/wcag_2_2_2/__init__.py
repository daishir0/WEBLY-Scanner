from .check_moving_blinking_scrolling import check as check_moving_blinking_scrolling
from .check_auto_updating import check as check_auto_updating

class WCAG2_2_2Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_moving_blinking_scrolling': False,
            'check_auto_updating': False
        }

    def run_checks(self):
        self.results['check_moving_blinking_scrolling'] = check_moving_blinking_scrolling(self.url)
        self.results['check_auto_updating'] = check_auto_updating(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results