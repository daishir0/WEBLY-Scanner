from .check_sitemap import check as check_sitemap
from .check_table_of_contents import check as check_table_of_contents
from .check_search_function import check as check_search_function
from .check_related_links import check as check_related_links
from .check_all_pages_list import check as check_all_pages_list
from .check_home_page_links import check as check_home_page_links
from .check_process_page import check as check_process_page

class WCAG2_4_5Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_sitemap': False,
            'check_table_of_contents': False,
            'check_search_function': False,
            'check_related_links': False,
            'check_all_pages_list': False,
            'check_home_page_links': False,
            'check_process_page': True
        }

    def run_checks(self):
        self.results['check_sitemap'] = check_sitemap(self.url)
        self.results['check_table_of_contents'] = check_table_of_contents(self.url)
        self.results['check_search_function'] = check_search_function(self.url)
        self.results['check_related_links'] = check_related_links(self.url)
        self.results['check_all_pages_list'] = check_all_pages_list(self.url)
        self.results['check_home_page_links'] = check_home_page_links(self.url)
        self.results['check_process_page'] = check_process_page(self.url)

    def evaluate(self):
        navigation_methods = [
            self.results['check_sitemap'],
            self.results['check_table_of_contents'],
            self.results['check_search_function'],
            self.results['check_related_links'],
            self.results['check_all_pages_list'],
            self.results['check_home_page_links']
        ]
        
        multiple_methods_available = sum(navigation_methods) >= 2
        not_process_page = self.results['check_process_page']
        
        overall_pass = multiple_methods_available and not_process_page
        return overall_pass, self.results