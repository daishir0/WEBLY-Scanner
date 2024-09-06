from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 通常とは異なる方法で使用される単語や語句の定義を探す
    # この部分も完全な自動化が難しいため、ヒューリスティックな方法を使用
    potential_unusual_words = soup.find_all(['span', 'abbr', 'dfn'], title=True)
    glossary = soup.find('dl')  # 用語集を探す
    
    if potential_unusual_words or glossary:
        print("潜在的な通常とは異なる使用の単語や語句の定義が見つかりました。手動での確認が必要です。")
        if potential_unusual_words:
            for word in potential_unusual_words[:5]:  # 最初の5つの例を表示
                print(f"- {word.text}: {word['title']}")
        if glossary:
            print("用語集が見つかりました。")
        return None  # 手動確認が必要
    else:
        print("通常とは異なる使用の単語や語句の定義が見つかりませんでした。")
        return False