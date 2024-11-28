from wcag_checker.utils import fetch_url, parse_html
from urllib.parse import urljoin, urlparse
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check(url):
    print("\n=== Starting Essential Image Text Check ===")
    print(f"Input URL: {url}")
    
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    # URLの解析をデバッグ出力
    parsed_url = urlparse(url)
    print(f"\nParsed URL components:")
    print(f"- scheme: {parsed_url.scheme}")
    print(f"- netloc: {parsed_url.netloc}")
    print(f"- path: {parsed_url.path}")
    
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    print(f"Base URL: {base_url}")
    
    soup = parse_html(html_content)
    img_elements = soup.find_all('img')
    print(f"\nFound {len(img_elements)} images")
    
    for i, img in enumerate(img_elements, 1):
        src = img.get('src')
        print(f"\n--- Processing image {i}/{len(img_elements)} ---")
        print(f"Original src: {src}")
        
        if not src:
            print("No src attribute found, skipping")
            continue
            
        try:
            # 相対パスを絶対URLに変換
            if not src.startswith(('http://', 'https://')):
                full_url = urljoin(base_url, src.lstrip('/'))
                print(f"Converting relative path to absolute URL:")
                print(f"- Base URL: {base_url}")
                print(f"- Relative path: {src}")
                print(f"- Full URL: {full_url}")
            else:
                full_url = src
                print(f"URL is already absolute: {full_url}")
            
            # 画像の取得を試行
            print(f"Attempting to fetch image: {full_url}")
            response = requests.get(full_url, verify=False)
            print(f"Response status code: {response.status_code}")
            
            if response.status_code == 200:
                print("Successfully fetched image")
                # 画像処理の続き...
            else:
                print(f"Failed to fetch image: HTTP {response.status_code}")
                
        except Exception as e:
            print(f"Error processing image: {str(e)}")
            print(f"Error type: {type(e)}")
            continue
    
    print("\n=== Essential Image Text Check completed ===")
    return True