from wcag_checker.utils import fetch_url, parse_html
import re

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLのコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # 形状に関連する単語のリスト
    shape_words = ['円形', '四角', '三角', '丸い', '四角い', '三角形']
    
    # テキストコンテンツを取得
    text_content = soup.get_text()
    
    # 形状に関連する単語を検索
    shape_references = [word for word in shape_words if re.search(r'\b' + word + r'\b', text_content, re.IGNORECASE)]
    
    if shape_references:
        print(f"警告: 以下の形状に関連する単語が検出されました: {', '.join(shape_references)}")
        print("手動確認が必要です: これらの単語が指示の唯一の手段として使用されていないか確認してください。")
        return False
    else:
        print("形状への依存は検出されませんでした。")
        return True