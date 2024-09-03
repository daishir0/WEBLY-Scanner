from wcag_checker.utils import fetch_url, parse_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def check(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        original_content = driver.find_elements_by_xpath("//*[text()]")
        
        # テキストサイズを200%に変更
        driver.execute_script("document.body.style.zoom = '200%'")
        
        resized_content = driver.find_elements_by_xpath("//*[text()]")
        
        # コンテンツの数が同じかチェック
        if len(original_content) == len(resized_content):
            print("Content is preserved after text resizing")
            return True
        else:
            print("Some content is lost after text resizing")
            return False
    except Exception as e:
        print(f"Error checking content preservation: {e}")
        return False
    finally:
        driver.quit()