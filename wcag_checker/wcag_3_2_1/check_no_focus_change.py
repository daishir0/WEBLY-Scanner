from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from wcag_checker.utils import get_webdriver

def check(url):
    driver = get_webdriver()
    try:
        print("Opening page...")
        driver.get(url)
        
        print("Finding interactive elements...")
        elements = driver.find_elements(By.CSS_SELECTOR, 'a, button, input, select, textarea')
        print(f"Found {len(elements)} interactive elements")
        
        for i, element in enumerate(elements, 1):
            try:
                if element.is_displayed() and element.is_enabled():
                    print(f"\nChecking element {i}/{len(elements)}")
                    print(f"- Tag: {element.tag_name}")
                    print(f"- Text: {element.text[:50] if element.text else ''}")
                    
                    original_active = driver.switch_to.active_element
                    print("Moving to element...")
                    ActionChains(driver).move_to_element(element).perform()
                    
                    if driver.switch_to.active_element != original_active:
                        print("Focus changed unexpectedly")
                        return False
                    print("Focus check passed")
                    
            except Exception as e:
                print(f"Warning: Error checking element {i}: {str(e)}")
                continue
        
        print("\nAll elements checked successfully")
        return True
        
    except Exception as e:
        print(f"Error during focus change check: {str(e)}")
        return False
        
    finally:
        print("Closing browser...")
        try:
            driver.quit()
        except Exception as e:
            print(f"Warning: Error while closing browser - {str(e)}")