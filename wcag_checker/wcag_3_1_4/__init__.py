from .check_abbreviation_first_occurrence import check as check_abbreviation_first_occurrence
from .check_abbreviation_all_occurrences import check as check_abbreviation_all_occurrences
from .check_abbreviation_different_meanings import check as check_abbreviation_different_meanings

class WCAG3_1_4Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_abbreviation_first_occurrence': False,
            'check_abbreviation_all_occurrences': False,
            'check_abbreviation_different_meanings': False
        }

    def run_checks(self):
        self.results['check_abbreviation_first_occurrence'] = check_abbreviation_first_occurrence(self.url)
        self.results['check_abbreviation_all_occurrences'] = check_abbreviation_all_occurrences(self.url)
        self.results['check_abbreviation_different_meanings'] = check_abbreviation_different_meanings(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_abbreviation_first_occurrence'] and
            self.results['check_abbreviation_all_occurrences'] and
            self.results['check_abbreviation_different_meanings']
        )
        return overall_pass, self.results