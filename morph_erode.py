import cv2
import numpy as np

### 모폴로지 : 형태학이란 뜻으로 영상 분야에서는 노이즈 제거, 구멍 메꾸기, 연결되지 않은 경계 이어붙이기 등 형태학적 관점에서의 영상 연산을 말함
# 1. 침식 연산 : 원래 있던 객체의 영역을 깎아 내는 연산
# 이 연산을 위해 구조화 요소라는 0과 1로 채워진 커널이 필요한데, 1이 채워진 모양에 따라 사각형, 타원형, 십자형 등을 사용할 수 있음
# 구조화 요소 커널 생성을 위한 함수로는 cv2.getStructuringElement()를, 침식 연산을 위한 함수로는 cv2.erode()를 제공함

img = cv2.imread('./img/morph_dot.png')

# 구조화 요소 커널, 사각형(3x3) 생성
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 침식 연산 적용
erosion =  cv2.erode(img, k)

# 결과 출력
merged = np.hstack((img, erosion))
cv2.imshow('Erode', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()