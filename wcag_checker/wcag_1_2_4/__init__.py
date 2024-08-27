from .check_captions_exist import check as check_captions_exist
from .check_captions_synchronized import check as check_captions_synchronized
from .check_captions_complete import check as check_captions_complete

class WCAG1_2_4Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_captions_exist': False,
            'check_captions_synchronized': False,
            'check_captions_complete': False
        }

    def run_checks(self):
        self.results['check_captions_exist'] = check_captions_exist(self.url)
        self.results['check_captions_synchronized'] = check_captions_synchronized(self.url)
        self.results['check_captions_complete'] = check_captions_complete(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results