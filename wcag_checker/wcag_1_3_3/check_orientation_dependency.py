from wcag_checker.utils import fetch_url, parse_html
import re

def check_orientation_dependency(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLのコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # 方向に関連する単語のリスト
    orientation_words = ['縦', '横']
    
    # テキストコンテンツを取得
    text_content = soup.get_text()
    
    # 方向に関連する単語を検索
    orientation_references = [word for word in orientation_words if re.search(r'\b' + word + r'\b', text_content, re.IGNORECASE)]
    
    if orientation_references:
        print(f"警告: 以下の方向に関連する単語が検出されました: {', '.join(orientation_references)}")
        print("手動確認が必要です: これらの単語が指示の唯一の手段として使用されていないか確認してください。")
        return False
    else:
        print("方向への依存は検出されませんでした。")
        return True

def check(url):
    return check_orientation_dependency(url)  # check関数が正しく定義されていることを確認