# ./wcag_1_2_8/__init__.py

from .check_synchronized_media import check as check_synchronized_media
from .check_video_only_media import check as check_video_only_media

class WCAG1_2_8Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_synchronized_media': False,
            'check_video_only_media': False
        }

    def run_checks(self):
        self.results['check_synchronized_media'] = check_synchronized_media(self.url)
        self.results['check_video_only_media'] = check_video_only_media(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_synchronized_media'] or
            self.results['check_video_only_media']
        )
        return overall_pass, self.results