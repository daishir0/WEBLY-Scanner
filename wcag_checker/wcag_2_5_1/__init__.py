from .check_multipoint_gestures import check as check_multipoint_gestures
from .check_path_based_gestures import check as check_path_based_gestures

class WCAG2_5_1Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_multipoint_gestures': False,
            'check_path_based_gestures': False
        }

    def run_checks(self):
        self.results['check_multipoint_gestures'] = check_multipoint_gestures(self.url)
        self.results['check_path_based_gestures'] = check_path_based_gestures(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results