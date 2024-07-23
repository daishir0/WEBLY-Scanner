from .check_lang_attribute_exists import check as check_lang_attribute_exists
from .check_lang_not_empty import check as check_lang_not_empty
from .check_lang_valid import check as check_lang_valid

class WCAG3_1_1Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_lang_attribute_exists': False,
            'check_lang_not_empty': False,
            'check_lang_valid': False
        }

    def run_checks(self):
        self.results['check_lang_attribute_exists'] = check_lang_attribute_exists(self.url)
        self.results['check_lang_not_empty'] = check_lang_not_empty(self.url)
        self.results['check_lang_valid'] = check_lang_valid(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_lang_attribute_exists'] and
            self.results['check_lang_not_empty'] and
            self.results['check_lang_valid']
        )
        return overall_pass, self.results