from .check_ui_component_change import check as check_ui_component_change
from .check_persistent_change import check as check_persistent_change
from .check_no_context_change import check as check_no_context_change
from .check_user_notification import check as check_user_notification

class WCAG3_2_2Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_ui_component_change': False,
            'check_persistent_change': False,
            'check_no_context_change': False,
            'check_user_notification': False
        }

    def run_checks(self):
        self.results['check_ui_component_change'] = check_ui_component_change(self.url)
        self.results['check_persistent_change'] = check_persistent_change(self.url)
        self.results['check_no_context_change'] = check_no_context_change(self.url)
        self.results['check_user_notification'] = check_user_notification(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_ui_component_change'] and
            self.results['check_persistent_change'] and
            (self.results['check_no_context_change'] or self.results['check_user_notification'])
        )
        return overall_pass, self.results