from .check_lang_attribute_exists_for_passages import check as check_lang_attribute_exists_for_passages
from .check_pdf_lang_entry_for_passages import check as check_pdf_lang_entry_for_passages

class WCAG3_1_2Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_lang_attribute_exists_for_passages': False,
            'check_pdf_lang_entry_for_passages': False
        }

    def run_checks(self):
        self.results['check_lang_attribute_exists_for_passages'] = check_lang_attribute_exists_for_passages(self.url)
        self.results['check_pdf_lang_entry_for_passages'] = check_pdf_lang_entry_for_passages(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_lang_attribute_exists_for_passages'] or
            self.results['check_pdf_lang_entry_for_passages']
        )
        return overall_pass, self.results