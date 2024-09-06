from .check_pronunciation_mechanism import check as check_pronunciation_mechanism
from .check_ambiguous_words import check as check_ambiguous_words
from .check_pronunciation_needed import check as check_pronunciation_needed

class WCAG3_1_6Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_pronunciation_mechanism': False,
            'check_ambiguous_words': False,
            'check_pronunciation_needed': False
        }

    def run_checks(self):
        self.results['check_pronunciation_mechanism'] = check_pronunciation_mechanism(self.url)
        self.results['check_ambiguous_words'] = check_ambiguous_words(self.url)
        self.results['check_pronunciation_needed'] = check_pronunciation_needed(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results