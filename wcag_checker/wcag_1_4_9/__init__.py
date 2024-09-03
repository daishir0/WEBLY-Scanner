from .check_text_images import check as check_text_images
from .check_essential_presentation import check as check_essential_presentation
from .check_logotype import check as check_logotype

class WCAG1_4_9Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_text_images': False,
            'check_essential_presentation': False,
            'check_logotype': False
        }

    def run_checks(self):
        self.results['check_text_images'] = check_text_images(self.url)
        self.results['check_essential_presentation'] = check_essential_presentation(self.url)
        self.results['check_logotype'] = check_logotype(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_text_images'] or
            self.results['check_essential_presentation'] or
            self.results['check_logotype']
        )
        return overall_pass, self.results