from wcag_checker.utils import fetch_url, parse_html
from wcag_checker.color_utils import calculate_contrast_ratio

def check_ui_components(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    ui_components = soup.find_all(['button', 'input', 'select', 'textarea', 'a'])
    
    for component in ui_components:
        # コンポーネントの背景色と前景色を取得
        bg_color = component.get('style', {}).get('background-color', '#FFFFFF')
        fg_color = component.get('style', {}).get('color', '#000000')
        
        # コントラスト比を計算
        contrast_ratio = calculate_contrast_ratio(bg_color, fg_color)
        
        if contrast_ratio is None:
            print(f"Warning: Contrast ratio is None for component {component}. Skipping this component.")
            continue
        
        if contrast_ratio < 3:
            return False
    
    return True