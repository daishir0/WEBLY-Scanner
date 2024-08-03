import sys
from wcag_checker.wcag_2_4_2 import WCAG2_4_2Checker
from wcag_checker.wcag_3_1_1 import WCAG3_1_1Checker
from wcag_checker.wcag_3_1_2 import WCAG3_1_2Checker
from wcag_checker.wcag_1_1_1 import WCAG1_1_1Checker
from wcag_checker.wcag_1_3_1 import WCAG1_3_1Checker
from wcag_checker.wcag_2_2_2 import WCAG2_2_2Checker

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
    wcag_checks = [
        (WCAG2_4_2Checker, "2.4.2"),
        (WCAG3_1_1Checker, "3.1.1"),
        (WCAG3_1_2Checker, "3.1.2"),
        (WCAG1_1_1Checker, "1.1.1"),
        (WCAG1_3_1Checker, "1.3.1"),
        (WCAG2_2_2Checker, "2.2.2")
    ]

    for checker_class, criterion in wcag_checks:
        run_wcag_check(checker_class, url, criterion)

if __name__ == "__main__":
    main()
