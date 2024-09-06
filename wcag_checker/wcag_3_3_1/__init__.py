from .check_input_error_detected import check as check_input_error_detected
from .check_error_described_in_text import check as check_error_described_in_text
from .check_error_message_specific import check as check_error_message_specific
from .check_combined_with_programmatic_info import check as check_combined_with_programmatic_info

class WCAG3_3_1Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_input_error_detected': False,
            'check_error_described_in_text': False,
            'check_error_message_specific': False,
            'check_combined_with_programmatic_info': False
        }

    def run_checks(self):
        self.results['check_input_error_detected'] = check_input_error_detected(self.url)
        self.results['check_error_described_in_text'] = check_error_described_in_text(self.url)
        self.results['check_error_message_specific'] = check_error_message_specific(self.url)
        self.results['check_combined_with_programmatic_info'] = check_combined_with_programmatic_info(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_input_error_detected'] and
            self.results['check_error_described_in_text'] and
            self.results['check_error_message_specific'] and
            self.results['check_combined_with_programmatic_info']
        )
        return overall_pass, self.results