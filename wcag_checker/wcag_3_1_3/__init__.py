from .check_idiom_definitions import check as check_idiom_definitions
from .check_jargon_definitions import check as check_jargon_definitions
from .check_unusual_word_definitions import check as check_unusual_word_definitions

class WCAG3_1_3Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_idiom_definitions': False,
            'check_jargon_definitions': False,
            'check_unusual_word_definitions': False
        }

    def run_checks(self):
        self.results['check_idiom_definitions'] = check_idiom_definitions(self.url)
        self.results['check_jargon_definitions'] = check_jargon_definitions(self.url)
        self.results['check_unusual_word_definitions'] = check_unusual_word_definitions(self.url)

    def evaluate(self):
        overall_pass = any([
            self.results['check_idiom_definitions'],
            self.results['check_jargon_definitions'],
            self.results['check_unusual_word_definitions']
        ])
        return overall_pass, self.results