from .check_headings_exist import check as check_headings_exist
from .check_labels_exist import check as check_labels_exist
from .check_headings_describe_topic_or_purpose import check as check_headings_describe_topic_or_purpose
from .check_labels_describe_topic_or_purpose import check as check_labels_describe_topic_or_purpose

class WCAG2_4_6Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_headings_exist': False,
            'check_labels_exist': False,
            'check_headings_describe_topic_or_purpose': False,
            'check_labels_describe_topic_or_purpose': False
        }

    def run_checks(self):
        self.results['check_headings_exist'] = check_headings_exist(self.url)
        self.results['check_labels_exist'] = check_labels_exist(self.url)
        self.results['check_headings_describe_topic_or_purpose'] = check_headings_describe_topic_or_purpose(self.url)
        self.results['check_labels_describe_topic_or_purpose'] = check_labels_describe_topic_or_purpose(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results