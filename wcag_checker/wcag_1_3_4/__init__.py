from .check_orientation_support import check as check_orientation_support
from .check_essential_orientation import check as check_essential_orientation

class WCAG1_3_4Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_orientation_support': False,
            'check_essential_orientation': True  # デフォルトでTrueとし、必要な場合のみFalseに設定
        }

    def run_checks(self):
        self.results['check_orientation_support'] = check_orientation_support(self.url)
        essential_orientation, reason = check_essential_orientation(self.url)
        self.results['check_essential_orientation'] = essential_orientation
        if not essential_orientation:
            print(f"Manual check required: {reason}")

    def evaluate(self):
        overall_pass = self.results['check_orientation_support'] or self.results['check_essential_orientation']
        return overall_pass, self.results