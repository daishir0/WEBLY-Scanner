from .check_label_exists import check as check_label_exists
from .check_instruction_exists import check as check_instruction_exists
from .check_input_fields_identified import check as check_input_fields_identified
from .check_data_format_specified import check as check_data_format_specified

class WCAG3_3_2Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_label_exists': False,
            'check_instruction_exists': False,
            'check_input_fields_identified': False,
            'check_data_format_specified': False
        }

    def run_checks(self):
        self.results['check_label_exists'] = check_label_exists(self.url)
        self.results['check_instruction_exists'] = check_instruction_exists(self.url)
        self.results['check_input_fields_identified'] = check_input_fields_identified(self.url)
        self.results['check_data_format_specified'] = check_data_format_specified(self.url)

    def evaluate(self):
        overall_pass = (
            (self.results['check_label_exists'] or self.results['check_instruction_exists']) and
            self.results['check_input_fields_identified'] and
            self.results['check_data_format_specified']
        )
        return overall_pass, self.results