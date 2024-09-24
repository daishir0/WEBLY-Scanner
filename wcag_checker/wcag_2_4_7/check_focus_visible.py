from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from wcag_checker.utils import get_webdriver

def check(url):
    driver = get_webdriver()
    try:
        driver.get(url)
        
        # フォーカス可能な要素を探す
        focusable_elements = driver.find_elements(By.CSS_SELECTOR, 
            'a, button, input, select, textarea, [tabindex]:not([tabindex="-1"])')
        
        for element in focusable_elements:
            element.send_keys(Keys.TAB)
            focused_element = driver.switch_to.active_element
            
            # フォーカス時のスタイルを取得
            normal_style = element.get_attribute('style')
            focused_style = focused_element.get_attribute('style')
            
            if normal_style != focused_style:
                return True
        
        return False
    finally:
        driver.quit()