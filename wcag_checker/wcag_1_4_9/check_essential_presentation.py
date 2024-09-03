from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # テキストの画像を検出する（この例では、alt属性を持つimg要素を検索）
    text_images = soup.find_all('img', alt=True)
    
    if not text_images:
        print("No text images found")
        return True
    
    print("Manual check required: Verify if the following text images have essential presentation:")
    for img in text_images:
        print(f"- Image with alt text: {img['alt']}")
    
    return None  # 手動チェックが必要