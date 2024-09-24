from wcag_checker.utils import fetch_url, parse_html
import re

def check_sound_dependency(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("URLのコンテンツの取得に失敗しました")
        return False
    
    soup = parse_html(html_content)
    
    # 音に関連する単語のリスト
    sound_words = ['音', '鳴る', '聞こえる']
    
    # テキストコンテンツを取得
    text_content = soup.get_text()
    
    # 音に関連する単語を検索
    sound_references = [word for word in sound_words if re.search(r'\b' + word + r'\b', text_content, re.IGNORECASE)]
    
    if sound_references:
        print(f"警告: 以下の音に関連する単語が検出されました: {', '.join(sound_references)}")
        print("手動確認が必要です: これらの単語が指示の唯一の手段として使用されていないか確認してください。")
        return False
    else:
        print("音への依存は検出されませんでした。")
        return True

def check(url):
    # ここにチェックロジックを追加
    # ���:
    # result = some_check_function(url)
    # return result
    pass  # これはプレースホルダーです。実際のロジックに置き換えてください。