import cv2
import numpy as np

### 영상 필터2 : 미디언 블러링

img = cv2.imread("./img/salt_pepper_noise.jpg")

# 1. 미디언 블러 적용
# cv2.medianBlur() 함수를 이용해서 커널 영역 픽셀 값 중에 중간 값을 대상 픽셀 값으로 선택하는 걸 미디언 블러링이라고 함
blur = cv2.medianBlur(img, 5)

# 2. 결과 출력
merged = np.hstack((img, blur))
cv2.imshow('media', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()