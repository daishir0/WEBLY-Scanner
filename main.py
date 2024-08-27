import sys
import importlib
import pkgutil

def import_checkers():
    checkers = {}
    package = importlib.import_module('wcag_checker')
    # print("Searching for checker modules...")
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        if module_name.startswith('wcag_'):
            try:
                module = importlib.import_module(f'wcag_checker.{module_name}')
                class_name = f"WCAG{module_name.split('_', 1)[1].upper().replace('_', '_')}Checker"
                # print(f"Looking for class: {class_name}")  # デバッグ出力
                if hasattr(module, class_name):
                    checker_class = getattr(module, class_name)
                    criterion = module_name.split('_', 1)[1].replace('_', '.')
                    checkers[criterion] = checker_class
                    # print(f"Added checker: {criterion}")
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

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <url>")
        return

    url = sys.argv[1]
    # print(f"Checking URL: {url}")  # デバッグ出力
    wcag_checks = import_checkers()
    # print(f"Found {len(wcag_checks)} checkers")  # デバッグ出力

    for criterion, checker_class in wcag_checks.items():
        run_wcag_check(checker_class, url, criterion)

if __name__ == "__main__":
    main()
