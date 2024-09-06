from .check_status_message_exists import check as check_status_message_exists
from .check_programmatically_determinable import check as check_programmatically_determinable

class WCAG4_1_3Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_status_message_exists': False,
            'check_programmatically_determinable': False
        }

    def run_checks(self):
        self.results['check_status_message_exists'] = check_status_message_exists(self.url)
        self.results['check_programmatically_determinable'] = check_programmatically_determinable(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results