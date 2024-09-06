from .check_touch_input import check as check_touch_input
from .check_mouse_input import check as check_mouse_input
from .check_keyboard_input import check as check_keyboard_input
from .check_voice_input import check as check_voice_input
from .check_essential_restriction import check as check_essential_restriction
from .check_security_restriction import check as check_security_restriction
from .check_user_settings_restriction import check as check_user_settings_restriction

class WCAG2_5_6Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_touch_input': False,
            'check_mouse_input': False,
            'check_keyboard_input': False,
            'check_voice_input': False,
            'check_essential_restriction': False,
            'check_security_restriction': False,
            'check_user_settings_restriction': False
        }

    def run_checks(self):
        self.results['check_touch_input'] = check_touch_input(self.url)
        self.results['check_mouse_input'] = check_mouse_input(self.url)
        self.results['check_keyboard_input'] = check_keyboard_input(self.url)
        self.results['check_voice_input'] = check_voice_input(self.url)
        self.results['check_essential_restriction'] = check_essential_restriction(self.url)
        self.results['check_security_restriction'] = check_security_restriction(self.url)
        self.results['check_user_settings_restriction'] = check_user_settings_restriction(self.url)

    def evaluate(self):
        input_modalities_allowed = (
            self.results['check_touch_input'] and
            self.results['check_mouse_input'] and
            self.results['check_keyboard_input'] and
            self.results['check_voice_input']
        )

        restrictions_justified = (
            self.results['check_essential_restriction'] or
            self.results['check_security_restriction'] or
            self.results['check_user_settings_restriction']
        )

        overall_pass = input_modalities_allowed or restrictions_justified
        return overall_pass, self.results