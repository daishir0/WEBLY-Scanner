from .check_flash_frequency import check as check_flash_frequency
from .check_flash_luminance import check as check_flash_luminance
from .check_flash_red import check as check_flash_red
from .check_flash_area import check as check_flash_area

class WCAG2_3_2Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_flash_frequency': False,
            'check_flash_luminance': False,
            'check_flash_red': False,
            'check_flash_area': False
        }

    def run_checks(self):
        self.results['check_flash_frequency'] = check_flash_frequency(self.url)
        self.results['check_flash_luminance'] = check_flash_luminance(self.url)
        self.results['check_flash_red'] = check_flash_red(self.url)
        self.results['check_flash_area'] = check_flash_area(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_flash_frequency'] and
            self.results['check_flash_luminance'] and
            self.results['check_flash_red'] and
            self.results['check_flash_area']
        )
        return overall_pass, self.results