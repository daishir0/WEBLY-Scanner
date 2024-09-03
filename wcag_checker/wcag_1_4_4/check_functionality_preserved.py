from wcag_checker.utils import fetch_url, parse_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def check(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        original_clickable = driver.find_elements_by_xpath("//*[self::a or self::button]")
        
        # テキストサイズを200%に変更
        driver.execute_script("document.body.style.zoom = '200%'")
        
        resized_clickable = driver.find_elements_by_xpath("//*[self::a or self::button]")
        
        # クリック可能な要素の数が同じかチェック
        if len(original_clickable) == len(resized_clickable):
            print("Functionality is preserved after text resizing")
            return True
        else:
            print("Some functionality is lost after text resizing")
            return False
    except Exception as e:
        print(f"Error checking functionality preservation: {e}")
        return False
    finally:
        driver.quit()