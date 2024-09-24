import sys
import importlib
import pkgutil

def import_checkers():
    checkers = {}
    package = importlib.import_module('wcag_checker')
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        if module_name.startswith('wcag_'):
            try:
                module = importlib.import_module(f'wcag_checker.{module_name}')
                class_name = f"WCAG{module_name.split('_', 1)[1].upper().replace('_', '_')}Checker"
                if hasattr(module, class_name):
                    checker_class = getattr(module, class_name)
                    criterion = module_name.split('_', 1)[1].replace('_', '.')
                    checkers[criterion] = checker_class
                else:
                    print(f"Class {class_name} not found in {module_name}")
            except Exception as e:
                print(f"Error processing {module_name}: {e}")
    return checkers

def run_wcag_check(checker_class, url, criterion):
    checker = checker_class(url)
    checker.run_checks()
    overall_pass, results = checker.evaluate()

    print(f"\nWCAG {criterion} Check Result for {url}:")
    print(f"Overall: {'Pass' if overall_pass else 'Fail'}\n")
    print("Detailed Results:")
    for check, result in results.items():
        print(f"- {check}: {'Pass' if result else 'Fail'}")

def main(url, criterion=None):
    checkers = import_checkers()
    if criterion:
        if criterion in checkers:
            run_wcag_check(checkers[criterion], url, criterion)
        else:
            print(f"Checker for criterion {criterion} not found.")
    else:
        for criterion, checker_class in checkers.items():
            run_wcag_check(checker_class, url, criterion)

if __name__ == "__main__":
    if len(sys.argv) not in [2, 3]:
        print("Usage: python main.py <url> [<criterion>]")
    else:
        url = sys.argv[1]
        criterion = sys.argv[2] if len(sys.argv) == 3 else None
        main(url, criterion)
