from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def check(url):
    driver = webdriver.Chrome()
    driver.get(url)
    
    try:
        # ページ内の全てのフォーカス可能な要素を取得
        focusable_elements = driver.find_elements(By.CSS_SELECTOR, 'a, button, input, select, textarea, [tabindex]:not([tabindex="-1"])')
        
        for i, element in enumerate(focusable_elements):
            element.send_keys(Keys.TAB)
            if element == driver.switch_to.active_element:
                # 次の要素にフォーカスを移動できるか確認
                if i < len(focusable_elements) - 1:
                    focusable_elements[i+1].send_keys(Keys.TAB)
                    if focusable_elements[i+1] == driver.switch_to.active_element:
                        return True
                else:
                    # 最後の要素の場合、最初の要素にフォーカスが戻るか確認
                    focusable_elements[0].send_keys(Keys.TAB)
                    if focusable_elements[0] == driver.switch_to.active_element:
                        return True
        
        return False
    finally:
        driver.quit()