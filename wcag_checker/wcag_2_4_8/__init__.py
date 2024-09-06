from .check_breadcrumb import check as check_breadcrumb
from .check_sitemap import check as check_sitemap
from .check_navigation_bar import check as check_navigation_bar
from .check_page_relationship import check as check_page_relationship

class WCAG2_4_8Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_breadcrumb': False,
            'check_sitemap': False,
            'check_navigation_bar': False,
            'check_page_relationship': False
        }

    def run_checks(self):
        self.results['check_breadcrumb'] = check_breadcrumb(self.url)
        self.results['check_sitemap'] = check_sitemap(self.url)
        self.results['check_navigation_bar'] = check_navigation_bar(self.url)
        self.results['check_page_relationship'] = check_page_relationship(self.url)

    def evaluate(self):
        overall_pass = any(self.results.values())
        return overall_pass, self.results