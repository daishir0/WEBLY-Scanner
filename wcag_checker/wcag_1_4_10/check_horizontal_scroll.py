from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def check(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=600,256")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    page_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")

    driver.quit()

    if page_height <= viewport_height:
        print("水平スクロールコンテンツは256 CSS ピクセル高さで表示可能です。")
        return True
    else:
        print(f"水平スクロールコンテンツは256 CSS ピクセル高さで表示できません。ページ高さ: {page_height}px")
        return False