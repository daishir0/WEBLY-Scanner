# ./wcag_1_2_1/__init__.py

from .check_audio_only import check as check_audio_only
from .check_video_only import check as check_video_only
from .check_media_alternative import check as check_media_alternative

class WCAG1_2_1Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_audio_only': None,
            'check_video_only': None,
            'check_media_alternative': None
        }

    def run_checks(self):
        self.results['check_audio_only'] = check_audio_only(self.url)
        self.results['check_video_only'] = check_video_only(self.url)
        self.results['check_media_alternative'] = check_media_alternative(self.url)

    def evaluate(self):
        overall_pass = all(result for result in self.results.values() if result is not None)
        return overall_pass, self.results