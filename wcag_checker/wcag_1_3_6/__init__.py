from .check_ui_components import check as check_ui_components
from .check_icons import check as check_icons
from .check_regions import check as check_regions

class WCAG1_3_6Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_ui_components': False,
            'check_icons': False,
            'check_regions': False
        }

    def run_checks(self):
        self.results['check_ui_components'] = check_ui_components(self.url)
        self.results['check_icons'] = check_icons(self.url)
        self.results['check_regions'] = check_regions(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results