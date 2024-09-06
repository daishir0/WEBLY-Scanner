from wcag_checker.utils import fetch_url, parse_html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def check(url):
    driver = webdriver.Chrome()
    driver.get(url)
    
    try:
        # ページ内の全てのフォーカス可能な要素を取得
        focusable_elements = driver.find_elements(By.CSS_SELECTOR, 'a, button, input, select, textarea, [tabindex]:not([tabindex="-1"])')
        
        # 各要素にキーボードでフォーカスを当てる
        for element in focusable_elements:
            element.send_keys(Keys.TAB)
            if element == driver.switch_to.active_element:
                return True
        
        return False
    finally:
        driver.quit()