from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # フォームの存在を確認
    forms = soup.find_all('form')
    if not forms:
        print("フォームが見つかりません")
        return False
    
    # 入力フィールドの存在を確認
    input_fields = soup.find_all('input')
    if not input_fields:
        print("入力フィールドが見つかりません")
        return False
    
    # クライアントサイドバリデーションの存在を確認（簡易的な方法）
    scripts = soup.find_all('script')
    validation_keywords = ['validate', 'validation', 'checkForm', 'formCheck']
    has_validation = any(any(keyword in script.text.lower() for keyword in validation_keywords) for script in scripts if script.text)
    
    if has_validation:
        print("クライアントサイドバリデーションが検出されました")
        return True
    else:
        print("クライアントサイドバリデーションが検出されませんでした。手動確認が必要です")
        return None