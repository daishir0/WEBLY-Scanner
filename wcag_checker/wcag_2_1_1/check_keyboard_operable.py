from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        
        # すべての対話可能な要素を取得
        interactive_elements = driver.find_elements(By.CSS_SELECTOR, 'a, button, input, select, textarea')
        
        for element in interactive_elements:
            # 要素にフォーカスを当てる
            element.send_keys(Keys.TAB)
            
            # フォーカスが当たっているか確認
            focused_element = driver.switch_to.active_element
            if focused_element != element:
                return False
            
            # エンターキーを押して操作を試みる
            focused_element.send_keys(Keys.ENTER)
            
            # 何らかの変化（ページ遷移やポップアップなど）が起きたか確認
            try:
                WebDriverWait(driver, 3).until(EC.staleness_of(element))
                return True
            except:
                pass
        
        return True
    finally:
        driver.quit()