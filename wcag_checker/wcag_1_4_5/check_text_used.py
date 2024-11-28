from wcag_checker.utils import fetch_url, parse_html
from PIL import Image
import pytesseract
import io
import requests
from urllib.parse import urljoin, urlparse
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check(url):
    print("\n=== Starting Text Used Check ===")
    print(f"Input URL: {url}")
    
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    print(f"Base URL derived: {base_url}")
    
    soup = parse_html(html_content)
    img_elements = soup.find_all('img')
    print(f"Found {len(img_elements)} images")
    
    for i, img in enumerate(img_elements, 1):
        src = img.get('src')
        if not src:
            print(f"Image {i}: No src attribute")
            continue
            
        print(f"\nProcessing image {i}/{len(img_elements)}")
        print(f"Original src: {src}")
        
        try:
            if not src.startswith(('http://', 'https://')):
                full_url = urljoin(base_url, src.lstrip('/'))
                print(f"Converted URL: {full_url}")
            else:
                full_url = src
                print(f"Using original URL: {full_url}")
            
            print(f"Fetching image from: {full_url}")
            response = requests.get(full_url, verify=False)
            
            if response.status_code == 200:
                print("Successfully fetched image")
                img = Image.open(io.BytesIO(response.content))
                
                text = pytesseract.image_to_string(img)
                if text.strip():
                    print(f"Text detected in image: {text[:50]}...")
                else:
                    print("No text detected in image.")
                    
            else:
                print(f"Failed to fetch image: HTTP {response.status_code}")
                
        except Exception as e:
            print(f"Error processing image: {str(e)}")
            continue
    
    print("\n=== Text Used Check completed ===")
    return True