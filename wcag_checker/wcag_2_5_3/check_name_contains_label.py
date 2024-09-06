from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    ui_components = soup.find_all(['button', 'input', 'select', 'textarea'])
    
    for component in ui_components:
        label_text = get_label_text(component, soup)
        name = component.get('aria-label') or component.get('title') or component.get('placeholder')
        
        if label_text and name and label_text.lower() in name.lower():
            return True
    
    print("名前にラベルのテキストが含まれるコンポーネントが見つかりませんでした")
    return False

def get_label_text(component, soup):
    if component.get('id'):
        label = soup.find('label', attrs={'for': component['id']})
        if label:
            return label.string
    return None