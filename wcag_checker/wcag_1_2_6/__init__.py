from .check_sign_language_provided import check as check_sign_language_provided
from .check_all_audio_content_covered import check as check_all_audio_content_covered
from .check_synchronized_media import check as check_synchronized_media

class WCAG1_2_6Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_sign_language_provided': False,
            'check_all_audio_content_covered': False,
            'check_synchronized_media': False
        }

    def run_checks(self):
        self.results['check_sign_language_provided'] = check_sign_language_provided(self.url)
        self.results['check_all_audio_content_covered'] = check_all_audio_content_covered(self.url)
        self.results['check_synchronized_media'] = check_synchronized_media(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results
