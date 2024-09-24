from wcag_checker.utils import fetch_url, parse_html
import re

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLのコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # 色に関連する単語のリスト
    color_words = ['赤', '青', '緑', '黄色', '黒', '白']
    
    # テキストコンテンツを取得
    text_content = soup.get_text()
    
    # 色に関連する単語を検索
    color_references = [word for word in color_words if re.search(r'\b' + word + r'\b', text_content, re.IGNORECASE)]
    
    if color_references:
        print(f"警告: 以下の色に関連する単語が検出されました: {', '.join(color_references)}")
        print("手動確認が必要です: これらの単語が指示の唯一の手段として使用されていないか確認してください。")
        return False
    else:
        print("色への依存は検出されませんでした。")
        return True