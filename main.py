import sys
import importlib
import pkgutil

def import_checkers():
    checkers = {}
    package = importlib.import_module('wcag_checker')
    
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        if module_name.startswith('wcag_') and '_' in module_name[5:]:
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
                print(f"Error processing {module_name}: {str(e)}")
    
    return checkers

def run_wcag_check(checker_class, url, criterion):
    try:
        checker = checker_class(url)
        checker.run_checks()
        overall_pass, results = checker.evaluate()

        print(f"\nWCAG {criterion} Check Result for {url}:")
        print(f"Overall: {'Pass' if overall_pass else 'Fail'}\n")
        print("Detailed Results:")
        for check, result in results.items():
            print(f"- {check}: {'Pass' if result else 'Fail'}")
        return overall_pass, results
            
    except Exception as e:
        print(f"\nWarning: Error during WCAG {criterion} check")
        print(f"Error details: {str(e)}")
        return False, {'error': str(e)}

def main(url, criterion=None):
    try:
        checkers = import_checkers()
        sorted_criteria = sorted(checkers.keys())
        results = []
        
        if criterion:
            continue_after = criterion.endswith('-')
            normalized_criterion = criterion.rstrip('-')
            
            start_index = next((i for i in range(len(sorted_criteria)) 
                              if sorted_criteria[i].startswith(normalized_criterion)), -1)
            
            if start_index == -1:
                print(f"エラー: 達成基準 {normalized_criterion} が見つかりません。")
                print("\n利用可能な達成基準:")
                for c in sorted_criteria:
                    print(f"- {c}")
                return
            
            target_criteria = sorted_criteria[start_index:] if continue_after else [sorted_criteria[start_index]]
        else:
            target_criteria = sorted_criteria

        for current_criterion in target_criteria:
            try:
                print(f"\n************ Running WCAG check: {current_criterion} ************")
                success, check_results = run_wcag_check(checkers[current_criterion], url, current_criterion)
                results.append({
                    'criterion': current_criterion,
                    'success': success,
                    'results': check_results
                })
            except Exception as e:
                print(f"Warning: Error in criterion {current_criterion}: {str(e)}")
                results.append({
                    'criterion': current_criterion,
                    'success': False,
                    'error': str(e)
                })
                continue

        # 最終結果の表示
        print("\n============ Summary ============")
        for result in results:
            status = "Success" if result['success'] else "Failed"
            error_msg = f" (Error: {result['error']})" if 'error' in result else ""
            print(f"{result['criterion']}: {status}{error_msg}")

    except Exception as e:
        print(f"Error in main process: {str(e)}")
        return False

if __name__ == "__main__":
    try:
        if len(sys.argv) not in [2, 3]:
            print("Usage: python main.py <url> [<criterion>]")
        else:
            url = sys.argv[1]
            criterion = sys.argv[2] if len(sys.argv) == 3 else None
            main(url, criterion)
    except Exception as e:
        print(f"Fatal error: {str(e)}")
