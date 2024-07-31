from .check_controls_input import check as check_controls_input
from .check_time_based_media import check as check_time_based_media
from .check_test import check as check_test
from .check_sensory import check as check_sensory
from .check_captcha import check as check_captcha
from .check_decoration import check as check_decoration

class WCAG1_1_1Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_controls_input': False,
            'check_time_based_media': False,
            'check_test': False,
            'check_sensory': False,
            'check_captcha': False,
            'check_decoration': False
        }

    def run_checks(self):
        self.results['check_controls_input'] = check_controls_input(self.url)
        self.results['check_time_based_media'] = check_time_based_media(self.url)
        self.results['check_test'] = check_test(self.url)
        self.results['check_sensory'] = check_sensory(self.url)
        self.results['check_captcha'] = check_captcha(self.url)
        self.results['check_decoration'] = check_decoration(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results
