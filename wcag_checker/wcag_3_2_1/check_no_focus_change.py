from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from wcag_checker.utils import get_webdriver

def check(url):
    driver = get_webdriver()
    try:
        driver.get(url)
        
        elements = driver.find_elements(By.CSS_SELECTOR, 'a, button, input, select, textarea')
        
        for i, element in enumerate(elements):
            try:
                if element.is_displayed() and element.is_enabled():
                    original_active = driver.switch_to.active_element
                    ActionChains(driver).move_to_element(element).perform()
                    if driver.switch_to.active_element != original_active:
                        return False
            except Exception as e:
                print(f"Error with element {i+1}: {str(e)}")  # デバッグ用
                continue
        
        return True
    except Exception as e:
        print(f"Major error occurred: {str(e)}")  # デバッグ用
        return False
    finally:
        driver.quit()