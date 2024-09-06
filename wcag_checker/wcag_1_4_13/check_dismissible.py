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
        
        # ホバーで表示される要素を探す
        hover_elements = driver.find_elements(By.CSS_SELECTOR, "[title], [data-tooltip]")
        
        for element in hover_elements:
            # 要素にホバー
            webdriver.ActionChains(driver).move_to_element(element).perform()
            
            # 追加コンテンツが表示されるのを待つ
            additional_content = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".tooltip, .popover"))
            )
            
            # ESCキーを押して追加コンテンツを閉じようとする
            additional_content.send_keys(Keys.ESCAPE)
            
            # 追加コンテンツが消えたかチェック
            try:
                WebDriverWait(driver, 3).until(EC.staleness_of(additional_content))
                return True
            except:
                return False
        
        # ホバーで表示される要素が見つからない場合
        return True
    
    finally:
        driver.quit()