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
    
    # フレームレートを取得
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # 1秒間のフレーム数
    frames_per_second = int(fps)
    
    # 点滅回数をカウント
    flash_count = 0
    prev_frame = None
    
    for i in range(frames_per_second):
        ret, frame = cap.read()
        if not ret:
            break
        
        if prev_frame is not None:
            # フレーム間の差分を計算
            diff = cv2.absdiff(frame, prev_frame)
            
            # 差分が大きい場合、点滅としてカウント
            if np.mean(diff) > 10:  # 閾値は調整が必要
                flash_count += 1
        
        prev_frame = frame
    
    cap.release()
    
    # 1秒間の点滅回数が3回以下であればTrue
    return flash_count <= 3