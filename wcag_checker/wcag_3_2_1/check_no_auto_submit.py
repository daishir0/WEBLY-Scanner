from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        forms = driver.find_elements(By.TAG_NAME, "form")
        for form in forms:
            inputs = form.find_elements(By.TAG_NAME, "input")
            for input_element in inputs:
                original_url = driver.current_url
                input_element.send_keys("test")
                WebDriverWait(driver, 3).until(
                    EC.url_changes(original_url)
                )
                if driver.current_url != original_url:
                    return False
        return True
    finally:
        driver.quit()