from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from wcag_checker.utils import get_webdriver

def check(url):
    driver = get_webdriver()
    try:
        driver.get(url)
        forms = driver.find_elements(By.TAG_NAME, "form")
        for form in forms:
            inputs = form.find_elements(By.TAG_NAME, "input")
            for input_element in inputs:
                original_url = driver.current_url
                input_element.send_keys("test")
                try:
                    WebDriverWait(driver, 10).until(
                        EC.staleness_of(input_element)
                    )
                except TimeoutException:
                    continue
                if driver.current_url != original_url:
                    return False
        return True
    finally:
        driver.quit()