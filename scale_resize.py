import cv2
import numpy as np

### 기하학적 변환2 : 확대, 축소

img = cv2.imread('./img/fish.jpg')
height, width = img.shape[:2]

# 1. 크기 지정으로 축소(확대 축소 기능은 cv2.resize() 함수 통해서 진행, 원본 크기의 0.5 곱해서 결과 크기 전달)
dst1 = cv2.resize(img, (int(width*0.5), int(height*0.5)),
                  interpolation=cv2.INTER_AREA)

# 2. 배율 지정으로 확대(변경하고 싶은 픽셀 크기를 직접 지정하거나 변경할 배율을 지정할 수 있음, 크기 인자 None으로 처리하고, 배율 두 배로 전달)
dst2 = cv2.resize(img, None, None, 2, 2, cv2.INTER_CUBIC)

# 3. 결과 출력
cv2.imshow("original", img)
cv2.imshow("small", dst1)
cv2.imshow("big", dst2)
cv2.waitKey()
cv2.destroyAllWindows()