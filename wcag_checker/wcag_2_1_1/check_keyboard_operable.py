from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wcag_checker.utils import get_webdriver
from selenium.common.exceptions import ElementNotInteractableException

def check(url):
    driver = get_webdriver()
    try:
        driver.get(url)
        
        # すべての対話可能な要素を取得
        interactive_elements = driver.find_elements(By.CSS_SELECTOR, 'a, button, input, select, textarea')
        
        for element in interactive_elements:
            # 要素にフォーカスを当てる
            try:
                element.send_keys(Keys.TAB)
            except ElementNotInteractableException:
                print(f"要素 {element} にフォーカスを当てることができませんでした。")
                continue  # 次の要素に進む
            
            # フォーカスが当たっているか確認
            focused_element = driver.switch_to.active_element
            if focused_element != element:
                return False
            
            # エンターキーを押して操作を試みる
            try:
                focused_element.send_keys(Keys.ENTER)
            except ElementNotInteractableException:
                print(f"要素 {focused_element} にエンターキーを送信できませんでした。")
                continue  # 次の要素に進む
            
            # 何らかの変化（ページ遷移やポップアップなど）が起きたか確認
            try:
                WebDriverWait(driver, 3).until(EC.staleness_of(element))
                return True
            except:
                pass
        
        return True
    finally:
        driver.quit()