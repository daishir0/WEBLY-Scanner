from selenium.webdriver.common.by import By
from wcag_checker.utils import get_webdriver

def check(url):
    driver = get_webdriver()
    try:
        driver.get(url)
        
        links = driver.find_elements(By.TAG_NAME, 'a')
        
        for i, link in enumerate(links):
            try:
                target = link.get_attribute('target')
                if target and target == '_blank':
                    return False
            except Exception as e:
                continue
        
        return True
    except Exception as e:
        return False
    finally:
        driver.quit()