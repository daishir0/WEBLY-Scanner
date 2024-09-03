from wcag_checker.utils import fetch_url, parse_html
from PIL import Image
import io
import requests
from colorsys import rgb_to_hls

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    text_elements = soup.find_all(text=True)
    
    for element in text_elements:
        parent = element.parent
        if parent.name not in ['script', 'style', 'head', 'title', 'meta', '[document]']:
            text_color = get_color(parent, 'color')
            bg_color = get_background_color(parent)
            
            if text_color and bg_color:
                contrast_ratio = calculate_contrast_ratio(text_color, bg_color)
                if contrast_ratio < 4.5:
                    print(f"Low contrast text found: {element.strip()[:30]}... (Ratio: {contrast_ratio:.2f})")
                    return False
    
    return True

def get_color(element, property):
    while element:
        color = element.get('style', '').split(f'{property}:')[-1].split(';')[0].strip()
        if color:
            return color_to_rgb(color)
        element = element.parent
    return None

def get_background_color(element):
    while element:
        bg_color = element.get('style', '').split('background-color:')[-1].split(';')[0].strip()
        if bg_color:
            return color_to_rgb(bg_color)
        element = element.parent
    return (255, 255, 255)  # Default to white if no background color is found

def color_to_rgb(color):
    if color.startswith('#'):
        return tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
    elif color.startswith('rgb'):
        return tuple(map(int, color.strip('rgb()').split(',')))
    else:
        return None

def calculate_contrast_ratio(color1, color2):
    l1 = relative_luminance(color1)
    l2 = relative_luminance(color2)
    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)

def relative_luminance(rgb):
    r, g, b = [x / 255 for x in rgb]
    r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
    return 0.2126 * r + 0.7152 * g + 0.0722 * b