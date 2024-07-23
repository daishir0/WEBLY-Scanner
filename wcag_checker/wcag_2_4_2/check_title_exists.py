from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    # print("Fetched HTML content:", html_content[:500])  # 最初の500文字を表示
    soup = parse_html(html_content)
    if soup.title and soup.title.string.strip():
        print("Title found:", soup.title.string.strip())
        return True
    else:
        print("Title not found or empty")
        return False