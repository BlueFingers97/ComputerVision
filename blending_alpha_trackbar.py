import cv2

### 이미지 프로세싱 : 알파 블렌딩

win_name = 'Alpha Blending'  # 창 이름
tracker_name = 'fade'        # 트랙바 이름

# 트랙바 이벤트 핸들러 함수
def onChange(x):
    alpha = x/100
    dst = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0) # 알파 블렌딩
    cv2.imshow(win_name, dst)

# 합성 영상 읽기
img1 = cv2.imread('./img/man_face.jpg')
img2 = cv2.imread('./img/lion_face.jpg')

# 이미지 표시 및 트랙바 붙이기
cv2.imshow(win_name, img1)
cv2.createTrackbar(tracker_name, win_name, 0, 100, onChange) # 트랙바를 움직여서 알파 값을 조정하면 서서히 바뀌는 것처럼 보임

cv2.waitKey()
cv2.destroyAllWindows()