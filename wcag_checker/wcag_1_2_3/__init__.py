from .check_audio_description import check as check_audio_description
from .check_media_alternative import check as check_media_alternative
from .check_exception_condition import check as check_exception_condition

class WCAG1_2_3Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_audio_description': False,
            'check_media_alternative': False,
            'check_exception_condition': False
        }

    def run_checks(self):
        self.results['check_audio_description'] = check_audio_description(self.url)
        self.results['check_media_alternative'] = check_media_alternative(self.url)
        self.results['check_exception_condition'] = check_exception_condition(self.url)

    def evaluate(self):
        overall_pass = (
            (self.results['check_audio_description'] or self.results['check_media_alternative']) or
            self.results['check_exception_condition']
        )
        return overall_pass, self.results