from wcag_checker.utils import fetch_url, parse_html
from .check_text_contrast import get_color, get_background_color, calculate_contrast_ratio

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False
    
    soup = parse_html(html_content)
    large_text_elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    large_text_elements += soup.find_all(style=lambda value: value and ('font-size' in value and is_large_font(value)))
    
    for element in large_text_elements:
        text_color = get_color(element, 'color')
        bg_color = get_background_color(element)
        
        if text_color and bg_color:
            contrast_ratio = calculate_contrast_ratio(text_color, bg_color)
            if contrast_ratio < 3:
                print(f"Low contrast large text found: {element.text.strip()[:30]}... (Ratio: {contrast_ratio:.2f})")
                return False
    
    return True

def is_large_font(style):
    font_size = style.split('font-size:')[-1].split(';')[0].strip()
    if 'pt' in font_size:
        size = float(font_size.replace('pt', ''))
        return size >= 14
    elif 'px' in font_size:
        size = float(font_size.replace('px', ''))
        return size >= 18.5
    else:
        return False