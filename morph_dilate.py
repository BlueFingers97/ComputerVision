import cv2
import numpy as np

### 모폴로지2 - 평창 연산(침식과 반대로 영상 속 사물의 주변을 덧붙여서 영역을 더 확장하는 연산)

img = cv2.imread('./img/morph_hole.png')

# 구조화 요소 커널, 사각형(3x3) 생성
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 팽창 연산 적용
dst = cv2.dilate(img, k)

# 결과 출력
merged = np.hstack((img, dst))
cv2.imshow('Dilation', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()