from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import cv2
import numpy as np
import os

def capture_screenshots(url, num_screenshots, interval):
    options = Options()
    options.headless = True
    options.binary_location = "/usr/bin/google-chrome"
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--enable-logging')
    options.add_argument('--log-level=1')
    options.add_argument("--headless")

    service = Service(executable_path="/usr/bin/chromedriver")

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1920, 2160)

    driver.get(url)
    time.sleep(5)

    screenshots = []
    for i in range(num_screenshots):
        screenshot_path = f'/tmp/screenshot_{i}.png'
        driver.save_screenshot(screenshot_path)
        screenshot = cv2.imread(screenshot_path)
        screenshots.append(screenshot)
        time.sleep(interval)

    driver.quit()
    return screenshots

def detect_moving_elements(screenshots):
    diff_threshold = 30
    moving_elements = []

    for i in range(len(screenshots) - 1):
        diff = cv2.absdiff(screenshots[i], screenshots[i + 1])
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blurred, diff_threshold, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) < 100:
                continue
            x, y, w, h = cv2.boundingRect(contour)
            moving_elements.append((x, y, w, h))

    return moving_elements

def check(url, num_screenshots=3, interval=0.5):
    screenshots = capture_screenshots(url, num_screenshots, interval)
    moving_elements = detect_moving_elements(screenshots)

    if len(moving_elements) > 0:
        print("⚠️ 動く、点滅する、またはスクロールする要素が検出されました。")
        print("手動で確認が必要です: 要素が自動的に開始し、5秒以上継続し、他のコンテンツと並行して表示されているか、")
        print("およびユーザーが一時停止、停止、または非表示にするメカニズムがあるかを確認してください。")
        return False
    else:
        print("✅ 動く、点滅する、またはスクロールする要素は検出されませんでした。")
        return True