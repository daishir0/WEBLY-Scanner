from wcag_checker.utils import fetch_url, parse_html
import requests
from PIL import Image
import io
from .check_text_contrast import calculate_contrast_ratio
from .check_image_text_contrast import has_text, analyze_image_contrast

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
                
                if has_text(img) and is_large_image(img):
                    contrast_ratio = analyze_image_contrast(img)
                    if contrast_ratio < 3:
                        print(f"Low contrast large image text found: {img_url} (Ratio: {contrast_ratio:.2f})")
                        return False
            except Exception as e:
                print(f"Error processing image {img_url}: {e}")
    
    return True

def is_large_image(img):
    # This is a placeholder function. In a real implementation, you would
    # analyze the image to determine if the text within it is "large".
    # For this example, we'll consider images larger than 200x200 as "large".
    return img.width > 200 and img.height > 200