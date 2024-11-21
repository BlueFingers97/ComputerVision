import cv2
import numpy as np

### 이미지 연산 : 이미지 합성과 마스킹

# 1. 합성 대상 영상 읽기
img1 = cv2.imread("./img/drawing.jpg")
img2 = cv2.imread("./img/my_hand.jpg")

# 2. 마스크 생성, 합성할 이미지 전체 영역을 255로 셋팅(해당 영역 전부가 합성의 대상임을 표시)
mask = np.full_like(img1, 255)

# 3. 합성 대상 좌표 계산(img2의 중앙)
height, width = img2.shape[:2]
center = (width//2, height//2)  # --> 여기 '/' 하나만 써서 인자값 잘못됐다는 에러 나는 거였음

# 4. seamlessClone 으로 합성  --> 여기서 에러나는데 이유를 모르겠네...
# img1을 img2에다가 mask에 지정된 영역만큼 center 좌표에 합성, 함수의 인자가 cv2.NORMAL_CLONE인 경우 꽃 그림이 선명하지만 주변의 피부가 뭉겨진 듯한 결과를 보임
normal = cv2.seamlessClone(img1, img2, mask, center, cv2.NORMAL_CLONE)
mixed = cv2.seamlessClone(img1, img2, mask, center, cv2.MIXED_CLONE) # cv2.MIXED_CLONE을 사용하여 두 영상의 특징을 살려 표현함

# 5. 결과 출력
cv2.imshow('normal', normal)
cv2.imshow('mixed', mixed)
cv2.waitKey()
cv2.destroyAllWindows()