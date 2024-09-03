from wcag_checker.utils import fetch_url, parse_html
from PIL import Image
import pytesseract
import io
import requests

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # テキストコンテンツの検出
    text_content = soup.get_text(strip=True)
    if not text_content:
        print("ページにテキストコンテンツが見つかりません")
        return False
    
    # 画像の検出と分析
    images = soup.find_all('img')
    for img in images:
        src = img.get('src')
        if src:
            try:
                response = requests.get(src)
                img = Image.open(io.BytesIO(response.content))
                text = pytesseract.image_to_string(img)
                if text.strip():
                    print(f"画像内にテキストが検出されました: {src}")
                    return False
            except Exception as e:
                print(f"画像の分析中にエラーが発生しました: {e}")
    
    print("テキストが適切に使用されています")
    return True