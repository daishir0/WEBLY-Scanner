from .check_captions_exist import check as check_captions_exist
from .check_synchronized_media import check as check_synchronized_media
from .check_not_text_alternative import check as check_not_text_alternative

class WCAG1_2_2Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_captions_exist': False,
            'check_synchronized_media': False,
            'check_not_text_alternative': False
        }

    def run_checks(self):
        self.results['check_captions_exist'] = check_captions_exist(self.url)
        self.results['check_synchronized_media'] = check_synchronized_media(self.url)
        self.results['check_not_text_alternative'] = check_not_text_alternative(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results