from .check_ui_component_control import check as check_ui_component_control
from .check_disable_motion import check as check_disable_motion
from .check_accessibility_supported_interface import check as check_accessibility_supported_interface
from .check_motion_essential import check as check_motion_essential

class WCAG2_5_4Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_ui_component_control': False,
            'check_disable_motion': False,
            'check_accessibility_supported_interface': False,
            'check_motion_essential': False
        }

    def run_checks(self):
        self.results['check_ui_component_control'] = check_ui_component_control(self.url)
        self.results['check_disable_motion'] = check_disable_motion(self.url)
        self.results['check_accessibility_supported_interface'] = check_accessibility_supported_interface(self.url)
        self.results['check_motion_essential'] = check_motion_essential(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_ui_component_control'] and
            self.results['check_disable_motion'] and
            (self.results['check_accessibility_supported_interface'] or
             self.results['check_motion_essential'])
        )
        return overall_pass, self.results