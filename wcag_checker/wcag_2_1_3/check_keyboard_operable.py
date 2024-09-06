from wcag_checker.utils import fetch_url, parse_html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check(url):
    driver = webdriver.Chrome()  # ChromeDriverのパスを適切に設定してください
    try:
        driver.get(url)
        
        # すべての対話可能な要素を取得
        interactive_elements = driver.find_elements(By.CSS_SELECTOR, 'a, button, input, select, textarea')
        
        for element in interactive_elements:
            # 要素にフォーカスを当てる
            driver.execute_script("arguments[0].focus();", element)
            
            # Enterキーを押す
            element.send_keys(Keys.ENTER)
            
            # 何らかの変化（ページ遷移やポップアップなど）を待つ
            WebDriverWait(driver, 3).until(
                EC.staleness_of(element) or 
                EC.presence_of_element_located((By.CSS_SELECTOR, '.popup, .modal'))
            )
            
            # 変化が検出されなかった場合、その要素はキーボードで操作できないと判断
            if driver.find_elements(By.CSS_SELECTOR, '.popup, .modal') or not element.is_displayed():
                print(f"Element not keyboard operable: {element.tag_name}, {element.get_attribute('class')}")
                return False
        
        return True
    except Exception as e:
        print(f"Error during keyboard operability check: {e}")
        return False
    finally:
        driver.quit()