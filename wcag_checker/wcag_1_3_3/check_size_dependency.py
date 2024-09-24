from wcag_checker.utils import fetch_url, parse_html
import re

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLのコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # サイズに関連する単語のリスト
    size_words = ['大きい', '小さい', '中くらい']
    
    # テキストコンテンツを取得
    text_content = soup.get_text()
    
    # サイズに関連する単語を検索
    size_references = [word for word in size_words if re.search(r'\b' + word + r'\b', text_content, re.IGNORECASE)]
    
    if size_references:
        print(f"警告: 以下のサイズに関連する単語が検出されました: {', '.join(size_references)}")
        print("手動確認が必要です: これらの単語が指示の唯一の手段として使用されていないか確認してください。")
        return False
    else:
        print("サイズへの依存は検出されませんでした。")
        return True