from wcag_checker.utils import fetch_url, parse_html
import re

def check_sensory_characteristics(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLのコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # 形状、色、サイズ、視覚的位置、方向、音に関連する単語のリスト
    sensory_words = {
        'shape': ['円形', '四角', '三角', '丸い', '四角い', '三角形'],
        'color': ['赤', '青', '緑', '黄色', '黒', '白'],
        'size': ['大きい', '小さい', '中くらい'],
        'location': ['上', '下', '左', '右', '中央'],
        'orientation': ['縦', '横'],
        'sound': ['音', '鳴る', '聞こえる']
    }
    
    # テキストコンテンツを取得
    text_content = soup.get_text()
    
    # 感覚的特徴に関連する単語を検索
    sensory_references = {key: [word for word in words if re.search(r'\b' + word + r'\b', text_content, re.IGNORECASE)] for key, words in sensory_words.items()}
    
    issues_found = False
    for key, references in sensory_references.items():
        if references:
            print(f"警告: 以下の{key}に関連する単語が検出されました: {', '.join(references)}")
            print("手動確認が必要です: これらの単語が指示の唯一の手段として使用されていないか確認してください。")
            issues_found = True
    
    if not issues_found:
        print("感覚的特徴への依存は検出されませんでした。")
        return True
    else:
        return False