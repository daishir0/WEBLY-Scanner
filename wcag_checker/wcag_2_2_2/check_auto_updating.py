import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_meta_refresh(url):
    try:
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.text, "html.parser")
        meta_refresh = soup.find("meta", attrs={"http-equiv": "refresh"})

        if meta_refresh:
            print("⚠️ 自動更新するメタタグが見つかりました。")
            print("手動で確認が必要です: ユーザーが一時停止、停止、非表示、または更新頻度を調整するメカニズムがあるかを確認してください。")
            return False
    except requests.exceptions.RequestException as e:
        print(f"警告: URLのチェック中にエラーが発生しました: {url}")
        print(f"エラー詳細: {str(e)}")
        return True

    return True

def check_iframes(url):
    try:
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.text, "html.parser")
        iframes = soup.find_all("iframe")

        for iframe in iframes:
            iframe_url = urljoin(url, iframe.get("src", ""))
            print(f"iframe内のコンテンツをチェックします: {iframe_url}")
            if not check_meta_refresh(iframe_url):
                return False
    except requests.exceptions.RequestException as e:
        print(f"警告: iframeのチェック中にエラーが発生しました: {url}")
        print(f"エラー詳細: {str(e)}")
        return True

    return True

def check(url):
    if not check_meta_refresh(url):
        return False

    if not check_iframes(url):
        return False

    print("✅ 自動更新する要素は検出されませんでした。")
    return True