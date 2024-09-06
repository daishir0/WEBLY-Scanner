from .check_navigation_exists import check as check_navigation_exists
from .check_navigation_order import check as check_navigation_order
from .check_user_initiated_change import check as check_user_initiated_change

class WCAG3_2_3Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_navigation_exists': False,
            'check_navigation_order': False,
            'check_user_initiated_change': True  # デフォルトでTrueとし、ユーザーによる変更がない場合を想定
        }

    def run_checks(self):
        self.results['check_navigation_exists'] = check_navigation_exists(self.url)
        self.results['check_navigation_order'] = check_navigation_order(self.url)
        self.results['check_user_initiated_change'] = check_user_initiated_change(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_navigation_exists'] and
            self.results['check_navigation_order'] and
            self.results['check_user_initiated_change']
        )
        return overall_pass, self.results