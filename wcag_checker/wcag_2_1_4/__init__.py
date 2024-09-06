from .check_shortcut_off import check as check_shortcut_off
from .check_shortcut_remap import check as check_shortcut_remap
from .check_shortcut_focus import check as check_shortcut_focus

class WCAG2_1_4Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_shortcut_off': False,
            'check_shortcut_remap': False,
            'check_shortcut_focus': False
        }

    def run_checks(self):
        self.results['check_shortcut_off'] = check_shortcut_off(self.url)
        self.results['check_shortcut_remap'] = check_shortcut_remap(self.url)
        self.results['check_shortcut_focus'] = check_shortcut_focus(self.url)

    def evaluate(self):
        overall_pass = any([
            self.results['check_shortcut_off'],
            self.results['check_shortcut_remap'],
            self.results['check_shortcut_focus']
        ])
        return overall_pass, self.results