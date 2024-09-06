from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        
        # フォーカス可能な要素を探す
        focusable_elements = driver.find_elements(By.CSS_SELECTOR, 
            'a, button, input, select, textarea, [tabindex]:not([tabindex="-1"])')
        
        if not focusable_elements:
            return False
        
        # キーボードでフォーカス移動できるか確認
        body = driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.TAB)
        
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ':focus'))
            )
            return True
        except:
            return False
    finally:
        driver.quit()