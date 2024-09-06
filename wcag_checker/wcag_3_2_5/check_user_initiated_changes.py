from wcag_checker.utils import fetch_url, parse_html
import re

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # 自動更新、自動リダイレクト、ポップアップウィンドウ、selectの変更イベントをチェック
    auto_refresh = soup.find('meta', attrs={'http-equiv': re.compile(r'refresh', re.I)})
    auto_redirect = soup.find('script', text=re.compile(r'window.location', re.I))
    popup_windows = soup.find_all('a', attrs={'target': '_blank'})
    select_onchange = soup.find_all('select', attrs={'onchange': True})

    if auto_refresh or auto_redirect:
        print("自動更新または自動リダイレクトが検出されました")
        return False
    
    if popup_windows:
        print("ポップアップウィンドウが検出されました。ユーザーの要求時のみ開くか確認が必要です")
    
    if select_onchange:
        print("selectの変更イベントが検出されました。コンテキスト変更を引き起こさないか確認が必要です")
    
    print("手動確認が必要: すべてのコンテキスト変更がユーザーの要求によってのみ開始されることを確認してください")
    return None  # 完全な自動チェックは困難なため、手動確認が必要