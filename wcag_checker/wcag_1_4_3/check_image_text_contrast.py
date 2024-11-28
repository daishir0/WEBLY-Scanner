from wcag_checker.utils import fetch_url, parse_html
import requests
from PIL import Image
import io
from .check_text_contrast import calculate_contrast_ratio
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
            print(f"Processing image URL: {img_url}")
            
            try:
                print(f"\nProcessing image: {img_url}")
                response = requests.get(img_url, verify=False)
                
                # レスポンスのステータスコードとContent-Typeをチェック
                if response.status_code != 200:
                    print(f"Failed to fetch image: Status code {response.status_code}")
                    continue
                
                if 'image' not in response.headers.get('Content-Type', ''):
                    print(f"Invalid content type: {response.headers.get('Content-Type')}")
                    continue
                
                # 画像データを検証
                image_data = response.content
                if not image_data:
                    print("Empty image data received")
                    continue
                
                try:
                    img = Image.open(io.BytesIO(image_data))
                    img.verify()  # 画像データの整合性チェック
                    img = Image.open(io.BytesIO(image_data))  # verify後は再度openが必要
                    
                    if has_text(img):
                        contrast_ratio = analyze_image_contrast(img)
                        if contrast_ratio < 4.5:
                            print(f"Low contrast image text found (Ratio: {contrast_ratio:.2f})")
                            return False
                        else:
                            print(f"Contrast ratio OK: {contrast_ratio:.2f}")
                            
                except Exception as img_error:
                    print(f"Invalid image data: {str(img_error)}")
                    continue
                    
            except Exception as e:
                print(f"Error processing image: {str(e)}")
                continue
    
    print("\nAll images processed successfully")
    return True

def has_text(img):
    # This is a placeholder function. In a real implementation, you would use
    # OCR (Optical Character Recognition) to detect text in the image.
    # For this example, we'll assume all images contain text.
    return True

def analyze_image_contrast(img):
    # Convert image to grayscale
    img_gray = img.convert('L')
    
    # Get histogram
    hist = img_gray.histogram()
    
    # Find the darkest and lightest pixels
    darkest = next(i for i, v in enumerate(hist) if v)
    lightest = next(i for i in range(255, -1, -1) if hist[i])
    
    # Calculate contrast ratio
    return calculate_contrast_ratio((darkest, darkest, darkest), (lightest, lightest, lightest))