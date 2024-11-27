from wcag_checker.utils import get_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException  # 追加
from selenium.webdriver.common.action_chains import ActionChains  # 追加
import time

def check(url):
    driver = get_webdriver()
    try:
        driver.get(url)
        
        # ホバーで表示される要素を探す
        hover_elements = driver.find_elements(By.CSS_SELECTOR, "[title], [data-tooltip]")
        
        if not hover_elements:
            print("ホバーで表示される要素が見つかりませんでした")
            return False
        
        for element in hover_elements:
            # 要素にホバー
            try:
                ActionChains(driver).move_to_element(element).perform()
            except ElementNotInteractableException:
                print(f"要素 {element} にホバーできませんでした。")
                continue  # 次の要素に進む
            
            # 追加コンテンツが表示されるのを待つ
            try:
                additional_content = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".tooltip, .popover"))
                )
            except TimeoutException:
                print("追加コンテンツが表示されませんでした")
                return False
            
            # 3秒待機
            time.sleep(3)
            
            # 追加コンテンツが表示されたままかチェック
            if additional_content.is_displayed():
                return True
            else:
                print("追加コンテンツが表示されませんでした")
                return False
        
        # ホバーで表示される要素が見つからない場合
        return True
    
    finally:
        driver.quit()