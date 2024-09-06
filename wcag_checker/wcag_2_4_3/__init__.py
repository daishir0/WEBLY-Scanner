from .check_sequential_navigation import check as check_sequential_navigation
from .check_focus_order_logic import check as check_focus_order_logic
from .check_focus_order_meaning import check as check_focus_order_meaning
from .check_focus_order_operability import check as check_focus_order_operability

class WCAG2_4_3Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_sequential_navigation': False,
            'check_focus_order_logic': False,
            'check_focus_order_meaning': False,
            'check_focus_order_operability': False
        }

    def run_checks(self):
        self.results['check_sequential_navigation'] = check_sequential_navigation(self.url)
        self.results['check_focus_order_logic'] = check_focus_order_logic(self.url)
        self.results['check_focus_order_meaning'] = check_focus_order_meaning(self.url)
        self.results['check_focus_order_operability'] = check_focus_order_operability(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results