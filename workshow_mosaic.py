import cv2

### 기하학적 변환4 : 모자이크 처리
# 특정 영역을 작게 축소했다가 다시 확대하면 원래의 픽셀과 비슷하긴 하지만 연산한 결과라 선명도가 떨어져 뿌옇게 보인다.

rate = 15            # 모자이크에 사용할 축소 비율(1/rate)
win_title = 'mosaic' # 창 제목
img = cv2.imread('./img/taekwonv1.jpg') # 이미지 읽기

while True:
    x, y, w, h = cv2.selectROI(win_title, img, False) # 관심영역 선택
    if w and h:
        roi = img[y:y+h, x:x+w]  # 관심영역 지정
        roi = cv2.resize(roi, (w//rate, h//rate)) # 1/rate 비율로 축소
        # 원래 크기로 확대
        roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_AREA)
        img[y:y+h, x:x+w] = roi  # 원본 이미지에 적용
        cv2.imshow(win_title, img)
    else:
        break
cv2.destroyAllWindows()
