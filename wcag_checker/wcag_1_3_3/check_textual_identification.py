from wcag_checker.utils import fetch_url, parse_html
import re

def check_textual_identification(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLのコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # テキストに関連する単語のリスト
    text_words = ['テキスト', '文字']
    
    # テキストコンテンツを取得
    text_content = soup.get_text()
    
    # テキストに関連する単語を検索
    text_references = [word for word in text_words if re.search(r'\b' + word + r'\b', text_content, re.IGNORECASE)]
    
    if text_references:
        print(f"警告: 以下のテキストに関連する単語が検出されました: {', '.join(text_references)}")
        print("手動確認が必要です: これらの単語が指示の唯一の手段として使用されていないか確認してください。")
        return False
    else:
        print("テキストへの依存は検出されませんでした。")
        return True

def check(url):
    return check_textual_identification(url)  # check関数が正しく定義されていることを確認