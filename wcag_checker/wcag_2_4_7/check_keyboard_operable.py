from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, StaleElementReferenceException
from wcag_checker.utils import get_webdriver
import time

def get_element_info(element, driver):
    """要素の詳細情報を取得する補助関数"""
    try:
        info = {
            'tag': element.tag_name,
            'text': element.text.strip()[:50] if element.text else '',
            'href': element.get_attribute('href'),
            'id': element.get_attribute('id'),
            'class': element.get_attribute('class'),
            'xpath': driver.execute_script("""
                function getXPath(element) {
                    if (element.id !== '')
                        return `//*[@id="${element.id}"]`;
                    if (element === document.body)
                        return '/html/body';
                    var ix = 0;
                    var siblings = element.parentNode.childNodes;
                    for (var i = 0; i < siblings.length; i++) {
                        var sibling = siblings[i];
                        if (sibling === element)
                            return getXPath(element.parentNode) + '/' + element.tagName.toLowerCase() + '[' + (ix + 1) + ']';
                        if (sibling.nodeType === 1 && sibling.tagName === element.tagName)
                            ix++;
                    }
                }
                return getXPath(arguments[0]);
                """, element)
        }
        return info
    except Exception as e:
        return {'error': str(e)}

def check_focus_state(element, driver):
    """要素のフォーカス状態をJavaScriptで安全にチェック"""
    try:
        # 要素の情報を先に取得して保存
        element_info = driver.execute_script("""
            function getElementInfo(element) {
                const style = window.getComputedStyle(element);
                return {
                    beforeStyles: {
                        outline: style.outline,
                        border: style.border,
                        boxShadow: style.boxShadow,
                        backgroundColor: style.backgroundColor,
                        color: style.color
                    }
                };
            }
            return getElementInfo(arguments[0]);
        """, element)

        # フォーカスチェックを別の実行コンテキストで実行
        focus_result = driver.execute_script("""
            function checkFocus(element) {
                element.focus();
                const isFocused = document.activeElement === element;
                const style = window.getComputedStyle(element);
                
                return {
                    focusable: isFocused,
                    afterStyles: {
                        outline: style.outline,
                        border: style.border,
                        boxShadow: style.boxShadow,
                        backgroundColor: style.backgroundColor,
                        color: style.color
                    }
                };
            }
            return checkFocus(arguments[0]);
        """, element)

        # 結果を組み合わせて返却
        beforeStyles = element_info['beforeStyles']
        afterStyles = focus_result['afterStyles']
        
        hasVisibleIndicator = (
            beforeStyles['outline'] != afterStyles['outline'] or
            beforeStyles['border'] != afterStyles['border'] or
            beforeStyles['boxShadow'] != afterStyles['boxShadow'] or
            beforeStyles['backgroundColor'] != afterStyles['backgroundColor'] or
            beforeStyles['color'] != afterStyles['color']
        )

        return {
            'status': 'success',
            'focusable': focus_result['focusable'],
            'hasVisibleIndicator': hasVisibleIndicator,
            'styles': {
                'before': beforeStyles,
                'after': afterStyles
            }
        }

    except Exception as e:
        return {
            'status': 'error',
            'error': str(e)
        }

def check(url):
    driver = None
    results = {
        'success': False,
        'elements': [],
        'error': None
    }
    
    try:
        driver = get_webdriver()
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        interactive_elements = driver.find_elements(By.CSS_SELECTOR, 
            'a, button, input, select, textarea, [tabindex]:not([tabindex="-1"])')
        
        for index, element in enumerate(interactive_elements, 1):
            try:
                element_info = {
                    'tag': element.tag_name,
                    'text': element.text.strip()[:50] if element.text else '',
                    'href': element.get_attribute('href'),
                    'xpath': element.get_attribute("xpath")
                }
                
                print(f"\nChecking element {index}/{len(interactive_elements)}:")
                print(f"- Tag: {element_info['tag']}")
                print(f"- Text: {element_info['text']}")
                if element_info['href']:
                    print(f"- Href: {element_info['href']}")
                
                focus_state = check_focus_state(element, driver)
                
                results['elements'].append({
                    'info': element_info.copy(),
                    'focus_state': focus_state.copy()
                })
                
                if focus_state['status'] == 'success':
                    print("Result: Focus check completed")
                    print(f"- Focusable: {focus_state['focusable']}")
                    print(f"- Has visible indicator: {focus_state['hasVisibleIndicator']}")
                
            except Exception as e:
                print(f"Warning: Error processing element - {str(e)}")
                results['elements'].append({
                    'info': element_info if 'element_info' in locals() else {},
                    'error': str(e)
                })
                continue
        
        results['success'] = True
        
    except Exception as e:
        print(f"Error during check: {str(e)}")
        results['error'] = str(e)
    
    finally:
        if driver:
            try:
                driver.quit()
            except Exception as e:
                print(f"Warning: Error while closing browser - {str(e)}")
                results['browser_close_error'] = str(e)
    
    return results