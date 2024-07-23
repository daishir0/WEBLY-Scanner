import sys
from wcag_checker.wcag_2_4_2 import WCAG2_4_2Checker
from wcag_checker.wcag_3_1_1 import WCAG3_1_1Checker
from wcag_checker.wcag_3_1_2 import WCAG3_1_2Checker

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <url>")
        return

    url = sys.argv[1]
    
    # WCAG 2.4.2 チェック
    checker_2_4_2 = WCAG2_4_2Checker(url)
    checker_2_4_2.run_checks()
    overall_pass_2_4_2, results_2_4_2 = checker_2_4_2.evaluate()

    print(f"WCAG 2.4.2 Check Result for {url}:")
    print(f"Overall: {'Pass' if overall_pass_2_4_2 else 'Fail'}\n")
    print("Detailed Results:")
    for check, result in results_2_4_2.items():
        print(f"- {check}: {'Pass' if result else 'Fail'}")
    
    # WCAG 3.1.1 チェック
    checker_3_1_1 = WCAG3_1_1Checker(url)
    checker_3_1_1.run_checks()
    overall_pass_3_1_1, results_3_1_1 = checker_3_1_1.evaluate()

    print(f"\nWCAG 3.1.1 Check Result for {url}:")
    print(f"Overall: {'Pass' if overall_pass_3_1_1 else 'Fail'}\n")
    print("Detailed Results:")
    for check, result in results_3_1_1.items():
        print(f"- {check}: {'Pass' if result else 'Fail'}")
    
    # WCAG 3.1.2 チェック
    checker_3_1_2 = WCAG3_1_2Checker(url)
    checker_3_1_2.run_checks()
    overall_pass_3_1_2, results_3_1_2 = checker_3_1_2.evaluate()

    print(f"\nWCAG 3.1.2 Check Result for {url}:")
    print(f"Overall: {'Pass' if overall_pass_3_1_2 else 'Fail'}\n")
    print("Detailed Results:")
    for check, result in results_3_1_2.items():
        print(f"- {check}: {'Pass' if result else 'Fail'}")

if __name__ == "__main__":
    main()