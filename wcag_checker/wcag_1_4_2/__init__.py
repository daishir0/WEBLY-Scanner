from .check_autoplay_audio import check as check_autoplay_audio
from .check_pause_stop_mechanism import check as check_pause_stop_mechanism
from .check_volume_control import check as check_volume_control

class WCAG1_4_2Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_autoplay_audio': False,
            'check_pause_stop_mechanism': False,
            'check_volume_control': False
        }

    def run_checks(self):
        self.results['check_autoplay_audio'] = check_autoplay_audio(self.url)
        if self.results['check_autoplay_audio']:
            self.results['check_pause_stop_mechanism'] = check_pause_stop_mechanism(self.url)
            self.results['check_volume_control'] = check_volume_control(self.url)

    def evaluate(self):
        if not self.results['check_autoplay_audio']:
            overall_pass = True
        else:
            overall_pass = (
                self.results['check_pause_stop_mechanism'] or
                self.results['check_volume_control']
            )
        return overall_pass, self.results