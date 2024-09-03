from .check_text_used import check as check_text_used
from .check_customizable_image_text import check as check_customizable_image_text
from .check_essential_image_text import check as check_essential_image_text

class WCAG1_4_5Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_text_used': False,
            'check_customizable_image_text': False,
            'check_essential_image_text': False
        }

    def run_checks(self):
        self.results['check_text_used'] = check_text_used(self.url)
        self.results['check_customizable_image_text'] = check_customizable_image_text(self.url)
        self.results['check_essential_image_text'] = check_essential_image_text(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_text_used'] or
            (self.results['check_customizable_image_text'] or self.results['check_essential_image_text'])
        )
        return overall_pass, self.results