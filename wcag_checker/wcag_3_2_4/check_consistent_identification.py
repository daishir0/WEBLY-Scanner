from wcag_checker.utils import fetch_url, parse_html
from collections import defaultdict

def check(url_set):
    components = defaultdict(list)
    
    for url in url_set:
        html_content = fetch_url(url)
        if html_content is None:
            print(f"Failed to fetch URL content: {url}")
            continue
        
        soup = parse_html(html_content)
        
        # ここでコンポーネントを抽出し、その識別子（ラベル、名前、テキスト代替など）を収集します
        # 例: ボタン、リンク、フォーム要素など
        buttons = soup.find_all('button')
        for button in buttons:
            components['button'].append({
                'url': url,
                'text': button.text.strip(),
                'aria-label': button.get('aria-label', ''),
                'title': button.get('title', '')
            })
        
        # 他のコンポーネントタイプに対しても同様の処理を行います
    
    # 収集したコンポーネントの一貫性をチェックします
    inconsistencies = []
    for component_type, instances in components.items():
        identifiers = defaultdict(set)
        for instance in instances:
            key = (instance['text'], instance['aria-label'], instance['title'])
            identifiers[key].add(instance['url'])
        
        if len(identifiers) > 1:
            inconsistencies.append(f"Inconsistent {component_type} identifiers found")
    
    if inconsistencies:
        print("Manual check required: Inconsistencies found in component identification")
        for inconsistency in inconsistencies:
            print(f"- {inconsistency}")
        return False
    
    return True