from .check_line_height import check as check_line_height
from .check_paragraph_spacing import check as check_paragraph_spacing
from .check_letter_spacing import check as check_letter_spacing
from .check_word_spacing import check as check_word_spacing

class WCAG1_4_12Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_line_height': False,
            'check_paragraph_spacing': False,
            'check_letter_spacing': False,
            'check_word_spacing': False
        }

    def run_checks(self):
        self.results['check_line_height'] = check_line_height(self.url)
        self.results['check_paragraph_spacing'] = check_paragraph_spacing(self.url)
        self.results['check_letter_spacing'] = check_letter_spacing(self.url)
        self.results['check_word_spacing'] = check_word_spacing(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_line_height'] and
            self.results['check_paragraph_spacing'] and
            self.results['check_letter_spacing'] and
            self.results['check_word_spacing']
        )
        return overall_pass, self.results