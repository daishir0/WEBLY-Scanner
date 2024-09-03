from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def check(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=320,600")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    page_width = driver.execute_script("return document.body.scrollWidth")
    viewport_width = driver.execute_script("return window.innerWidth")

    driver.quit()

    if page_width <= viewport_width:
        print("垂直スクロールコンテンツは320 CSS ピクセル幅で表示可能です。")
        return True
    else:
        print(f"垂直スクロールコンテンツは320 CSS ピクセル幅で表示できません。ページ幅: {page_width}px")
        return False