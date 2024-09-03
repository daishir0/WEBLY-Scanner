from .check_audio_content import check as check_audio_content
from .check_background_audio import check as check_background_audio

class WCAG1_4_7Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_audio_content': False,
            'check_background_audio': False
        }

    def run_checks(self):
        self.results['check_audio_content'] = check_audio_content(self.url)
        self.results['check_background_audio'] = check_background_audio(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_audio_content'] and
            self.results['check_background_audio']
        )
        return overall_pass, self.results