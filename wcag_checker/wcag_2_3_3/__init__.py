from .check_animation_disable import check as check_animation_disable
from .check_user_preference import check as check_user_preference
from .check_essential_animation import check as check_essential_animation

class WCAG2_3_3Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_animation_disable': False,
            'check_user_preference': False,
            'check_essential_animation': False
        }

    def run_checks(self):
        self.results['check_animation_disable'] = check_animation_disable(self.url)
        self.results['check_user_preference'] = check_user_preference(self.url)
        self.results['check_essential_animation'] = check_essential_animation(self.url)

    def evaluate(self):
        animation_control = (
            self.results['check_animation_disable'] and
            self.results['check_user_preference']
        )
        overall_pass = animation_control or self.results['check_essential_animation']
        return overall_pass, self.results