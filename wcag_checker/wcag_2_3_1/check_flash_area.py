from wcag_checker.utils import fetch_url, parse_html
import cv2
import numpy as np

def check(url):
    video_content = fetch_url(url)
    if video_content is None:
        print("URLコンテンツの取得に失敗しました")
        return False
    
    # ビデオを読み込む
    cap = cv2.VideoCapture(video_content)
    
    # ビデオの解像度を取得
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # 10度の視野に相当する面積を計算（画面の25%）
    max_flash_area = width * height * 0.25
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # フレーム間の差分を計算
        if 'prev_frame' in locals():
            diff = cv2.absdiff(frame, prev_frame)
            
            # 点滅領域を検出
            _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
            flash_area = np.sum(thresh == 255)
            
            # 点滅面積が閾値を超える場合、Falseを返す
            if flash_area > max_flash_area:
                cap.release()
                return False
        
        prev_frame = frame
    
    cap.release()
    return True