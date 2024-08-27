# ./wcag_1_2_1/check_media_alternative.py

from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return None
    
    soup = parse_html(html_content)
    media_elements = soup.find_all(['audio', 'video'])
    
    if not media_elements:
        print("No media content found")
        return True
    
    for media in media_elements:
        if 'aria-label' in media.attrs and 'alternative' in media['aria-label'].lower():
            print("Media content is labeled as an alternative to text")
            return True
    
    print("Manual check required: Verify if media content is an alternative to text and clearly labeled as such")
    return None