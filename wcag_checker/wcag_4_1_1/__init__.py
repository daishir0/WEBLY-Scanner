from .check_start_end_tags import check as check_start_end_tags
from .check_element_nesting import check as check_element_nesting
from .check_duplicate_attributes import check as check_duplicate_attributes
from .check_unique_ids import check as check_unique_ids

class WCAG4_1_1Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_start_end_tags': False,
            'check_element_nesting': False,
            'check_duplicate_attributes': False,
            'check_unique_ids': False
        }

    def run_checks(self):
        self.results['check_start_end_tags'] = check_start_end_tags(self.url)
        self.results['check_element_nesting'] = check_element_nesting(self.url)
        self.results['check_duplicate_attributes'] = check_duplicate_attributes(self.url)
        self.results['check_unique_ids'] = check_unique_ids(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results