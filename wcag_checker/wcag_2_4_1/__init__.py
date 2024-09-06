from .check_skip_link import check as check_skip_link
from .check_aria_landmarks import check as check_aria_landmarks
from .check_headings import check as check_headings
from .check_frames import check as check_frames
from .check_collapsible_menu import check as check_collapsible_menu

class WCAG2_4_1Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_skip_link': False,
            'check_aria_landmarks': False,
            'check_headings': False,
            'check_frames': False,
            'check_collapsible_menu': False
        }

    def run_checks(self):
        self.results['check_skip_link'] = check_skip_link(self.url)
        self.results['check_aria_landmarks'] = check_aria_landmarks(self.url)
        self.results['check_headings'] = check_headings(self.url)
        self.results['check_frames'] = check_frames(self.url)
        self.results['check_collapsible_menu'] = check_collapsible_menu(self.url)

    def evaluate(self):
        bypass_mechanism = (
            self.results['check_skip_link'] or
            self.results['check_aria_landmarks'] or
            self.results['check_headings'] or
            self.results['check_frames'] or
            self.results['check_collapsible_menu']
        )
        overall_pass = bypass_mechanism
        return overall_pass, self.results