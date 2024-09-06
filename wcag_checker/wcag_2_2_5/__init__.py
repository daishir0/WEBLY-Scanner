from .check_session_expiration import check as check_session_expiration
from .check_reauthentication_mechanism import check as check_reauthentication_mechanism
from .check_data_preservation import check as check_data_preservation
from .check_data_restoration import check as check_data_restoration

class WCAG2_2_5Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_session_expiration': False,
            'check_reauthentication_mechanism': False,
            'check_data_preservation': False,
            'check_data_restoration': False
        }

    def run_checks(self):
        self.results['check_session_expiration'] = check_session_expiration(self.url)
        self.results['check_reauthentication_mechanism'] = check_reauthentication_mechanism(self.url)
        self.results['check_data_preservation'] = check_data_preservation(self.url)
        self.results['check_data_restoration'] = check_data_restoration(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results