from .check_ui_components import check_ui_components
from .check_graphical_objects import check_graphical_objects

class WCAG1_4_11Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'ui_components': False,
            'graphical_objects': False
        }

    def run_checks(self):
        self.results['ui_components'] = check_ui_components(self.url)
        self.results['graphical_objects'] = check_graphical_objects(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results