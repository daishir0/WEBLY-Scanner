from .check_title_exists import check as check_title_exists
from .check_title_not_empty import check as check_title_not_empty
from .check_title_not_generic import check as check_title_not_generic
from .check_title_describes_content import check as check_title_describes_content

class WCAG2_4_2Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_title_exists': False,
            'check_title_not_empty': False,
            'check_title_not_generic': False,
            'check_title_describes_content': False
        }

    def run_checks(self):
        self.results['check_title_exists'] = check_title_exists(self.url)
        self.results['check_title_not_empty'] = check_title_not_empty(self.url)
        self.results['check_title_not_generic'] = check_title_not_generic(self.url)
        self.results['check_title_describes_content'] = check_title_describes_content(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_title_exists'] and
            self.results['check_title_not_empty'] and
            self.results['check_title_not_generic'] and
            self.results['check_title_describes_content']
        )
        return overall_pass, self.results
