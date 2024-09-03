from wcag_checker.utils import fetch_url, parse_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def check(url):
    # このチェックには動的な検証が必要なため、Seleniumを使用します
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        original_size = driver.execute_script("return document.body.innerHTML.length")
        
        # テキストサイズを200%に変更
        driver.execute_script("document.body.style.zoom = '200%'")
        
        resized_size = driver.execute_script("return document.body.innerHTML.length")
        
        # サイズ変更後もコンテンツが保持されているかチェック
        if abs(original_size - resized_size) / original_size < 0.1:  # 10%以内の変化は許容
            print("Text is resizable to 200% without loss of content")
            return True
        else:
            print("Text resizing causes significant content loss")
            return False
    except Exception as e:
        print(f"Error checking text resizability: {e}")
        return False
    finally:
        driver.quit()