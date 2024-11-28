from wcag_checker.utils import fetch_url, parse_html
import requests
from PIL import Image
import io
from .check_text_contrast import calculate_contrast_ratio
from .check_image_text_contrast import has_text, analyze_image_contrast
import urllib3
from urllib.parse import urljoin, urlparse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    # URLからベースURLを導出
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    print(f"Base URL derived: {base_url}")
    
    soup = parse_html(html_content)
    img_elements = soup.find_all('img')
    
    for img in img_elements:
        img_url = img.get('src')
        if img_url:
            # base_urlを使用してURLを生成
            img_url = urljoin(base_url, img_url.lstrip('/'))
            print(f"Processing large image URL: {img_url}")
            
            try:
                print(f"\nProcessing large image: {img_url}")
                response = requests.get(img_url, verify=False)
                
                # レスポンスの検証
                if response.status_code != 200:
                    print(f"Failed to fetch image: Status code {response.status_code}")
                    continue
                
                if 'image' not in response.headers.get('Content-Type', ''):
                    print(f"Invalid content type: {response.headers.get('Content-Type')}")
                    continue
                
                # 画像データの検証
                image_data = response.content
                if not image_data:
                    print("Empty image data received")
                    continue
                
                try:
                    img = Image.open(io.BytesIO(image_data))
                    img.verify()  # 画像データの整合性チェック
                    img = Image.open(io.BytesIO(image_data))  # verify後は再度open
                    
                    if has_text(img) and is_large_image(img):
                        contrast_ratio = analyze_image_contrast(img)
                        if contrast_ratio < 3:
                            print(f"Low contrast large image text found (Ratio: {contrast_ratio:.2f})")
                            return False
                        else:
                            print(f"Large image contrast ratio OK: {contrast_ratio:.2f}")
                            
                except Exception as img_error:
                    print(f"Invalid image data: {str(img_error)}")
                    continue
                    
            except Exception as e:
                print(f"Error processing image: {str(e)}")
                continue
    
    print("\nAll large images processed successfully")
    return True

def is_large_image(img):
    # This is a placeholder function. In a real implementation, you would
    # analyze the image to determine if the text within it is "large".
    # For this example, we'll consider images larger than 200x200 as "large".
    return img.width > 200 and img.height > 200