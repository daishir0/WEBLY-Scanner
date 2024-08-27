from .check_audio_description_exists import check as check_audio_description_exists
from .check_audio_description_synchronized import check as check_audio_description_synchronized

class WCAG1_2_5Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_audio_description_exists': False,
            'check_audio_description_synchronized': False
        }

    def run_checks(self):
        self.results['check_audio_description_exists'] = check_audio_description_exists(self.url)
        self.results['check_audio_description_synchronized'] = check_audio_description_synchronized(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_audio_description_exists'] and
            self.results['check_audio_description_synchronized']
        )
        return overall_pass, self.results