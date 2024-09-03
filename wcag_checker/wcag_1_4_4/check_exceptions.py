from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    
    # キャプションと画像化されたテキストの検出
    captions = soup.find_all('caption')
    img_text = soup.find_all('img', alt=True)
    
    if captions or img_text:
        print("Captions or image text found. Manual check required.")
        return None  # Manual check required
    else:
        print("No exceptions (captions or image text) found")
        return True