from .check_reading_level import check as check_reading_level
from .check_supplemental_content import check as check_supplemental_content

class WCAG3_1_5Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_reading_level': False,
            'check_supplemental_content': False
        }

    def run_checks(self):
        self.results['check_reading_level'] = check_reading_level(self.url)
        self.results['check_supplemental_content'] = check_supplemental_content(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_reading_level'] or
            self.results['check_supplemental_content']
        )
        return overall_pass, self.results