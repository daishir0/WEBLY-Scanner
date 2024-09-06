from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # ヘルプ要素の可視性を確認
    help_elements = soup.find_all(['a', 'button', 'div'], text=lambda text: text and 'ヘルプ' in text.lower())
    help_elements += soup.find_all(['a', 'button', 'div'], title=lambda title: title and 'ヘルプ' in title.lower())
    
    if help_elements:
        for element in help_elements:
            # 要素が非表示でないか確認
            if 'style' in element.attrs and ('display:none' in element['style'] or 'visibility:hidden' in element['style']):
                print("ヘルプ要素が非表示になっています")
                return False
        print("ヘルプ要素が可視状態です")
        return True
    else:
        print("ヘルプ要素が見つかりませんでした")
        return False