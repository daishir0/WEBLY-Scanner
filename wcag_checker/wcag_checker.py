import importlib
import os
from . import utils

class WCAGChecker:
    def __init__(self, criterion):
        self.criterion = criterion
        self.modules = {}
        self.load_modules()

    def load_modules(self):
        module_dir = f'wcag_checker.wcag_{self.criterion.replace(".", "_")}'
        for filename in os.listdir(os.path.join(os.path.dirname(__file__), f'wcag_{self.criterion.replace(".", "_")}')):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                module = importlib.import_module(f'{module_dir}.{module_name}')
                self.modules[module_name] = module.check

    def check(self, url):
        results = {}
        for module_name, check_function in self.modules.items():
            results[module_name] = check_function(url)
        return self.evaluate_results(results)

    def evaluate_results(self, results):
        # For WCAG criteria, all checks must pass
        overall_result = all(result for result in results.values() if result is not None)
        return {
            'overall': overall_result,
            'details': results
        }
