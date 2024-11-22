import re  # 追加
from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    try:
        # コンテキスト変更をオフにするメカニズムの存在をチェック
        disable_options = soup.find_all(['input', 'select', 'button'], 
            text=re.compile(r'(disable|turn off|stop) (context changes|updates)', re.I))
        
        if disable_options:
            print("コンテキスト変更をオフにするメカニズムが検出されました")
            return True
        else:
            print("コンテキスト変更をオフにするメカニズムが検出されませんでした")
            print("手動確認が必要: コンテキスト変更をオフにするメカニズムが利用可能か確認してください")
            return None  # 完全な自動チェックは困難なため、手動確認が必要
            
    except Exception as e:
        print(f"チェック中にエラーが発生しました: {str(e)}")
        return False