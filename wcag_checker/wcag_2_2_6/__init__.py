from .check_timeout_exists import check as check_timeout_exists
from .check_inactivity_duration_notification import check as check_inactivity_duration_notification
from .check_data_preservation import check as check_data_preservation

class WCAG2_2_6Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_timeout_exists': False,
            'check_inactivity_duration_notification': False,
            'check_data_preservation': False
        }

    def run_checks(self):
        self.results['check_timeout_exists'] = check_timeout_exists(self.url)
        self.results['check_inactivity_duration_notification'] = check_inactivity_duration_notification(self.url)
        self.results['check_data_preservation'] = check_data_preservation(self.url)

    def evaluate(self):
        timeout_warning = (
            self.results['check_timeout_exists'] and
            self.results['check_inactivity_duration_notification']
        )
        data_preservation = self.results['check_data_preservation']
        
        overall_pass = timeout_warning or data_preservation
        return overall_pass, self.results