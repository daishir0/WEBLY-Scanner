from .check_name import check as check_name
from .check_role import check as check_role
from .check_state_property_value import check as check_state_property_value
from .check_notification import check as check_notification

class WCAG4_1_2Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_name': False,
            'check_role': False,
            'check_state_property_value': False,
            'check_notification': False
        }

    def run_checks(self):
        self.results['check_name'] = check_name(self.url)
        self.results['check_role'] = check_role(self.url)
        self.results['check_state_property_value'] = check_state_property_value(self.url)
        self.results['check_notification'] = check_notification(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_name'] and
            self.results['check_role'] and
            self.results['check_state_property_value'] and
            self.results['check_notification']
        )
        return overall_pass, self.results