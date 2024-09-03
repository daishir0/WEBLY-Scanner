from .check_text_alternative import check as check_text_alternative
from .check_contrast_ratio import check as check_contrast_ratio
from .check_pattern_usage import check as check_pattern_usage
from .check_programmatic_access import check as check_programmatic_access

class WCAG1_4_1Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_text_alternative': False,
            'check_contrast_ratio': False,
            'check_pattern_usage': False,
            'check_programmatic_access': False,
            'check_additional_visual_cues': None  # 手動チェックが必要
        }

    def run_checks(self):
        self.results['check_text_alternative'] = check_text_alternative(self.url)
        self.results['check_contrast_ratio'] = check_contrast_ratio(self.url)
        self.results['check_pattern_usage'] = check_pattern_usage(self.url)
        self.results['check_programmatic_access'] = check_programmatic_access(self.url)
        self.results['check_additional_visual_cues'] = "Manual check required"

    def evaluate(self):
        visual_means = (
            self.results['check_text_alternative'] or
            self.results['check_contrast_ratio'] or
            self.results['check_pattern_usage'] or
            self.results['check_additional_visual_cues'] == True
        )
        programmatic_access = self.results['check_programmatic_access']
        
        overall_pass = visual_means and programmatic_access
        return overall_pass, self.results