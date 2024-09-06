from .check_label_text import check as check_label_text
from .check_label_image_text import check as check_label_image_text
from .check_name_contains_label import check as check_name_contains_label
from .check_name_starts_with_label import check as check_name_starts_with_label

class WCAG2_5_3Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_label_text': False,
            'check_label_image_text': False,
            'check_name_contains_label': False,
            'check_name_starts_with_label': False
        }

    def run_checks(self):
        self.results['check_label_text'] = check_label_text(self.url)
        self.results['check_label_image_text'] = check_label_image_text(self.url)
        self.results['check_name_contains_label'] = check_name_contains_label(self.url)
        self.results['check_name_starts_with_label'] = check_name_starts_with_label(self.url)

    def evaluate(self):
        overall_pass = (
            (self.results['check_label_text'] or self.results['check_label_image_text']) and
            self.results['check_name_contains_label']
        )
        return overall_pass, self.results