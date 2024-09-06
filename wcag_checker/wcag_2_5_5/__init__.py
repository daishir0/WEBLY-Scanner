from .check_target_size import check as check_target_size
from .check_equivalent_target import check as check_equivalent_target
from .check_inline_target import check as check_inline_target
from .check_user_agent_control import check as check_user_agent_control
from .check_essential_target import check as check_essential_target

class WCAG2_5_5Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_target_size': False,
            'check_equivalent_target': False,
            'check_inline_target': False,
            'check_user_agent_control': False,
            'check_essential_target': False
        }

    def run_checks(self):
        self.results['check_target_size'] = check_target_size(self.url)
        self.results['check_equivalent_target'] = check_equivalent_target(self.url)
        self.results['check_inline_target'] = check_inline_target(self.url)
        self.results['check_user_agent_control'] = check_user_agent_control(self.url)
        self.results['check_essential_target'] = check_essential_target(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_target_size'] or
            self.results['check_equivalent_target'] or
            self.results['check_inline_target'] or
            self.results['check_user_agent_control'] or
            self.results['check_essential_target']
        )
        return overall_pass, self.results