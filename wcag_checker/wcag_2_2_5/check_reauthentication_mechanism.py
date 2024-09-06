from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # ログインフォームや再認証リンクを探す
    login_form = soup.find('form', id='login') or soup.find('form', class_='login')
    reauth_link = soup.find('a', string=re.compile(r'再認証|ログイン', re.I))
    
    if login_form or reauth_link:
        print("再認証メカニズムが見つかりました")
        return True
    else:
        print("再認証メカニズムが見つかりませんでした。手動確認が必要です。")
        return None  # 手動確認が必要