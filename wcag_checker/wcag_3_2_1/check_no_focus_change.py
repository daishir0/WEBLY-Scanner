from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from wcag_checker.utils import get_webdriver

def check(url):
    driver = get_webdriver()
    try:
        driver.get(url)
        elements = driver.find_elements(By.XPATH, "//*")
        for element in elements:
            original_active = driver.switch_to.active_element
            ActionChains(driver).move_to_element(element).perform()
            if driver.switch_to.active_element != original_active:
                return False
        return True
    finally:
        driver.quit()