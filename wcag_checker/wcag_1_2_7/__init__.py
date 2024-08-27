from .check_extended_audio_description_exists import check as check_extended_audio_description_exists
from .check_extended_audio_description_for_all_content import check as check_extended_audio_description_for_all_content
from .check_synchronized_media import check as check_synchronized_media

class WCAG1_2_7Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_extended_audio_description_exists': False,
            'check_extended_audio_description_for_all_content': False,
            'check_synchronized_media': False
        }

    def run_checks(self):
        self.results['check_extended_audio_description_exists'] = check_extended_audio_description_exists(self.url)
        self.results['check_extended_audio_description_for_all_content'] = check_extended_audio_description_for_all_content(self.url)
        self.results['check_synchronized_media'] = check_synchronized_media(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        if overall_pass:
            print("WARNING: Manual check required for insufficient pauses in foreground audio.")
        return overall_pass, self.results