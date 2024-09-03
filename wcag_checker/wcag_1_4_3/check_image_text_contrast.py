from wcag_checker.utils import fetch_url, parse_html
import requests
from PIL import Image
import io
from .check_text_contrast import calculate_contrast_ratio

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    img_elements = soup.find_all('img')
    
    for img in img_elements:
        img_url = img.get('src')
        if img_url:
            if not img_url.startswith('http'):
                img_url = url + img_url
            
            try:
                response = requests.get(img_url)
                img = Image.open(io.BytesIO(response.content))
                
                if has_text(img):
                    contrast_ratio = analyze_image_contrast(img)
                    if contrast_ratio < 4.5:
                        print(f"Low contrast image text found: {img_url} (Ratio: {contrast_ratio:.2f})")
                        return False
            except Exception as e:
                print(f"Error processing image {img_url}: {e}")
    
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