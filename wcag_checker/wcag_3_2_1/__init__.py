from .check_no_auto_submit import check as check_no_auto_submit
from .check_no_new_window import check as check_no_new_window
from .check_no_focus_change import check as check_no_focus_change

class WCAG3_2_1Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_no_auto_submit': False,
            'check_no_new_window': False,
            'check_no_focus_change': False
        }

    def run_checks(self):
        try:
            print("\nRunning check_no_auto_submit...")
            self.results['check_no_auto_submit'] = check_no_auto_submit(self.url)
            print(f"check_no_auto_submit completed: {self.results['check_no_auto_submit']}")
        except Exception as e:
            print(f"Error in check_no_auto_submit: {str(e)}")
            self.results['check_no_auto_submit'] = False

        try:
            print("\nRunning check_no_new_window...")
            self.results['check_no_new_window'] = check_no_new_window(self.url)
            print(f"check_no_new_window completed: {self.results['check_no_new_window']}")
        except Exception as e:
            print(f"Error in check_no_new_window: {str(e)}")
            self.results['check_no_new_window'] = False

        try:
            print("\nRunning check_no_focus_change...")
            self.results['check_no_focus_change'] = check_no_focus_change(self.url)
            print(f"check_no_focus_change completed: {self.results['check_no_focus_change']}")
        except Exception as e:
            print(f"Error in check_no_focus_change: {str(e)}")
            self.results['check_no_focus_change'] = False

    def evaluate(self):
        print("\nEvaluating results...")
        for check, result in self.results.items():
            print(f"- {check}: {'Pass' if result else 'Fail'}")
        
        overall_pass = all(self.results.values())
        print(f"Overall result: {'Pass' if overall_pass else 'Fail'}")
        
        return overall_pass, self.results