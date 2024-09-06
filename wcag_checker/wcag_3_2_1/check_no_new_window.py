from selenium import webdriver
from selenium.webdriver.common.by import By

def check(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        original_handles = driver.window_handles
        elements = driver.find_elements(By.XPATH, "//*")
        for element in elements:
            element.send_keys("\t")
            if len(driver.window_handles) > len(original_handles):
                return False
        return True
    finally:
        driver.quit()