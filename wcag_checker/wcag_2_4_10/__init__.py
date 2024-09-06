from .check_sections_exist import check as check_sections_exist
from .check_headings_exist import check as check_headings_exist
from .check_heading_content import check as check_heading_content
from .check_heading_hierarchy import check as check_heading_hierarchy

class WCAG2_4_10Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_sections_exist': False,
            'check_headings_exist': False,
            'check_heading_content': False,
            'check_heading_hierarchy': False
        }

    def run_checks(self):
        self.results['check_sections_exist'] = check_sections_exist(self.url)
        self.results['check_headings_exist'] = check_headings_exist(self.url)
        self.results['check_heading_content'] = check_heading_content(self.url)
        self.results['check_heading_hierarchy'] = check_heading_hierarchy(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results