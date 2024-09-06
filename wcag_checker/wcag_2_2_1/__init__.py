from .check_disable_time_limit import check as check_disable_time_limit
from .check_adjust_time_limit import check as check_adjust_time_limit
from .check_extend_time_limit import check as check_extend_time_limit
from .check_realtime_exception import check as check_realtime_exception
from .check_essential_exception import check as check_essential_exception
from .check_20hour_exception import check as check_20hour_exception

class WCAG2_2_1Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_disable_time_limit': False,
            'check_adjust_time_limit': False,
            'check_extend_time_limit': False,
            'check_realtime_exception': False,
            'check_essential_exception': False,
            'check_20hour_exception': False
        }

    def run_checks(self):
        self.results['check_disable_time_limit'] = check_disable_time_limit(self.url)
        self.results['check_adjust_time_limit'] = check_adjust_time_limit(self.url)
        self.results['check_extend_time_limit'] = check_extend_time_limit(self.url)
        self.results['check_realtime_exception'] = check_realtime_exception(self.url)
        self.results['check_essential_exception'] = check_essential_exception(self.url)
        self.results['check_20hour_exception'] = check_20hour_exception(self.url)

    def evaluate(self):
        overall_pass = any([
            self.results['check_disable_time_limit'],
            self.results['check_adjust_time_limit'],
            self.results['check_extend_time_limit'],
            self.results['check_realtime_exception'],
            self.results['check_essential_exception'],
            self.results['check_20hour_exception']
        ])
        return overall_pass, self.results