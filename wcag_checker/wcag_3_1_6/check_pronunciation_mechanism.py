from wcag_checker.utils import fetch_url, parse_html
import re

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    
    # 発音情報の直接提供をチェック
    if re.search(r'\([/ˈˌ.əɪuɔæ]+\)', str(soup)):
        return True
    
    # 発音へのリンクをチェック
    if soup.find('a', href=re.compile(r'pronunciation|audio')):
        return True
    
    # 用語集へのリンクをチェック
    if soup.find('a', href=re.compile(r'glossary')):
        return True
    
    # rubyタグの使用をチェック
    if soup.find('ruby'):
        return True
    
    print("Manual check required: Verify if there's a mechanism to identify specific pronunciation of words.")
    return False