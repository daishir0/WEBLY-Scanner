from .check_color_selection import check as check_color_selection
from .check_text_width import check as check_text_width
from .check_text_alignment import check as check_text_alignment
from .check_line_spacing import check as check_line_spacing
from .check_text_resize import check as check_text_resize

class WCAG1_4_8Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_color_selection': False,
            'check_text_width': False,
            'check_text_alignment': False,
            'check_line_spacing': False,
            'check_text_resize': False
        }

    def run_checks(self):
        self.results['check_color_selection'] = check_color_selection(self.url)
        self.results['check_text_width'] = check_text_width(self.url)
        self.results['check_text_alignment'] = check_text_alignment(self.url)
        self.results['check_line_spacing'] = check_line_spacing(self.url)
        self.results['check_text_resize'] = check_text_resize(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results