from .check_link_text_exists import check as check_link_text_exists
from .check_link_text_not_empty import check as check_link_text_not_empty
from .check_link_text_describes_purpose import check as check_link_text_describes_purpose
from .check_link_purpose_ambiguous import check as check_link_purpose_ambiguous

class WCAG2_4_9Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_link_text_exists': False,
            'check_link_text_not_empty': False,
            'check_link_text_describes_purpose': False,
            'check_link_purpose_ambiguous': False
        }

    def run_checks(self):
        self.results['check_link_text_exists'] = check_link_text_exists(self.url)
        self.results['check_link_text_not_empty'] = check_link_text_not_empty(self.url)
        self.results['check_link_text_describes_purpose'] = check_link_text_describes_purpose(self.url)
        self.results['check_link_purpose_ambiguous'] = check_link_purpose_ambiguous(self.url)

    def evaluate(self):
        if self.results['check_link_purpose_ambiguous']:
            overall_pass = True
        else:
            overall_pass = (
                self.results['check_link_text_exists'] and
                self.results['check_link_text_not_empty'] and
                self.results['check_link_text_describes_purpose']
            )
        return overall_pass, self.results