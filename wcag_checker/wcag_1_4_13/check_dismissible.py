from wcag_checker.utils import get_webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # 追加

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
            webdriver.ActionChains(driver).move_to_element(element).perform()
            
            # 追加コンテンツが表示されるのを待つ
            try:
                additional_content = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".tooltip, .popover"))
                )
            except TimeoutException:
                print("追加コンテンツが表示されませんでした")
                return False
            
            # ESCキーを押して追加コンテンツを閉じようとする
            additional_content.send_keys(Keys.ESCAPE)
            
            # 追加コンテンツが消えたかチェック
            try:
                WebDriverWait(driver, 3).until(EC.staleness_of(additional_content))
                return True
            except TimeoutException:
                print("追加コンテンツが消えませんでした")
                return False
        
        # ホバーで表示される要素が見つからない場合
        return True
    
    finally:
        driver.quit()