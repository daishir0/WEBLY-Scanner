from .check_info_relationships_programmatically_determinable import check as check_info_relationships_programmatically_determinable
from .check_text_equivalents_provided import check as check_text_equivalents_provided

class WCAG1_3_1Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_info_relationships_programmatically_determinable': False,
            'check_text_equivalents_provided': False
        }

    def run_checks(self):
        self.results['check_info_relationships_programmatically_determinable'] = check_info_relationships_programmatically_determinable(self.url)
        self.results['check_text_equivalents_provided'] = check_text_equivalents_provided(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_info_relationships_programmatically_determinable'] and
            self.results['check_text_equivalents_provided']
        )
        return overall_pass, self.results
