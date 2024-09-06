from .check_flash_frequency import check as check_flash_frequency
from .check_flash_area import check as check_flash_area
from .check_flash_pattern import check as check_flash_pattern

class WCAG2_3_1Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_flash_frequency': False,
            'check_flash_area': False,
            'check_flash_pattern': False
        }

    def run_checks(self):
        self.results['check_flash_frequency'] = check_flash_frequency(self.url)
        self.results['check_flash_area'] = check_flash_area(self.url)
        self.results['check_flash_pattern'] = check_flash_pattern(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_flash_frequency'] and
            (self.results['check_flash_area'] or self.results['check_flash_pattern'])
        )
        return overall_pass, self.results