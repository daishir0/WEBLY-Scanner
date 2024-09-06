from .check_down_event_not_used import check as check_down_event_not_used
from .check_up_event_completion import check as check_up_event_completion
from .check_abort_mechanism import check as check_abort_mechanism
from .check_undo_mechanism import check as check_undo_mechanism
from .check_up_event_reversal import check as check_up_event_reversal
from .check_down_event_essential import check as check_down_event_essential

class WCAG2_5_2Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_down_event_not_used': False,
            'check_up_event_completion': False,
            'check_abort_mechanism': False,
            'check_undo_mechanism': False,
            'check_up_event_reversal': False,
            'check_down_event_essential': False
        }

    def run_checks(self):
        self.results['check_down_event_not_used'] = check_down_event_not_used(self.url)
        self.results['check_up_event_completion'] = check_up_event_completion(self.url)
        self.results['check_abort_mechanism'] = check_abort_mechanism(self.url)
        self.results['check_undo_mechanism'] = check_undo_mechanism(self.url)
        self.results['check_up_event_reversal'] = check_up_event_reversal(self.url)
        self.results['check_down_event_essential'] = check_down_event_essential(self.url)

    def evaluate(self):
        overall_pass = (
            self.results['check_down_event_not_used'] or
            (self.results['check_up_event_completion'] and 
             (self.results['check_abort_mechanism'] or self.results['check_undo_mechanism'])) or
            self.results['check_up_event_reversal'] or
            self.results['check_down_event_essential']
        )
        return overall_pass, self.results