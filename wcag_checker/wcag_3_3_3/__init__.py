from .check_error_detection import check as check_error_detection
from .check_correction_suggestion import check as check_correction_suggestion
from .check_security_purpose import check as check_security_purpose

class WCAG3_3_3Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_error_detection': False,
            'check_correction_suggestion': False,
            'check_security_purpose': False
        }

    def run_checks(self):
        self.results['check_error_detection'] = check_error_detection(self.url)
        self.results['check_correction_suggestion'] = check_correction_suggestion(self.url)
        self.results['check_security_purpose'] = check_security_purpose(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results