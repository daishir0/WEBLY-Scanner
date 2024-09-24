from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from wcag_checker.utils import get_webdriver

def check(url):
    driver = get_webdriver()
    try:
        driver.get(url)
        original_handles = driver.window_handles
        elements = driver.find_elements(By.XPATH, "//*")
        for element in elements:
            try:
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(element)
                )
                element.send_keys("\t")
            except (TimeoutException, ElementNotInteractableException):
                continue
            if len(driver.window_handles) > len(original_handles):
                return False
        return True
    finally:
        driver.quit()